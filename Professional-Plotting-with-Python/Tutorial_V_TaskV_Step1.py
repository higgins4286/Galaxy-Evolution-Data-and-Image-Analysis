#Task V

#Step 1
#Plot two panel plot with u-r vs. r-z with log10(sigma) on the left
#                         log10(sigma) vs log10(stellar_mass) and best fit on the right

import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting

catalog = np.genfromtxt('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_V_Professional_Plotting_with_Python/data/sdss_tutorial_file_v2.csv', 
                        dtype=None, delimiter=",", names=True, encoding=None) 

#Step 1. Good Subsets for all, ETG, and LTG
etg_array = ['ETG' in each_gal['Type'] and np.log10(each_gal['stellar_mass']) > 10.5 and each_gal['veldisp']!=-99
                    for each_gal in catalog]
etg_subset = catalog[etg_array]
good_array = [each_gal['mag_u']!=-99  for each_gal in catalog]
good_subset = catalog[good_array]

r = good_subset['mag_r']
z = good_subset['mag_z']
u = good_subset['mag_u']
mass = np.log10(etg_subset['stellar_mass'])
veld = np.log10(etg_subset['veldisp'])
veldg = np.log10(good_subset['veldisp'])

#The error in this case is not due to poission. The error values are listed in the .cvs file.
vld_error = 0.434 * etg_subset['veldisp_err']/etg_subset['veldisp']

#Creating the weights
linear_initial = models.Linear1D(slope=1, intercept=0)
fit = fitting.LevMarLSQFitter()
inv_sig_etgv = 1.0/vld_error
fitted_model_weights_etgs = fit(linear_initial, mass, veld, weights=inv_sig_etgv)

#Calling the slope and intercept
A = fitted_model_weights_etgs.slope.value
B = fitted_model_weights_etgs.intercept.value

fig, axs = plt.subplots( nrows=1, ncols=2, figsize=[18,8] )
ax1, ax2 = axs

c = ax1.scatter(r-z, u-r, s=5, c=veldg, cmap='RdBu_r', vmin=1.5, vmax=2.6)
cbar = plt.colorbar(c, ax=ax1)
cbar.set_label('log$_{10}$[$\sigma$ [km/s]]', fontsize = 18)
ax1.set_xlim([0.2, 1])
ax1.set_ylim([1.2, 3.15])
ax1.set_yticks([1.25, 1.75, 2.25, 2.75, 3.15])
ax1.set_yticklabels([1.25, 1.75, 2.25, 2.75, 3.15], fontsize=18)
ax1.set_xticks([0.2, 0.4, 0.6, 0.8, 1])
ax1.set_xticklabels([0.2, 0.4, 0.6, 0.8, 1], fontsize=18)
ax1.set_xlabel('(r-z) color', fontsize=18)
ax1.set_ylabel('(u-r) color', fontsize=18)

#ax2
x_values_for_plotting = [10.45, 10.5, 10.8, 11.1, 11.3, 11.5]
y_values_etgs = fitted_model_weights_etgs(x_values_for_plotting)
ax2.plot(x_values_for_plotting, y_values_etgs, 'r--', linewidth=1, label="ETGs best-fit")

#Code for printing A and B
plt.text(0.75, 0.3, 'A = %s \nB = %s' % (round(A,2), round(B,2)), color='red', 
         fontsize=12, transform=plt.gca().transAxes)

ax2.errorbar(mass, veld, vld_error, marker='o', capsize=None, ecolor='black', markersize=2, markerfacecolor='black',
                    linestyle='None', alpha=0.3, label='Massive ETG Galaxies', mec='black', mfcalt='black')
ax2.set_xlim([10.45, 11.5])
ax2.set_ylim([1.9, 2.7])
ax2.set_yticks([1.9, 2.1, 2.3, 2.5, 2.7])
ax2.set_yticklabels([1.9, 2.1, 2.3, 2.5, 2.7], fontsize=18)
ax2.set_xticks([10.5, 10.8, 11.1, 11.3, 11.5])
ax2.set_xticklabels([10.5, 10.8, 11.1, 11.3, 11.5], fontsize=14)
ax2.set_xlabel('log$_{10}$[Stellar Mass]', fontsize=18)
ax2.set_ylabel('(u-r) color', fontsize=18)
ax2.legend(loc=2, fontsize=14)

plt.tight_layout()
#plt.savefig('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_V_Professional_Plotting_with_Python/plots/TaskV_double_panel.pdf', 
#             format='pdf', bbox_inches='tight')
plt.show()
