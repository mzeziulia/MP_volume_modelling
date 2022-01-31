# Mathematical model of macropinosome shrinkage repo

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

* g_ASOR
* g_TPC
* g_K (in all simulations is set to 0)
* g_CLC
* g_NHE (in all simulations is set to 0)
* g_vATPase
* g_H-leak
* ASOR pH-dependency could be chosen between wild-type (wt), pH-shifted mutant (mt) or without pH-dependency (none)
* Choice if ASOR has voltage-dependency: yes/no
* Choice if CLC has pH- or voltage-dependency: yes/no
* Initial internal Cl concentration: 'high' = 159mM, 'low' = 9mM, 'zero' = 1mM


If you are running the code from the command line, if no input was provided from a keyboard, default parameters will be used:

- g_asor = 8*10<sup>-5
- g_tpc = 2*10<sup>-6
- g_k = 0.0
- g_CLC = 10*10<sup>-8
- g_NHE = 0.0
- g_VATPase = 8*10<sup>-9
- g_H_leak = 16*10<sup>-9
- ASOR pH-dependency: wt
- ASOR voltage-dependency: yes
- CLC pH- and voltage-dependency: yes
- Initial internal Cl concentration: 'high'


If you are running the code from IPython kernel, you have to set all parameters from the keyboard. In case of g values, if the indicated value in the manuscript states 1*10<sup>-6, the window will state 10**-6, please input 1.

## List of parameters used to generate figures

### Supplementary figure 14

- a) g_CLC = 4*10<sup>-6
- b) g_ASOR = 4*10<sup>-6, g_CLC = 4*10<sup>-6
- c) g_TPC = 1*10<sup>-6, g_CLC = 4*10<sup>-6
- d) g_ASOR = 4*10<sup>-6, g_TPC = 1*10<sup>-6, g_CLC = 4*10<sup>-6
- e) g_ASOR = 4*10<sup>-6, g_TPC = 1*10<sup>-6
no pH- and voltage-dependency for ASOR and CLC
Initial ClC concentration is set to either 'high' or to 'zero'


### Supplementary figure 15

f(pH) = 1 / (1 + e<sup>(k<sub>1 * (pH - pH<sub>1/2)))
f(U) = 1 / (1 + e<sup>(k<sub>2 * (U - U<sub>1/2)))

WT ASOR pH-dependency: k<sub>1 = 3, pH<sub>1/2 = 5.4
pH-shifted mutant ASOR pH-dependency: k<sub>1 = 1, pH<sub>1/2 = 7.4
CLC pH-dependency: k<sub>1 = -1.5, pH<sub>1/2 = 5.5

ASOR and CLC voltage dependency: k<sub>2 = 80, U<sub>1/2 = -40

### Supplementary figure 16

- a) g_ASOR = 8*10<sup>-5, g_TPC = 2*10<sup>-6, g_CLC = 1*10<sup>-7, g_vATPase = 8*10<sup>-9, g_Hleak = 1.6*10<sup>-8
- b) g_TPC = 2*10<sup>-6, g_CLC = 1*10<sup>-7, g_vATPase = 8*10<sup>-9, g_Hleak = 1.6*10<sup>-8
- c) g_TPC = 2*10<sup>-6, g_CLC = 1*10<sup>-7, g_Hleak = 1.6*10<sup>-8
- d) g_TPC = 2*10<sup>-6, g_CLC = 1*10<sup>-7
- e) g_ASOR = 8*10<sup>-5, g_TPC = 2*10<sup>-6, g_vATPase = 8*10<sup>-9, g_Hleak = 1.6*10<sup>-8
- f) g_ASOR = 8*10<sup>-5, g_TPC = 2*10<sup>-6, g_CLC = 1*10<sup>-7, g_Hleak = 1.6*10<sup>-8
- g) g_ASOR = 8*10<sup>-5, g_TPC = 2*10<sup>-6, g_CLC = 1*10<sup>-7, g_vATPase = 8*10<sup>-9
- h) g_ASOR = 8*10<sup>-5, g_TPC = 2*10<sup>-6, g_CLC = 1*10<sup>-7
- i) g_ASOR = 8*10<sup>-5, g_TPC = 2*10<sup>-6, g_vATPase = 8*10<sup>-9
- j) g_ASOR = 8*10<sup>-5, g_TPC = 2*10<sup>-6, g_Hleak = 1.6*10<sup>-8
- k) g_ASOR = 8*10<sup>-5, g_TPC = 2*10<sup>-6

Wild-type pH- and voltage-dependency for ASOR and CLC
Initial ClC concentration is set to either 'high' or to 'low'

### Supplementary figure 17

a) g_ASOR = 4*10<sup>-5, g_ASOR(5x) = 2*10<sup>-4, g_TPC = 1*10<sup>-6, g_CLC = 5*10<sup>-8, g_vATPase = 4*10<sup>-9

 
