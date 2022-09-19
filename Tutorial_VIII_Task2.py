#Tutorial VIII Task 2

from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import (PercentileInterval, AsinhStretch, ImageNormalize)
import sep
import numpy as np
from matplotlib.patches import Ellipse, Circle

my_postage_data = fits.getdata('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/data/my_postage_stamp.fits')
my_postage_header = fits.getheader('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/data/my_postage_stamp.fits')

#changing byte order
byte_swaped_data = my_postage_data.byteswap().newbyteorder()

#above this range sources will be identified
back_size2 = 128
back_filter_size2 = 5
global_bkg2 = sep.Background(byte_swaped_data, bw=back_size2, bh=back_size2, 
                            fw=back_filter_size2, fh=back_filter_size2)
#background subtraction
bkg_subtracted2 = byte_swaped_data - global_bkg2

#convolution filter
filter_size = 5 #number of pixels
Bsource_kernel = Box2DKernel(filter_size)

#object catalog and segmentation map
min_area2 = 10
nsigma2 = 3
deb_n_thresh2 = 64
deb_count2 = 0.001
objects2, segmap2 = sep.extract(bkg_subtracted2, nsigma2, err=global_bkg2.globalrms,
                              minarea=min_area2, deblend_nthresh=deb_n_thresh2, 
                              deblend_cont=deb_count2, segmentation_map=True, 
                              filter_kernel = Bsource_kernel.array)

#Plotting image
normalization = ImageNormalize(my_postage_data, interval=PercentileInterval(99.), stretch=AsinhStretch())
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=[8,10])
axs1, axs2 = axs

rad = 7
for i in range(len(objects2)):
    c = Circle(xy=(objects2['x'][i], objects2['y'][i]), radius=rad)
    c.set_facecolor('none')
    c.set_edgecolor('red')
    axs1.add_artist(c)
    
axs1.imshow(my_postage_data, origin='lower', cmap='Greys_r', norm=normalization)
axs1.xaxis.set_visible(False)
axs1.yaxis.set_visible(False)

# plot an ellipse for each object
for i in range(len(objects2)):
    e = Ellipse(xy=(objects2['x'][i], objects2['y'][i]),
                width=6*objects2['a'][i],
                height=6*objects2['b'][i],
                angle=objects2['theta'][i] * 180. / np.pi)
    e.set_facecolor('none')
    e.set_edgecolor('red')
    axs2.add_artist(e)

axs2.imshow(my_postage_data, origin='lower', cmap='Greys_r', norm=normalization)
axs2.xaxis.set_visible(False)
axs2.yaxis.set_visible(False)

plt.tight_layout()
plt.savefig('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/plots/elipses_circles.pdf', 
             format='pdf', bbox_inches='tight')
plt.show()