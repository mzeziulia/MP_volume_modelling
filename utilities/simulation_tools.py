import numpy as np
import nernst_potentials as P
import ionic_fluxes as i_flux
import dep_functions as F
from config import *


def compute_flows(time_step, 
    internal_ions, 
    V_t,
    G = G,
    external_ions = external_ions,
    A_from_V_const = A_from_V_const,
    X_amount = None,
    buffer_capacity_T0 = None, 
    V_t0 = None, 
    c_spec = None, 
    RT = 2578.5871, 
    F = 96485.0
):
    '''
    Parameters
    =============
    `time_step` [float]:
        - which timestep (in seconds)
    `internal_ions` [1D np.ndarray]:
        -vector of internal ion amounts (in moles)
    `external_ions` [1D np.ndarray]:
        -vector of external ion amounts (in moles)
    `V_t` [float]:
        - current volume (in m3)
    "G" [dict]:
        - dictionary containing conductances (in UNITS HERE) for the following channel types:
            - ASOR, ClC, ...
    `X_amount` [float]:
        - amount of unaccounted for ions (in moles)
    `A_from_V_const` [float]
        - area calculated from the volume
    `buffer_capacity_T0` [float]:
        - buffer capacity at initial time
    `V_t0` [float]:
        - initial volume (in m3)
    `c_spec` [float]:
        - membrane capacitance (in F/(m**2))
    `RTdivF` [float]:
        - RT / F
    `RT` [float]:
        - Gas constant x Temperature 
    `F` [float]:
        - Faraday's constant

    Returns
    ===========

    '''

    dIons_dt = np.zeros_like(internal_ions)

    Buffer_T=buffer_capacity_T0*(V_t/V_t0)
    h_i = internal_ions[H_idx]/(V_t*1000)

    # toggle buffering
    hprime_o =  external_ions[H_idx] * buffer_capacity_T0
    hprime_i = h_i * Buffer_T

    A=A_from_V_const*(V_t**(2/3))
    C=A*c_spec
    Q = (internal_ions[Na_idx] + internal_ions[K_idx] + internal_ions[H_idx] -  internal_ions[Cl_idx] + X_amount) * F
    U = Q / C 
    
    cl_i = cl_i_amount/(V_t*1000)
    na_i = internal_ions[Na_idx]/(V_t*1000)
    k_i = internal_ions[K_idx]/(V_t*1000)

    pH_local=-np.log10(hprime_i)

    RTdivF = RT / F

    # compute potentials from different channels
    potential_asor = P.nernst_potential_Cl_asor(U, external_ions[Cl_idx], cl_i, RTdivF)
    potential_CLC = P.nernst_potential_CLC(U, cl_i, external_ions[Cl_idx], hprime_i, hprime_o, RT, F)
    n_potential_Na_TPC = P.nernst_potential_Na_K(U, external_ions[Na_idx], na_i, RTdivF)
    potential_nhe = P.potential_NHE(external_ions[Na_idx], na_i, hprime_i, hprime_o)
    potential_k= P.nernst_potential_Na_K(U, external_ions[K_idx], k_i, RTdivF)
    potential_Cl_OH= P.nernst_potential_Cl_OH(external_ions[Cl_idx], cl_i, hprime_i, hprime_o)
    potential_VATPase= P.nernst_potential_VATPase(U, hprime_o, hprime_i, RTdivF)
    potential_H_leak = P.nernst_potential_H_leak(U, hprime_o, hprime_i, RTdivF)

    # calculate flow of chloriDe (d[Cl]/dt)
    Cl_flux_asor = i_flux.J_cl_asor(potential_asor, G['asor'], U, pH_local, A)
    Cl_flux_CLC = i_flux.J_Cl_CLC(potential_CLC, G['CLC'], U, pH_local, A )
    Cl_flux_Cl_OH = i_flux.J_Cl_OH(potential_Cl_OH, G['Cl_OH'], A )

    dIons_dt[0] = Cl_flux_asor + Cl_flux_CLC + Cl_flux_Cl_OH

    # calculate flow of sodium (d[Na]/dt)
    na_flux_tpc = i_flux.J_na_tpc(n_potential_Na_TPC, G['tpc'], A)
    na_flux_nhe = i_flux.J_Na_NHE(potential_nhe, G['NHE'], A)

    dIons_dt[1] = na_flux_tpc + na_flux_nhe

    # calculate flow of H (d[H]/dt)
    H_flux_CLC = i_flux.J_H_CLC(potential_CLC, G['CLC'], U, pH_local, A)
    H_flux_NHE = i_flux.J_H_NHE(potential_nhe,G['NHE'],A)
    H_flux_Cl_OH = i_flux.J_Cl_OH(potential_Cl_OH, G['Cl_OH'], A )
    H_flux_VATPase = i_flux.J_VATPase(potential_VATPase, G['ATPase'], time_step, A)
    H_flux_leak    = i_flux.J_H_leak(potential_H_leak, G['H_leak'], A)

    dIons_dt[2] = H_flux_CLC + H_flux_NHE + H_flux_Cl_OH + H_flux_VATPase + H_flux_leak

    # calculate flow of K (d[K]/dt)
    K_flux = i_flux.J_k(potential_k, G['g_k'], A)

    dIons_dt[3] = K_flux
    
    pH_dep_ASOR= F.pH_dependence_ASOR(pH_local)
    v_dep_ASOR= F.v_dependence_ASOR(U)
    
    pH_dep_ClC = F.pH_dependence_ClC(pH_local)
    v_dep_ClC  = F.v_dependence_ClC(U)

    t_dep_VATPase = F.g_VATP_dependence(time_step)

    fluxes = {'Cl_asor': Cl_flux_asor,
            'Cl_CLC': Cl_flux_CLC,
            'Cl_Cl_OH': Cl_flux_Cl_OH,
            'Na_tpc': na_flux_tpc,
            'Na_nhe': na_flux_nhe,
            'H_CLC': H_flux_CLC,
            'H_NHE': H_flux_NHE,
            'H_Cl_OH': H_flux_Cl_OH,
            'H_VATPase': H_flux_VATPase,
            'H_leak': H_flux_leak,
            'K': K_flux
            }
    
    pH_dep_ASOR, v_dep_ASOR, pH_dep_ClC, v_dep_ClC, t_dep_VATPase,
    deps = {'pH_ASOR': pH_dep_ASOR,
            'v_ASOR': v_dep_ASOR,
            'pH_ClC': pH_dep_ClC,
            'v_ClC': v_dep_ClC,
             't_VATPase': t_dep_VATPase
             }
    
    pH_local, A, C, Buffer_T
    local_vars = {'pH_local': pH_local,
                    'A': A,
                    'C': C,
                    'Buffer_T': Buffer_T
                    }

    return dIons_dt, fluxes, deps, local_vars

def update_euler(past_state, int_step, derivative):
    """ Integrate ODE with simple Euler integration """
    return past_state + (int_step * derivative) # Euler integration i.e. x(t) = x(t-1) + (dt * dx(t)/dt)

def run_simulation(initial_state, parameters):
    """
    Run simulation
    Arguments
    ==========
    `external_ions` [1D np.ndarray]:
        - vector of initial external ionic amounts (in moles)
    `parameters` [dict]:
        - dictionary of simulation parameters, including the following key/value pairs:
            "conductances" [dict]:
                - dictionary containing conductances for the following channel types:
                    - ASOR, ClC, ...
        "buffer_capacity_t0" [float]:
            - Description
        "V_t0" [float]:
            - Description    

    Returns
    =======   
    """

    ''' Initialize variables for the simulation '''
    dt, T = parameters['dt'], parameters['T']
    time_axis = np.arange(0, T, dt)

    ''' Initialize arrays / dictionaries to store the histories of each variable-of-interest over time '''
    ions_t = np.empty((4, len(time_axis)))
    ions_t[:,0] = external_ions

    # flux_history_dictionary = {'ClC_ASOR': np.zeros(len(time_axis)-1), ''}
    # flux_history_array = np.zeros( (11, np.zeros(len(time_axis)-1)))

    for t in range(1,len(time_axis)):

        ''' Compute the flows and local variables to store at this timestep''' 
        dIons_dt, fluxes, deps, local_vars = compute_flows(time_axis[t], ions_t[t-1, :], V_t[t-1], **parameters)

        ''' update the ion amounts using the flows and store '''
        ions_t[t,:] = update_euler(ions_t[t-1,:], dt, dIons_dt)

        ''' store other relevant variables in history array '''
        # flux_history_dictionary = update_history_datastructure(flux_history, fluxes)
        # dependency_histories = update_history_datastructure(flux_history, fluxes)

        ''' update volume using the ion amounts and the initial amounts and store '''
        V[t] = (parameters['V_t0']*(ions_t[t, 0]+ions_t[t,1]+ions_t[t,3] + abs(parameters['X_amount'])))/Sum_initial_amounts

    ions_t_concen = ions_t/ (V[t] *1000)
    # ions_t_concen = ions_t / parameters['V_t0']


    ''' Package output of simulation into results dictionary / some understandable datastructure that is useful for downstream plotting/processing/etc.'''
    # results = {'external_ions': {}, 'fluxes': fluxes, 'deps': deps}

    # Option 1

    # results['external_ions'] = {'amounts': ions_t, 'concentrations': ions_t_concen}
    # results['fluxes'] = flux_history_dictionary / flux_history_array
    # results['fluxes'] = dependency_history_dictionary / dependency_history_array

    # Option 2
    # results['external_ions'] = {'Na': {'amounts': ions_t[Na_idx,:], 'concentrations': ions_t_concen[Na_idx,:]}, 
    #                             "H": {'amounts': ions_t[H_idx,:], 'concentrations': ions_t_concen[H_idx,:]}, 
    #                             "Cl": {'amounts': ions_t[Cl_idx,:], 'concentrations': ions_t_concen[Cl_idx,:]}, 
    #                             "K": {'amounts': ions_t[K_idx,:], 'concentrations': ions_t_concen[K_idx,:]}
    #                             }

    

    return results



    # ions = results['external_ions']

    # plt.plot(ions['Na']['concentrations'][:500])


