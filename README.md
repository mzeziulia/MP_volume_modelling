# Macropinosome shrinkage mathematical model paper repo

Companion repository for "Proton-gated anion transport governs endocytic vacuole shrinkage" by Mariia Zeziulia, Sandy Blin, Franziska W. Schmitt, Martin Lehmann, Thomas J. Jentsch

# Installation 

To run the Python code in this repo, we recommend building a virtual environment using `venv` and the provided `requirements.txt` file, which 
will install all of the required dependencies for you:

```
python3 -m venv my_env
source my_env/bin/activate
pip install -r requirements.txt
```

# Usage

## How to run the code

To run the code using an IPython kernel (e.g. in VSCode or Spyder or Pycharm), open up the file `ipython_run.py` in your IDE of choice and then run the code using the parameters provided in figure legends 

If you want to run this from the command line you can also specify particular parameters as additional keyword arguments using 

`python3 run.py [-KEYWORD] [VALUE]`

## Choice of parameters

Parameters that are requested and could be defined from a keyboard:
g_ASOR
g_TPC
g_K (in all simulations is set to 0)
g_CLC
g_NHE (in all simulations is set to 0)
g_vATPase
g_H-leak
ASOR pH-dependency could be chosen between wild-type (wt), pH-shifted mutant (mt) or without pH-dependency (none)
Choice if ASOR has voltage-dependency: yes/no
Choice if CLC has pH- or voltage-dependency: yes/no
Initial internal Cl concentration: 'high' = 159mM, 'low' = 9mM, 'zero' = 1mM

If you are running the code from the command line, if no input was provided from a keyboard, default parameters will be used:
g_asor = 8*10^-5
g_tpc = 2*10^-6
g_k = 0.0
g_CLC = 10*10^-8
g_NHE = 0.0
g_VATPase = 8*10^-9
g_H_leak = 16*10^-9
ASOR pH-dependency: wt
ASOR voltage-dependency: yes
CLC pH- and voltage-dependency: yes
Initial internal Cl concentration: 'high'

If you are running the code from IPython kernel, you have to set all parameters from the keyboard. In case of g values, if the indicated value in the manuscript states 1*10^-6, the window will state 10**-6, please input 1.

## List of parameters used to generate figures

### Supplementary figure 14
a) g_CLC = 4*10^-6
b) g_ASOR = 4*10^-6, g_CLC = 4*10^-6
c) g_TPC = 1*10^-6, g_CLC = 4*10^-6
d) g_ASOR = 4*10^-6, g_TPC = 1*10^-6, g_CLC = 4*10^-6
e) g_ASOR = 4*10^-6, g_TPC = 1*10^-6



