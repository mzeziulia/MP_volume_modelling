
# %%
import numpy as np
import matplotlib.pyplot as plt
from mps_modelling import ode_tools

# %% initialise my system with desired conditions
number_of_ions=3
T = 100 # length of simulation in seconds
dt = 0.001 # duration of integration window
t_axis = np.arange(0,T,dt)
F = 96485.0 # Faraday constant

ion_concentrations_over_time = np.zeros((len(t_axis), number_of_ions)) # history of ion concentrations
ion_amounts_over_time= np.zeros((len(t_axis), number_of_ions))
volume_over_time = np.zeros(len(t_axis)) # history of volumes 

c_spec = 0.001
U0 = 40*1e-3 # membrane potential in V 
r=1.3e-6 # radius of vesicle
V0 = (4.0/3.0) * np.pi * (r**3) # m3
volume_over_time[0] = V0
A = 4.0 * np.pi * (r**2) # surface area of vesicle

C = A * c_spec

Cl_o_concentration=20*1e-3 #M
Cl_i_concentration=164*1e-3 #M
Na_o_concentration=10*1e-3 #M
Na_i_concentration=150*1e-3 #M

K_i_concentration=5*1e-3
K_i_amount=K_i_concentration*V0*1000

pH_o =  7.2
pH_i =  7.2

hprime_o_concentration = 10**(-pH_o)
hprime_i_concentration = 10**(-pH_i)

h_o_concentration = hprime_o_concentration/ (3.0*1e-5)
h_i_concentration = hprime_i_concentration/ (3.0*1e-5)

h_i_amount = h_i_concentration*V0*1000

Q0=U0*C
X_amount=(Q0/F)-((Na_i_concentration+K_i_concentration+h_i_concentration-Cl_i_concentration)*V0*1000)
#X_amount = 6.347856428029419e-17
X_concantration=X_amount/(V0*1000)

ions_i_concentration, ions_o_concentration, ions_i_amount = np.zeros(3), np.zeros(3), np.zeros(3)

ions_i_concentration[0] = Cl_i_concentration
ions_o_concentration[0] = Cl_o_concentration

ions_i_concentration[1] = Na_i_concentration
ions_o_concentration[1] = Na_o_concentration

ions_i_concentration[2] = h_i_concentration
ions_o_concentration[2] = h_o_concentration

ions_i_amount[0] = Cl_i_concentration*V0*1000
ions_i_amount[1] = Na_i_concentration*V0*1000
ions_i_amount[2] = h_i_concentration*V0*1000

Sum_amounts = ions_i_amount[0] + ions_i_amount[1] + X_amount + K_i_amount

ion_concentrations_over_time[0, :] = ions_i_concentration
ion_amounts_over_time[0, :] = ions_i_amount

conductances = np.zeros(5)

#G_asor, G_tpc, G_k, G_CLC, G_NHE = (0, 1*1e-10, 0, 0, 0) # JUST TPC
#G_asor, G_tpc, G_k, G_CLC, G_NHE = (0, 0, 0, 0, 1*1e-7) # JUST NHE
#G_asor, G_tpc, G_k, G_CLC, G_NHE = (1*1e-7, 0, 0, 0, 0) # JUST ASOR
#G_asor, G_tpc, G_k, G_CLC, G_NHE = (0, 0, 0, 1*1e-8, 0) # JUST CLC

G_asor, G_tpc, G_k, G_CLC, G_NHE = (1*1e-6, 1*1e-6, 0, 1*1e-6, 1*1e-6) #ALL
#G_asor, G_tpc, G_k, G_CLC, G_NHE = (0, 1*1e-6, 0, 1*1e-6, 1*1e-6) #ASOR KO

conductances[0] = G_asor
conductances[1] = G_tpc
conductances[2] = G_k
conductances[3] = G_CLC
conductances[4] = G_NHE

ion_amounts_over_time, volume_over_time = ode_tools.integrate_system(ions_i_amount, ions_o_concentration, conductances, A, C, X_amount, K_i_amount, r, t_axis)


ion_concentrations_over_time = ion_amounts_over_time / (volume_over_time *1000).reshape(-1,1)

pH_over_time=np.zeros(len(ion_concentrations_over_time))
for i in range(len(ion_concentrations_over_time)):
    pH_over_time[i]=-np.log10(ion_concentrations_over_time[i, 2]*(3.0*1e-5))

U_over_time=np.zeros(len(ion_amounts_over_time))
for i in range(len(ion_amounts_over_time)):
    Q2 = (ion_amounts_over_time[i,1] +K_i_amount + ion_amounts_over_time[i,2] - ion_amounts_over_time[i,0] + X_amount) * F
    U_over_time[i] = Q2 / C 


# %% Plotting
fig,axes = plt.subplots(3,3, figsize = (15,15), sharex = True)

axes[0,0].plot(t_axis,ion_concentrations_over_time[:,0])
axes[0,0].set_title('Cloride concentration')
axes[0,1].plot(t_axis,ion_concentrations_over_time[:,1])
axes[0,1].set_title('Sodium concentration')
axes[0,2].plot(t_axis,ion_concentrations_over_time[:,2])
axes[0,2].set_title('Hydrogen concentration')
axes[1,0].plot(t_axis,ion_amounts_over_time[:,0])
axes[1,0].set_title('Cloride amounts')
axes[1,1].plot(t_axis,ion_amounts_over_time[:,1])
axes[1,1].set_title('Sodium amounts')
axes[1,2].plot(t_axis,ion_amounts_over_time[:,2])
axes[1,2].set_title('Hydrogen amounts')
axes[2,0].plot(t_axis,pH_over_time)
axes[2,0].set_title('pH')
axes[2,1].plot(t_axis,volume_over_time)
axes[2,1].set_title('Volume')
axes[2,2].plot(t_axis,U_over_time)
axes[2,2].set_title('Membrane potential')
plt.subplots_adjust(wspace=None, hspace=None)

# for ax in fig.get_axes():
#     ax.label_outer()

# %% Plotting

plt.plot(t_axis,ion_concentrations_over_time[:,0],label='Cloride concentration')
plt.legend()
plt.show()

plt.plot(t_axis,ion_concentrations_over_time[:,1],label='Sodium concentration')
plt.legend()
plt.show()

plt.plot(t_axis,ion_concentrations_over_time[:,2],label='Hydrogen concentration')
plt.legend()
plt.show()

plt.plot(t_axis,ion_amounts_over_time[:,0],label='Cloride amounts')
plt.legend()
plt.show()

plt.plot(t_axis,ion_amounts_over_time[:,1],label='Sodium amounts')
plt.legend()
plt.show()

plt.plot(t_axis,ion_amounts_over_time[:,2],label='Hydrogen amounts')
plt.legend()
plt.show()

plt.plot(t_axis,pH_over_time,label='pH')
plt.legend()
plt.show() 

plt.plot(t_axis,volume_over_time, label='Volume')
plt.legend()
plt.show()

plt.plot(t_axis,U_over_time,label='Membrane potential')
#plt.ylim(0.02, 0.06)
plt.legend()
plt.show()
