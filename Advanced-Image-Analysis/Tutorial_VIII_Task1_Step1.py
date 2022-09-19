#Task 1 Image Cutout

from astropy.io import fits
from astropy.wcs import WCS
from astropy.nddata import Cutout2D
import matplotlib.pyplot as plt
from astropy.visualization import (PercentileInterval, AsinhStretch, ImageNormalize)
from astropy.convolution import Box2DKernel, convolve

'''
Step 1
'''
#importing data, reading in header information
large_image_data = fits.getdata('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/data/large_mosaic.fits')
large_image_header = fits.getheader('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/data/large_mosaic.fits')
#extracting WCS information from the header
large_image_WCS = WCS(large_image_header)

#creating the cutout from a specific point in the center of the desired object and extending it out to the size I want
x_cen = 505
y_cen = 506
xsize = 200
ysize = 200
cutout_image = Cutout2D(large_image_data, (x_cen, y_cen), (xsize, ysize), wcs = large_image_WCS)

#accessing the image data from the cutout
cutout_data = cutout_image.data
cutout_WCS = cutout_image.wcs #this will be different than the original image WCS

#create a fits file with the cutout
#fits.writeto('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/data/my_postage_stamp.fits', 
#             cutout_data, header=cutout_WCS.to_header())

#smoothing image
box_sizeB = 3
box = Box2DKernel(box_sizeB)
convolved_box = convolve(cutout_data, box)

#plotting
fig, axs = plt.subplots()
normalization = ImageNormalize(convolved_box, interval=PercentileInterval(99.), stretch=AsinhStretch())
axs.imshow(convolved_box, origin='lower', cmap='gray_r', norm=normalization)
axs.xaxis.set_visible(False)
axs.yaxis.set_visible(False)

#plt.tight_layout()
#plt.savefig('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VIII_Advanced_Image_Analysis/plots/my_postage_stamp.pdf', 
#             format='pdf', bbox_inches='tight')
#plt.show()

