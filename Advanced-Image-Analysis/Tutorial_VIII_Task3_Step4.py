from copy import deepcopy
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import (PercentileInterval, AsinhStretch, ImageNormalize)
from astropy.convolution import Box2DKernel
import sep
import numpy as np

my_postage_data = fits.getdata('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/data/my_postage_stamp.fits')
my_postage_header = fits.getheader('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/data/my_postage_stamp.fits')

#changing byte order
byte_swaped_data = my_postage_data.byteswap().newbyteorder()

#above this range sources will be identified
##boxes of this size all over the image and calculates the mean and variance of each box
back_size2 = 128
#convolves the background
back_filter_size2 = 5
global_bkg2 = sep.Background(byte_swaped_data, bw=back_size2, bh=back_size2, 
                            fw=back_filter_size2, fh=back_filter_size2)
#background subtraction
bkg_subtracted2 = byte_swaped_data - global_bkg2

#convolution filter NOT GOING TO CALCULATE THE BACKGROUND
filter_size = 5 #number of pixels
Bsource_kernel = Box2DKernel(filter_size)

#object catalog and segmentation map
min_area2 = 10
nsigma2 = 1
deb_n_thresh2 = 64
deb_count2 = 0.001
objects2, segmap2 = sep.extract(bkg_subtracted2, nsigma2, err=global_bkg2.globalrms,
                              minarea=min_area2, deblend_nthresh=deb_n_thresh2, 
                              deblend_cont=deb_count2, segmentation_map=True, 
                              filter_kernel = Bsource_kernel.array)
print(segmap2)

#creating a mask for all sources
mask = deepcopy(segmap2)
mask = mask + 1
mask[ mask > 1] = 0
masked_data = my_postage_data * mask

#Plotting image and segmap
normalization = ImageNormalize(my_postage_data, interval=PercentileInterval(99.), stretch=AsinhStretch())

fig, axs = plt.subplots(2, 2, figsize=[8,8])

#Cut out
axs[0, 0].imshow(my_postage_data, origin='lower', cmap='Greys_r', norm=normalization)
axs[0, 0].xaxis.set_visible(False)
axs[0, 0].yaxis.set_visible(False)
#axs1.text(400, 40, 'Config 1', color='white', fontsize=12) # 1000 x 1000, large

axs[0, 1].imshow(segmap2, origin='lower')
axs[0, 1].xaxis.set_visible(False)
axs[0, 1].yaxis.set_visible(False)

axs[1, 0].imshow(mask, origin='lower')
axs[1, 0].xaxis.set_visible(False)
axs[1, 0].yaxis.set_visible(False)

axs[1, 1].imshow(masked_data, origin='lower', cmap='Greys_r', norm=normalization)
axs[1, 1].xaxis.set_visible(False)
axs[1, 1].yaxis.set_visible(False)

plt.tight_layout()
plt.savefig('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/plots/segmap_maskAll.pdf', 
             format='pdf', bbox_inches='tight')
plt.show()
