import numpy as np
from . import wrapper_funcs as wf

RT = 2477.572 # gas constant x temperature in K
F = 96485.0 # Faraday's constant
acid_conv_constant = 3*1e-5

def compute_flows(ions_inside, ions_outside_concentration, g, V_t, A, C, X_amount, K_i_amount):

    num_ionic_species = ions_inside.shape[0] # number of ions we're updating

    dIons_dt = np.zeros(num_ionic_species) # vector for storing the flows for each ionic species

    # unpack the amounts (resp. concentrations) of each ionic species, both internally and externally
    cl_i_amount, cl_o = ions_inside[0], ions_outside_concentration[0]
    na_i_amount, na_o = ions_inside[1], ions_outside_concentration[1]
    h_i_amount, h_o = ions_inside[2], ions_outside_concentration[2]

    Q = (na_i_amount + K_i_amount + h_i_amount - cl_i_amount + X_amount) * F # compute charge (in ?)
    U = Q / C # compute membrane potential (in V)

    # convert from amounts to concentrations for the different ionic species
    cl_i = cl_i_amount/(V_t*1000.0)
    na_i = na_i_amount/(V_t*1000.0)
    h_i = h_i_amount / (V_t*1000.0) 
    hprime_i = h_i * acid_conv_constant # convert from inside hydrogen concentration to acidity / pH
    hprime_o = h_o * acid_conv_constant # convert from outside hydrogen concentration to acidity / pH
    
    # unpack the conductances for the various channels
    g_ASOR, g_TPC, g_K, g_CLC, g_NHE = g[0], g[1], g[2], g[3], g[4]

    # compute the flows for the different ionic species
    dIons_dt[0] = wf.compute_Cl_flux(U, cl_i, cl_o, hprime_i, hprime_o, g_ASOR, g_CLC, A)
    dIons_dt[1] = wf.compute_Na_flux(U, na_o, na_i, hprime_i, hprime_o, g_TPC, g_NHE, A)
    dIons_dt[2] = wf.compute_H_flux(U, cl_i, cl_o, hprime_i, hprime_o, na_o, na_i, g_CLC, g_NHE, A)

    return dIons_dt

def integrate_system(ions_inside_init, ions_outside_concentration, g, A, C, X_amount, K_i_amount, r_vesicle, t_axis):

    num_ionic_species = ions_inside_init.shape[0]
    ions_over_time = np.zeros( (len(t_axis), num_ionic_species) )
    ions_over_time[0,:] = ions_inside_init

    V_t = np.zeros(len(t_axis)) # history of volumes 

    V0 = (4.0/3.0) * np.pi * (r_vesicle**3) # m3
    V_t[0] = V0

    initial_total_amount = ions_inside_init[0] + ions_inside_init[1] + X_amount + K_i_amount

    dt = t_axis[1] - t_axis[0] # integrate step size

    # integrate the system of equations
    for t in range(1,len(t_axis)):

        dIons_dt = compute_flows(ions_over_time[t-1,:], ions_outside_concentration, g, V_t[t-1], A, C, X_amount, K_i_amount) # get the derivative (flow)

        ions_over_time[t, :] = ions_over_time[t-1, :] + (dt * dIons_dt) # Euler integration i.e. x(t) = x(t-1) + (dt * dx(t)/dt)

        cl_i_amount, na_i_amount = ions_over_time[t, 0], ions_over_time[t, 1] # extract the ionic amounts you just updated 
        V_t[t] = (V0*(cl_i_amount+na_i_amount+K_i_amount+X_amount)) / initial_total_amount # use them to update the volume of the vesicle at time t
    
    #ions_over_time_C = ions_over_time/ (V_t[t] *1000)

    #return ions_over_time, V_t, ions_over_time_C
    return ions_over_time, V_t

def integrate_system_RK(ions_inside_init, ions_outside_concentration, g, A, C, X_amount, K_i_amount, r_vesicle, t_axis):

    num_ionic_species = ions_inside_init.shape[0]
    ions_over_time = np.zeros( (len(t_axis), num_ionic_species) )
    ions_over_time[0,:] = ions_inside_init

    V_t = np.zeros(len(t_axis)) # history of volumes 

    V0 = (4.0/3.0) * np.pi * (r_vesicle**3) # m3
    V_t[0] = V0

    initial_total_amount = ions_inside_init[0] + ions_inside_init[1] + X_amount + K_i_amount

    dt = t_axis[1] - t_axis[0] # integrate step size

    # integrate the system of equations
    for t in range(1,len(t_axis)):

        dIons_dt = compute_flows(ions_over_time[t-1,:], ions_outside_concentration, g, V_t[t-1], A, C, X_amount, K_i_amount) # get the derivative (flow)
        
        k1 = dIons_dt*t_axis[t]

        dIons_dt2 = compute_flows((ions_over_time[t-1,:]+(dt*(k1/2))), ions_outside_concentration, g, V_t[t-1], A, C, X_amount, K_i_amount) # get the derivative (flow)

        k2 = dIons_dt2*(t_axis[t]+dt/2)
        
        dIons_dt3 = compute_flows((ions_over_time[t-1,:]+(dt*(k2/2))), ions_outside_concentration, g, V_t[t-1], A, C, X_amount, K_i_amount) # get the derivative (flow)
        
        k3 = dIons_dt3*(t_axis[t]+dt/2)

        dIons_dt4 = compute_flows((ions_over_time[t-1,:]+(dt*k3)), ions_outside_concentration, g, V_t[t-1], A, C, X_amount, K_i_amount) # get the derivative (flow)

        k4 = dIons_dt4*(t_axis[t]+dt)

        ions_over_time[t, :] = ions_over_time[t-1, :] + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) 
        cl_i_amount, na_i_amount = ions_over_time[t, 0], ions_over_time[t, 1] # extract the ionic amounts you just updated 
        V_t[t] = (V0*(cl_i_amount+na_i_amount+K_i_amount+X_amount)) / initial_total_amount # use them to update the volume of the vesicle at time t
    
    #ions_over_time_C = ions_over_time/ (V_t[t] *1000)

    #return ions_over_time, V_t, ions_over_time_C
    return ions_over_time, V_t








