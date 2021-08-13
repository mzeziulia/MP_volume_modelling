

# mapping of chemicals to numerical indices used to index the state vectors
Cl_idx = 0
Na_idx = 1
H_idx = 2
K_idx = 3

number_of_ions = 4
T = 1000 # total time (in seconds)
dt = 0.001 # duration of integration window (in seconds). Making this smaller ensures more numerical stability but will take longer 

# initialise constants related to the simulation
RT = 2578.5871 # gas constant x temperature in Kelvin
F = 96485.0 # Faraday constant
c_spec = 0.01  # F/(m**2)
#buffer_capacity_t0=3.0*1e-5  # very crude measure
buffer_capacity_t0=5.0*1e-4 
U0 = 40*1e-3 # membrane potential in V 

r=1.3e-6 # radius of vesicle
V0 = (4.0/3.0) * np.pi * (r**3) # m3
A0 = 4.0 * np.pi * (r**2) # surface area of vesicle
A_from_V_const=(36.0*np.pi)**(1/3)

C0 = A0 * c_spec

G = {'ASOR': 1.0, 'ClC': 2.0 , 'Na_ASOR': 3.0 }

