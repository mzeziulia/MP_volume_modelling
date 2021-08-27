from config import dt, T, A_from_V_const, buffer_capacity_t0, V0, c_spec, pH_i, U0, A0, C0, initialize_internal_concentrations
import matplotlib.pyplot as plt
import numpy as np
import plotting as plot
import plot_functional_dependences as plot_dep

from utilities import simulation_tools as simtools

# G = {}
# G['ASOR'] = float(input('G_ASOR'))
# G['TPC'] = float(input('G_TPC'))
# G['K'] = float(input('G_K'))
# G['CLC'] = float(input('G_CLC'))
# G['NHE'] = float(input('G_NHE'))
# G['vATPase'] = float(input('G_vATPase'))
# G['H_leak'] = float(input('G_H_leak'))

G = {}
G['ASOR'] = float(input('G_ASOR 10**(-5)'))*1e-5
G['TPC'] = float(input('G_TPC 10**(-6)'))*1e-6
G['K'] = float(input('G_K'))
G['CLC'] = float(input('G_CLC 10**(-8)'))*1e-8
G['NHE'] = float(input('G_NHE'))
G['vATPase'] = float(input('G_vATPase 10**(-9)'))*1e-9
G['H_leak'] = float(input('G_H_leak 10**(-9)'))*1e-9


ASOR_args = {}
choice_dep_fuct = input ('ASOR pH-dependency: WT (wt) or pH-shifted mutant (mt)')
if choice_dep_fuct == 'wt':
    ASOR_args['alpha'] = 3.0
    ASOR_args['pH_offset'] = 5.4
elif choice_dep_fuct == 'mt':
    ASOR_args['alpha'] = 1.0
    ASOR_args['pH_offset'] = 7.4

choice_Cl_conc = input ('Initial internal Cl concentration: high, low or zero')
if choice_Cl_conc == 'high':
    Cl_i_concentration = 159*1e-3
elif choice_Cl_conc == 'low':
    Cl_i_concentration = 9*1e-3
elif choice_Cl_conc == 'zero':
    Cl_i_concentration = 1*1e-3


X_amount, external_ions_concentrations, internal_ions_amounts, internal_ions_concentrations, Sum_initial_amounts = initialize_internal_concentrations(Cl_i_concentration)

parameters = {
    'dt': dt,
    'T': T,
    'G': G,
    'external_ions_concentrations': external_ions_concentrations,
    'A_from_V_const': A_from_V_const,
    'X_amount': X_amount,
    'buffer_capacity_t0': buffer_capacity_t0, 
    'V_t0': V0, 
    'c_spec': c_spec, 
    'RT': 2578.5871, 
    'F': 96485.0,
    'pH_i': pH_i,
    'U0': U0,
    'A0': A0,
    'C0': C0,
    'Sum_initial_amounts': Sum_initial_amounts,
    'alpha': ASOR_args['alpha'],
    'pH_offset': ASOR_args['pH_offset']
   }


results = simtools.run_simulation(internal_ions_amounts, parameters) # I removed ** in front of parameters

figure = plot.figure_plottting(results)
figure_dependency = plot_dep.plot_dependency()

# results['concentrations']['Cl']
# results['volumes']['Cl']

# display_simulation_results(results)
