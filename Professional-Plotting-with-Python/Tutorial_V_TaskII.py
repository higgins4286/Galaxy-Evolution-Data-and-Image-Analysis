#Task II
import numpy as np
import matplotlib.pyplot as plt

catalog = np.genfromtxt('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_V_Professional_Plotting_with_Python/data/sdss_tutorial_file_v2.csv', 
                        dtype=None, delimiter=",", names=True, encoding=None) 

#Step 1. Good Subsets for all, ETG, and LTG
etg_array = [each_gal['mag_u']!=-99 and 'ETG' in each_gal['Type'] for each_gal in catalog]
etg_subset = catalog[etg_array]
ltg_array = [each_gal['mag_u']!=-99 and 'LTG' in each_gal['Type'] or 'SpDisk' in each_gal['Type'] for each_gal in catalog]
ltg_subset = catalog[ltg_array]

fig, axs = plt.subplots( nrows=1, ncols=2, figsize=[18,8] )
ax1, ax2 = axs

ax1.plot(np.log10(etg_subset['stellar_mass']), etg_subset['mag_u']-etg_subset['mag_r'], marker='o',
         markersize=3, color='red', linestyle='None', alpha=0.2, label='ETGs')
ax1.plot(np.log10(ltg_subset['stellar_mass']), ltg_subset['mag_u']-ltg_subset['mag_r'], marker='o',
         markersize=3, color='blue', linestyle='None', alpha=0.2, label='LTGs')

ax1.set_xlim([9.9, 11.5])
ax1.set_ylim([1.2, 3.15])
ax1.set_yticks([1.25, 1.75, 2.25, 2.75, 3.15])
ax1.set_yticklabels([1.25, 1.75, 2.25, 2.75, 3.15], fontsize=18)
ax1.set_xticks([10, 10.3, 10.6, 10.9, 11.2, 11.5])
ax1.set_xticklabels([10, 10.3, 10.6, 10.9, 11.2, 11.5], fontsize=18)
ax1.set_xlabel('log$_{10}$[Stellar Mass]', fontsize=18)
ax1.set_ylabel('(u-r) color', fontsize=18)

ax2.plot(etg_subset['mag_r']-etg_subset['mag_z'], etg_subset['mag_u']-etg_subset['mag_r'], marker='o',
         markersize=3, color='red', linestyle='None', alpha=0.2, label='ETGs')
ax2.plot(ltg_subset['mag_r']-ltg_subset['mag_z'], ltg_subset['mag_u']-ltg_subset['mag_r'], marker='o',
         markersize=3, color='blue', linestyle='None', alpha=0.2, label='ETGs')

ax2.set_xlim([0.2, 1])
ax2.set_ylim([1.2, 3.15])
ax2.set_yticks([1.25, 1.75, 2.25, 2.75, 3.15])
ax2.set_yticklabels([1.25, 1.75, 2.25, 2.75, 3.15], fontsize=18)
ax2.set_xticks([0.2, 0.4, 0.6, 0.8, 1])
ax2.set_xticklabels([0.2, 0.4, 0.6, 0.8, 1], fontsize=18)
ax2.set_xlabel('(r-z) color', fontsize=18)
ax2.set_ylabel('(u-r) color', fontsize=18)
plt.tight_layout()
#plt.savefig('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_V_Professional_Plotting_with_Python/plots/TaskII_double_panel.pdf', 
             #format='pdf', bbox_inches='tight')
plt.show()