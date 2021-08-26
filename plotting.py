#%% SM5 low/high Cl figures

import matplotlib 
new_rc_params = {'text.usetex': False, "svg.fonttype": 'none'}
matplotlib.rcParams.update(new_rc_params)
#ax.set_xticklabels(fontsize = 10, rotation = 0)
t_axis2=np.arange(0,T-dt,dt)
fig,axes = plt.subplots(1,3, figsize = (15, 5), sharex = True)
plt.subplots_adjust(wspace=0.55, hspace=0.6)
matplotlib.rcParams['font.sans-serif'] = "Arial"
matplotlib.rcParams['font.family'] = "Arial"

# axes[0].plot(t_axis,pH_over_time,color=u'#348ABD', linewidth=0.6)
axes[0].plot(t_axis,pH_over_time,color=u'#E24A33', linewidth=0.6)
axes[0].set_title('pH', fontsize=20, pad=20)
axes[0].set_ylim(5.0,7.5)
axes[0].set_xlim(0,1000)
axes[0].spines['right'].set_visible(False)
axes[0].spines['top'].set_visible(False)
axes[0].spines['bottom'].set_linewidth(0.4)
axes[0].spines['left'].set_linewidth(0.4)
axes[0].spines['left'].set_position(('outward', 5))
axes[0].tick_params(axis='both', which='major', labelsize=16, width=0.1)
axes[0].set_ylabel('pH', fontname="Arial", fontsize =24)
axes[0].set_xlabel('Time, s', fontname="Arial", fontsize =24)

# axes[1].plot(t_axis,volume_over_time*1e18, color=u'#348ABD', linewidth=0.6)
axes[1].plot(t_axis,volume_over_time*1e18, color=u'#E24A33', linewidth=0.6)
axes[1].set_title('Volume', fontsize=20, pad=20)
axes[1].set_ylim(1,10)
axes[1].set_xlim(0,1000)
axes[1].spines['right'].set_visible(False)
axes[1].spines['top'].set_visible(False)
axes[1].spines['bottom'].set_linewidth(0.4)
axes[1].spines['left'].set_linewidth(0.4)
axes[1].spines['left'].set_position(('outward', 5))
axes[1].tick_params(axis='both', which='major', labelsize=16, width=0.1)
axes[1].set_ylabel(' $\mathregular{µm^3}$', fontname="Arial", fontsize =24)
axes[1].set_xlabel('Time, s', fontname="Arial", fontsize =24)


# axes[2].plot(t_axis,U_over_time*1000, color=u'#348ABD', linewidth=0.6)
axes[2].plot(t_axis,U_over_time*1000, color=u'#E24A33', linewidth=0.6)
axes[2].set_title('Membrane potential', fontsize=20, pad=20)
axes[2].set_ylim(-80,40)
axes[2].set_xlim(0,1000)
axes[2].spines['right'].set_visible(False)
axes[2].spines['top'].set_visible(False)
axes[2].spines['bottom'].set_linewidth(0.4)
axes[2].spines['left'].set_linewidth(0.4)
axes[2].spines['left'].set_position(('outward', 5))
axes[2].tick_params(axis='both', which='major', labelsize=16, width=0.1)
axes[2].set_ylabel('mV', fontname="Arial", fontsize =24)
axes[2].set_xlabel('Time, s', fontname="Arial", fontsize =24)

# plt.legend(['9 mM Cl$^{-}$'], loc=0, bbox_to_anchor=(0, 0.1, 0.5, 0.5), fontsize=20, frameon=False)

# plt.savefig(os.path.join('SM5a ASOR+TPC+ClC+H-ATPase+H-leak high Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5a ASOR+TPC+ClC+H-ATPase+H-leak low Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5b TPC+ClC+H-ATPase+H-leak high Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5b TPC+ClC+H-ATPase+H-leak low Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5c TPC+ClC+H-leak high Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5c TPC+ClC+H-leak low Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5j ASOR+TPC+H-leak high Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5j ASOR+TPC+H-leak low Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5h ASOR+TPC+CLC high Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5h ASOR+TPC+CLC low Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5d TPC+CLC high Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5d TPC+CLC low Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5g ASOR+TPC+CLC+H-ATPase high Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5g ASOR+TPC+CLC+H-ATPase low Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5i ASOR+TPC+H-ATPase high Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5i ASOR+TPC+H-ATPase low Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5e ASOR+TPC+H-ATPase+H-leak high Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5e ASOR+TPC+H-ATPase+H-leak low Cl.svg'), transparent=True)
# plt.savefig(os.path.join('SM5f ASOR+TPC+ClC+H-leak high Cl.svg'), transparent=True)
plt.savefig(os.path.join('SM5f ASOR+TPC+ClC+H-leak low Cl.svg'), transparent=True)

# plt.savefig(os.path.join('SM2 ASOR+TPC+H-ATPase.svg'), transparent=True)






























#%% SM5 fluxes

import matplotlib 
new_rc_params = {'text.usetex': False, "svg.fonttype": 'none'}
matplotlib.rcParams.update(new_rc_params)
#ax.set_xticklabels(fontsize = 10, rotation = 0)
t_axis2=np.arange(0,T-dt,dt)
fig,axes = plt.subplots(2,3, figsize = (15, 10), sharex = False)
plt.subplots_adjust(wspace=0.55, hspace=0.5)
matplotlib.rcParams['font.sans-serif'] = "Arial"
matplotlib.rcParams['font.family'] = "Arial"

# axes[0,0].plot(t_axis2,Cl_FLUX_asor*1e18, color=u'#348ABD', linewidth=0.6)
axes[0,0].plot(t_axis2,Cl_FLUX_asor*1e18, color=u'#E24A33', linewidth=0.6)
axes[0,0].set_title('Cl$^{-}$ flux through ASOR', fontsize=20)
axes[0,0].set_ylim(-2,0.1)
axes[0,0].set_xlim(0,T)
axes[0,0].spines['right'].set_visible(False)
axes[0,0].spines['top'].set_visible(False)
axes[0,0].spines['bottom'].set_linewidth(0.4)
axes[0,0].spines['left'].set_linewidth(0.4)
axes[0,0].spines['left'].set_position(('outward', 5))
axes[0,0].tick_params(axis='both', which='major', labelsize=16, width=0.1)
axes[0,0].set_ylabel('mol*s$^{-1}$, $10^{-18}$', fontname="Arial", fontsize =24)
axes[0,0].set_xlabel('Time, s', fontname="Arial", fontsize =24)

# axes[0,1].plot(t_axis2,Cl_FLUX_CLC*1e19, color=u'#348ABD', linewidth=0.6)
axes[0,1].plot(t_axis2,Cl_FLUX_CLC*1e19, color=u'#E24A33', linewidth=0.6)
axes[0,1].set_title('Cl$^{-}$ flux through CLC', fontsize=20)
axes[0,1].set_ylim(-3.5,0.1)
axes[0,1].set_xlim(0,T)
axes[0,1].spines['right'].set_visible(False)
axes[0,1].spines['top'].set_visible(False)
axes[0,1].spines['bottom'].set_linewidth(0.4)
axes[0,1].spines['left'].set_linewidth(0.4)
axes[0,1].spines['left'].set_position(('outward', 5))
axes[0,1].tick_params(axis='both', which='major', labelsize=16, width=0.1)
axes[0,1].set_ylabel('mol*s$^{-1}$, $10^{-19}$', fontname="Arial", fontsize =24)
axes[0,1].set_xlabel('Time, s', fontname="Arial", fontsize =24)

# axes[0,2].plot(t_axis2,H_FLUX_CLC*1e19, color=u'#348ABD', linewidth=0.6)
axes[0,2].plot(t_axis2,H_FLUX_CLC*1e19, color=u'#E24A33', linewidth=0.6)
axes[0,2].set_title('H$^{+}$ flux through CLC', fontsize=20)
axes[0,2].set_ylim(-0.1,1.5)
axes[0,2].set_xlim(0,T)
axes[0,2].spines['right'].set_visible(False)
axes[0,2].spines['top'].set_visible(False)
axes[0,2].spines['bottom'].set_linewidth(0.4)
axes[0,2].spines['left'].set_linewidth(0.4)
axes[0,2].spines['left'].set_position(('outward', 5))
axes[0,2].tick_params(axis='both', which='major', labelsize=16, width=0.1)
axes[0,2].set_ylabel('mol*s$^{-1}$, $10^{-19}$', fontname="Arial", fontsize =24)
axes[0,2].set_xlabel('Time, s', fontname="Arial", fontsize =24)

# axes[1,0].plot(t_axis2,na_FLUX_tpc*1e18, color=u'#348ABD', linewidth=0.6)
axes[1,0].plot(t_axis2,na_FLUX_tpc*1e18, color=u'#E24A33', linewidth=0.6)
axes[1,0].set_title('Na$^{+}$ flux through TPC', fontsize=20)
axes[1,0].set_ylim(-5,0)
axes[1,0].set_xlim(0,T)
axes[1,0].spines['right'].set_visible(False)
axes[1,0].spines['top'].set_visible(False)
axes[1,0].spines['bottom'].set_linewidth(0.4)
axes[1,0].spines['left'].set_linewidth(0.4)
axes[1,0].spines['left'].set_position(('outward', 5))
axes[1,0].tick_params(axis='both', which='major', labelsize=16, width=0.1)
axes[1,0].set_ylabel('mol*s$^{-1}$, $10^{-18}$', fontname="Arial", fontsize =24)
axes[1,0].set_xlabel('Time, s', fontname="Arial", fontsize =24)


# axes[1,1].plot(t_axis2,H_FLUX_VATPase*1e20, color=u'#348ABD', linewidth=0.6)
axes[1,1].plot(t_axis2,H_FLUX_VATPase*1e20, color=u'#E24A33', linewidth=0.6)
axes[1,1].set_title('H$^{+}$ flux through V-ATPase', fontsize=20, pad=20)
axes[1,1].set_ylim(-0.1,3)
axes[1,1].set_xlim(0,1000)
axes[1,1].spines['right'].set_visible(False)
axes[1,1].spines['top'].set_visible(False)
axes[1,1].spines['bottom'].set_linewidth(0.4)
axes[1,1].spines['left'].set_linewidth(0.4)
axes[1,1].spines['left'].set_position(('outward', 5))
axes[1,1].tick_params(axis='both', which='major', labelsize=16, width=0.1)
axes[1,1].set_ylabel('mol*s$^{-1}$, $10^{-20}$', fontname="Arial", fontsize =24)
axes[1,1].set_xlabel('Time, s', fontname="Arial", fontsize =24)


# axes[1,2].plot(t_axis2,H_FLUX_leak*1e20, color=u'#348ABD', linewidth=0.6)
axes[1,2].plot(t_axis2,H_FLUX_leak*1e20, color=u'#E24A33', linewidth=0.6)
axes[1,2].set_title('H$^{+}$ flux through H-leak', fontsize=20, pad=20)
axes[1,2].set_ylim(-2,3)
axes[1,2].set_xlim(0,1000)
axes[1,2].spines['right'].set_visible(False)
axes[1,2].spines['top'].set_visible(False)
axes[1,2].spines['bottom'].set_linewidth(0.4)
axes[1,2].spines['left'].set_linewidth(0.4)
axes[1,2].spines['left'].set_position(('outward', 5))
axes[1,2].tick_params(axis='both', which='major', labelsize=16, width=0.1)
axes[1,2].set_ylabel('mol*s$^{-1}$, $10^{-20}$', fontname="Arial", fontsize =24)
axes[1,2].set_xlabel('Time, s', fontname="Arial", fontsize =24)

# plt.legend(['159 mM Cl$^{-}$'], loc=0, bbox_to_anchor=(0, 0.1, 0.5, 0.5), fontsize=20, frameon=False)

# plt.savefig(os.path.join('SM5a ASOR+TPC+ClC+H-ATPase+H-leak high Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5a ASOR+TPC+ClC+H-ATPase+H-leak low Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5b TPC+ClC+H-ATPase+H-leak high Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5b TPC+ClC+H-ATPase+H-leak low Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5c TPC+ClC+H-leak high Cl fluxes.svg'), transparent=True)
plt.savefig(os.path.join('SM5c TPC+ClC+H-leak low Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5j ASOR+TPC+H-leak high Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5j ASOR+TPC+H-leak low Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5h ASOR+TPC+ClC high Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5h ASOR+TPC+ClC low Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5d TPC+ClC high Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5d TPC+ClC low Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5g ASOR+TPC+ClC+H-ATPase high Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5g ASOR+TPC+ClC+H-ATPase low Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5i ASOR+TPC+H-ATPase high Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5i ASOR+TPC+H-ATPase low Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5e ASOR+TPC+H-ATPase+H-leak high Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5e ASOR+TPC+H-ATPase+H-leak low Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5f ASOR+TPC+ClC+H-leak high Cl fluxes.svg'), transparent=True)
# plt.savefig(os.path.join('SM5f ASOR+TPC+ClC+H-leak low Cl fluxes.svg'), transparent=True)
