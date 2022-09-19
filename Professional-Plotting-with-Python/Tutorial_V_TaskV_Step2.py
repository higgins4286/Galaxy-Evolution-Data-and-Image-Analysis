#Task 5, Step 2

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

#Step 2
catalog = np.genfromtxt('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_V_Professional_Plotting_with_Python/data/sdss_tutorial_file_v2.csv', 
                        dtype=None, delimiter=",", names=True, encoding=None) 
good_array = [each_gal['mag_u']!=-99 for each_gal in catalog]
good_subset = catalog[good_array]

r = good_subset['mag_r']
u = good_subset['mag_u']
stellar_mass = np.log10(good_subset['stellar_mass'])

#Step 3
number_of_bins = 40

fig = plt.figure(figsize=(8,6))
plt.hist2d(stellar_mass, u-r, range=[[10, 11.5], [1.2, 3.15]], bins=number_of_bins, cmap='gray', 
           norm=LogNorm(), cmin=3)
cbar = plt.colorbar()
cbar.set_label('Number', fontsize = 18)
plt.xlabel('log$_{10}$[stellar mass]', fontsize=18)
plt.ylabel('(u-r) color', fontsize=18)
plt.xticks([10, 10.3, 10.6, 10.9, 11.2, 11.5], fontsize=18)
plt.yticks([1.25, 1.75, 2.25, 2.75, 3.15], fontsize=18)
#plt.savefig('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_V_Professional_Plotting_with_Python/plots/TaskV_Step2.pdf', 
#               format='pdf', bbox_inches='tight')
plt.show()