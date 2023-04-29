#!../py310_env/bin/python

import sys
sys.path.append("/DATA/aakash/paper-1/general_scripts/")
from genutils import check

HEADER = \
"""
# SCRIPT TO PERFORM THE FOLLOWING OPERATIONS  (Data Preparation)

1. Load the input images. (10 images, each of the same area but of a differnt time)
2. Cut the input images into smaller images of dimensions (384 x 384)
3. Prepare a single h5 file for these images with the following keys : image_id, image_array (uint8)
"""

check("header", HEADER)

import os
import numpy as np
from tqdm import tqdm
import argparse
import h5py

from PIL import Image
Image.MAX_IMAGE_PIXELS = pow(10,12)
check("info", "All modules loaded successfully...")

parser = argparse.ArgumentParser()
parser.add_argument("input_dir", help="Location of the input directory containing images of different times. (Image format = TIF)")
parser.add_argument("output_dir", help="Location of the directory to save the H5 files into.")
parser.add_argument("-img_res", help="Resolution of the square subimages that are to be generated. (we use 384)", default=384)

args = parser.parse_args()
input_dir = args.input_dir
output_dir = args.output_dir # THe complete location of the output_directory
img_res = args.img_res

check("info", "All arguments loaded...")

in_files_list = sorted(os.listdir(input_dir)) # will be used as image ID
check("info", "Files list : " + str(in_files_list))

image_data = [] # All images will be loaded into this list

# Open each of the files, load to memory
for file in tqdm(in_files_list, desc="Loading images.", leave=True):
    # Open the file
    file_path = os.path.join(input_dir, file)
    im = Image.open(file_path) 
    imarray = np.array(im) 
    imarray.shape 
    #im.show()
    # Append array to image_data
    image_data.append(imarray)

check("info", "All images loaded into memory...")

data_points = [] # This list stores all the data_points to be added to the h5 file, each smaller image area will be a separate data point

#image_data[np.isnan(image_data)] = 0
image_data = (image_data-np.min(image_data))/(np.max(image_data)-np.min(image_data))
image_data = np.array(image_data, dtype=np.uint8) # Full image data
print(image_data.shape)

row_start = 0
col_start = 0

row_chunk_count = int(np.floor(image_data.shape[1])/img_res)
col_chunk_count = int(np.floor(image_data.shape[2])/img_res)

row_chunk_counter = 0
col_chunk_counter = 0

image_data_final = [] # Image data with data points
image_ids_final = [] # Image ids for data points



for row_counter in [_ for _ in range(row_chunk_count)]:
    for col_counter in [__ for __ in range(col_chunk_count)]:
        data = image_data[:][row_start:row_start+img_res][col_start:col_start+img_res]
        id = "r" + str(row_counter) + "c" + str(col_counter)
        #if row_start == 0 and col_start == 0:
        #    img = Image.fromarray((data*255).astype(np.uint8))
        #    img.show()
        image_data_final.append(data)
        image_ids_final.append(id)
        col_start += img_res
    row_start += img_res

check("info", "Images subdivided...")



# Save dict as HDF5 file
output_file_path = output_dir
with h5py.File(output_file_path, 'w') as f:
    for counter in range(len(image_data)):
        f.create_dataset(image_ids_final[counter], data = image_data_final[counter])

check("info", "Images saved into ")
