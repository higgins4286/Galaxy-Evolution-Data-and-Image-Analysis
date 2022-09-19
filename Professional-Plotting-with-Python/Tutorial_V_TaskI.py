#Task I 

#Step 1, Activity I
from astropy.cosmology import Planck15
redshift = 2.0
look_back_time = Planck15.lookback_time(redshift).value

#Step 2
import numpy as np
redshifts = np.array([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
lookback_times = Planck15.lookback_time(redshifts).value


#Step 3, Activity 3
x = [0.75, 1.25, 1.75, 2.25, 2.75]
y = [0.05, 0.1, 0.15, 0.2, 0.25]
y2 = [0.01, 0.05, 0.1, 0.05, 0.02]

import matplotlib.pyplot as plt
catalog = np.genfromtxt('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_V_Professional_Plotting_with_Python/data/sdss_tutorial_file_v2.csv', 
                        dtype=None, delimiter=",", names=True, encoding=None)
truth_array_etg = [each_gal['mag_u']!=-99 and 'ETG' in each_gal['Type'] for each_gal in catalog]
fancy_subset_etg = catalog[truth_array_etg]

fig = plt.figure(figsize=(8,6))
axis = plt.gca()
axis.plot(x, y, marker='o', markersize=10, color='red', linestyle='None')
axis.plot(x, y2, marker='o', markersize=10, markerfacecolor='None', markeredgecolor='red', linestyle='None')
axis.set_xlim([0, 3])
#axis.set_ylim([0, 0.25])
axis.set_yticks([0, 0.05, 0.1, 0.15, 0.2, 0.25])
axis.set_yticklabels([0, 0.05, 0.1, 0.15, 0.2, 0.25], fontsize=18)
#axis.set_xticks([10, 10.3, 10.6, 10.9, 11.2, 11.5], fontsize=18)
axis.set_xticklabels([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0], fontsize=18)
axis.set_xlabel('Redshift', fontsize=18)
axis.set_ylabel('Arbitrary Quantity', fontsize=18)

#Step 4
twin_axis = axis.twiny()
twin_axis.set_xlim([-0.01, 3.01]) 
twin_axis.set_xticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
twin_axis.set_xticklabels(np.round(lookback_times, 1), fontsize=18)
twin_axis.xlabel('Lookback Time [Gyr]', fontsize=18)
twin_axis 

plt.tight_layout()
plt.show()