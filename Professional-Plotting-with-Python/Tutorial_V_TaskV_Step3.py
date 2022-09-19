#Task V, Step 3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

catalog = np.genfromtxt('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_V_Professional_Plotting_with_Python/data/sdss_tutorial_file_v2.csv', 
                        dtype=None, delimiter=",", names=True, encoding=None) 
good_array = [each_gal['mag_u']!=-99  for each_gal in catalog]
good_subset = catalog[good_array]

r = good_subset['mag_r']
u = good_subset['mag_u']
stellar_mass = np.log10(good_subset['stellar_mass'])

number_of_bins = 40


fig = plt.figure(figsize=(8,6))
#Step 2
hist, xbins, ybins, mesh = plt.hist2d(stellar_mass, u-r, range=[[10, 11.5], [1.2, 3.15]],
                                      bins=number_of_bins, cmap='RdBu_r',
                                      norm=LogNorm(), cmin=3, alpha=0.5)
cbar = plt.colorbar()
#Step 3
plt.contour(hist.transpose(), levels=[5,10,15,25,50,75,100], extent=[xbins.min(),
            xbins.max(), ybins.min(), ybins.max()], linewidths=2, colors='black',
            linestyles='--')
cbar.set_label('Number', fontsize = 18)
plt.xlabel('log$_{10}$[stellar mass]', fontsize=18)
plt.ylabel('(u-r) color', fontsize=18)
plt.xticks([10, 10.3, 10.6, 10.9, 11.2, 11.5], fontsize=18)
plt.yticks([1.25, 1.75, 2.25, 2.75, 3.15], fontsize=18)
#plt.savefig('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_V_Professional_Plotting_with_Python/plots/TaskIV_color_bar_contour.pdf', 
#               format='pdf', bbox_inches='tight')
plt.show()