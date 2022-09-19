#Task III

'''
1.4.1 Loading Image Data, Headerm and WCS
'''
#Importing modules
from astropy.io import fits
from astropy.wcs import WCS

#Two options for header info for a single extension fits file

###Opening files and getting header
#fits_file = fits.open('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/data/***', 
#                      memmap=True)
#image_data = fits_file[0].data
#image_header = fits_file[0].header
#wcs_image = WCS(image_header)
#fits_file.close()

'''
1.4.1 Loading Image Data, Header, and WCS
'''
##Retreiving info w/o opening file
image_data = fits.getdata('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/data/large_mosaic.fits')
image_header = fits.getheader('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/data/large_mosaic.fits')


#Multi extension file
cube = fits.open('/Users/laurenhiggins/Desktop/499_Kam/Tutorial_VI_Astronomy_Image_Analysis_I/data/image_cube.fits', 
                      memmap=True)
image_data_1 = cube[1].data
image_data_2 = cube[2].data
image_data_3 = cube[3].data

image_header_1 = cube[1].header
image_header_2 = cube[2].header
image_header_3 = cube[3].header

cube.close()

'''
1.4.2 Viewing the Images
'''
#importing modules
import matplotlib.pyplot as plt
from astropy.visualization import (MinMaxInterval, PercentileInterval, ZScaleInterval, SqrtStretch, 
                                   AsinhStretch, LogStretch, ImageNormalize)

#plotting image
fig, axis = plt.subplots()
c = axis.imshow(image_data, origin='lower', cmap='Greys_r') #play with the colormap
cbar = plt.colorbar(c)
axis.xaxis.set_visible(False)
axis.yaxis.set_visible(False)
plt.show()

#normalizing
fig, axis = plt.subplots()
normalization = ImageNormalize(image_data, interval=PercentileInterval(99.), stretch=AsinhStretch())
c2 = axis.imshow(image_data, origin='lower', cmap='gray_r', norm=normalization)
cbar = plt.colorbar(c2)
axis.xaxis.set_visible(False)
axis.yaxis.set_visible(False)
plt.show()

'''
1.4.3 Convolution
'''
#importing modules
from astropy.convolution import Box2DKernel, convolve, Gaussian2DKernel, Tophat2DKernel

box_size = 15
kernel = Box2DKernel(box_size)
convolved_data = convolve(image_data, kernel)
