import matplotlib.pyplot as plt
import numpy as np

from utilities import dep_functions as F
from utilities import ionic_fluxes as i_flux
from utilities import nernst_potentials as potentials
from utilities import simulation_tools as simtools
from plotting import display_simulation_results



user_inputs = parse_user_inputs()

G['ASOR'] = user_input['g_ASOR']




results = simtools.run_simulation(T, initial_state, **parameters)

results['concentrations']['Cl']
results['volumes']['Cl']

display_simulation_results(results)
