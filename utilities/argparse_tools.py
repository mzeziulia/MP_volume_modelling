import argparse



G_asor = 8*1e-5
G_tpc = 2*1e-6
G_k = 0.0
G_CLC = 10*1e-8
G_NHE = 0.0
G_VATPase = 8*1e-9
G_H_leak = 16*1e-9

def parse_user_input():
    """
    Wrapper for arg-parser used to get the input random seed and save mode
    from the user and set defaults if none is provided
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fff", help="a dummy argument to fool ipython", default="1")

    parser.add_argument('--gasor', '-as', type = float,
                help = "Conductance of ASOR channel",
                dest = "ASOR", default=G_asor)
    parser.add_argument('--gtpc', '-tpc', type = float,
                help = "Conductance of TPC channel",
                dest = "TPC", default=G_tpc)
    parser.add_argument('--gk', '-k', type = float,
                help = "Conductance of K channel",
                dest = "K", default=G_k)
    parser.add_argument('--gclc', '-cl', type = float,
                help = "Conductance of CLC channel",
                dest = "CLC", default=G_CLC)
    parser.add_argument('--gnhe', '-nhe', type = float,
                help = "Conductance of NHE channel",
                dest = "NHE", default=G_NHE)
    parser.add_argument('--gvatpase', '-atp', type = float,
                help = "Conductance of v_ATPase channel",
                dest = "vATPase", default=G_VATPase)
    parser.add_argument('--ghleak', '-hlk', type = float,
                help = "Conductance of H_leak channel",
                dest = "H_leak", default=G_H_leak)
    parser.add_argument("--wt_vs_mutant", "-wtmt", type = str,
                help = "Type of ASOR channel: wildtype (wt) vs. mutant (mt)", choices=['wt', 'mt'],
                dest = "wt_vs_mutant", default="wt")
    parser.add_argument("--Cli_concentration", "-cli", type = str,
                help = "Initial internal cloride concentration high, low, zero",
                choices = ['high', 'low', 'zero'],
                dest = "Cl_i", default="high")

    arg_dictionary = parser.parse_args()

    G = {}
    G['ASOR'] = arg_dictionary.ASOR
    G['TPC'] = arg_dictionary.TPC
    G['K'] = arg_dictionary.K
    G['CLC'] = arg_dictionary.CLC
    G['NHE'] = arg_dictionary.NHE
    G['vATPase'] = arg_dictionary.vATPase
    G['H_leak'] = arg_dictionary.H_leak

    ASOR_args = {}
    if arg_dictionary.wt_vs_mutant == 'wt':
        ASOR_args['alpha'] = 3.0
        ASOR_args['pH_offset'] = 5.4
    elif arg_dictionary.wt_vs_mutant == 'mt':
        ASOR_args['alpha'] = 1.0
        ASOR_args['pH_offset'] = 7.4

    if arg_dictionary.Cl_i == 'high':
        Cl_i_concentration = 159*1e-3
    elif arg_dictionary.Cl_i == 'low':
        Cl_i_concentration = 9*1e-3
    elif arg_dictionary.Cl_i == 'zero':
        Cl_i_concentration = 1*1e-3

    return G, ASOR_args, Cl_i_concentration
