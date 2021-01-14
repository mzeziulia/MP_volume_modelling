import numpy as np
from . import nernst_potentials as potentials
from . import ionic_fluxes as fluxes

# the following functions compute the driving forces exerted upon each ionic species
def compute_Cl_flux(U, Cl_inside, Cl_outside, Hprime_inside, Hprime_outside, g_ASOR, g_CLC, A):

    ASOR_flux = compute_ASOR_flux(U, Cl_outside, Cl_inside, g_ASOR, Hprime_inside, A)
    CLC_flux = compute_CLC_flux(U, Cl_outside, Cl_inside, g_CLC, Hprime_inside, Hprime_outside, A, ion_type = 'Cl')

    return ASOR_flux + CLC_flux

def compute_Na_flux(U, Na_outside, Na_inside, Hprime_inside, Hprime_outside, g_TPC, g_NHE, A):

    TPC_flux = compute_TPC_flux(U, Na_outside, Na_inside, g_TPC, A)
    NHE_flux = compute_NHE_flux(Na_outside, Na_inside, Hprime_inside, Hprime_outside, g_NHE, A, ion_type = 'Na')

    return TPC_flux + NHE_flux

def compute_H_flux(U, Cl_inside, Cl_outside, Hprime_inside, Hprime_outside, Na_outside, Na_inside, g_CLC, g_NHE, A):

    CLC_flux = compute_CLC_flux(U, Cl_outside, Cl_inside, g_CLC, Hprime_inside, Hprime_outside, A, ion_type = 'H')
    NHE_flux = compute_NHE_flux(Na_outside, Na_inside, Hprime_inside, Hprime_outside, g_NHE, A, ion_type = 'H')

    return CLC_flux + NHE_flux

# the following functions compute the contributions from specific channels (e.g. ASOR) to the driving forces exerted upon each ionic species

def compute_ASOR_flux(U, Cl_outside, Cl_inside, g_ASOR, Hprime_inside, A):

    ASOR_potential = potentials.Cl_ASOR(U, Cl_outside, Cl_inside)

    return fluxes.Cl_ASOR(ASOR_potential, g_ASOR, U, Hprime_inside, A)

def compute_CLC_flux(U, Cl_outside, Cl_inside, g_CLC, Hprime_inside, Hprime_outside, A, ion_type):

    CLC_potential = potentials.CLC(U, Cl_inside, Cl_outside, Hprime_inside, Hprime_outside)

    if ion_type is 'Cl':
        output = fluxes.Cl_CLC(CLC_potential, g_CLC, U, A)
    elif ion_type is 'H':
        output = fluxes.H_CLC(CLC_potential, g_CLC, U, A)
    else:
        ValueError("ion_type must be either Cl or H")

    return output 

def compute_TPC_flux(U, Na_outside, Na_inside, g_TPC, A):

    TPC_potential = potentials.Na_K(U, Na_outside, Na_inside)

    return fluxes.Na_TPC(TPC_potential, g_TPC, A)

def compute_NHE_flux(Na_outside, Na_inside, Hprime_inside, Hprime_outside, g_NHE, A, ion_type):

    NHE_potential = potentials.NHE(Na_outside, Na_inside, Hprime_inside, Hprime_outside)

    if ion_type is 'Na':
        output = fluxes.Na_NHE(NHE_potential, g_NHE, A)
    elif ion_type is 'H':
        output = fluxes.H_NHE(NHE_potential, g_NHE, A)
    else:
        ValueError("ion_type must be either Na or H")
    
    return output






