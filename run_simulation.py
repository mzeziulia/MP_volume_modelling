import matplotlib.pyplot as plt
import numpy as np

from utilities import dep_functions as F
from utilities import ionic_fluxes as i_flux
from utilities import nernst_potentials as potentials
from plotting import display_simulation_results


number_of_ions = 4
T = 1000 # total time (in seconds)
dt = 0.001 # duration of integration window (in seconds). Making this smaller ensures more numerical stability but will take longer 
t_axis = np.arange(0,T,dt) # the time axis, expressed in seconds and advancing in increments of 'dt'

# initialise constants related to the simulation
RT = 2578.5871 # gas constant x temperature in Kelvin
F = 96485.0 # Faraday constant
RTdivF=RT/F
c_spec = 0.01  # F/(m**2)
#buffer_capacity_t0=3.0*1e-5  # very crude measure
buffer_capacity_t0=5.0*1e-4 
U0 = 40*1e-3 # membrane potential in V 

r=1.3e-6 # radius of vesicle
V0 = (4.0/3.0) * np.pi * (r**3) # m3
volume_over_time[0] = V0
A0 = 4.0 * np.pi * (r**2) # surface area of vesicle
A_from_V_const=(36.0*np.pi)**(1/3)

C0 = A0 * c_spec


results = run_simulation(T, initial_state, **parameters)

results['concentrations']['Cl']
results['volumes']['Cl']

display_simulation_results(results)
