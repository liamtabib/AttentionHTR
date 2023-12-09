import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join
import random
import cv2 as cv

# Function to extract numerical values from a line
def extract_numbers(line):
    # Split the line into words
    words = line.split()
    
    # Extract the numerical value (assuming it's the last token on the line)
    try:
        value = float(words[-1])
        return value
    except ValueError:
        return None

# Read the text file and extract numerical values
GW = 'GW'
IAM = 'IAM'
IMGUR5k = 'IMGUR5k'
datasets = [IAM, IMGUR5k, GW]
names = ['IAM', 'IMGUR5K', 'Washington']
# Set up the figure and adjust subplot spacing
f, axarr = plt.subplots(3,10, figsize=(20, 2))

for index_dataset, dataset in enumerate(datasets):
    print(dataset)
    for index_image, confidence in enumerate(np.arange(0.0, 1.0, 0.1)): 
        path = f'synthetic_{dataset}/{str(round(confidence, 1))}-{str(round(confidence+0.1, 1))}_confidence/'
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        print(random.choice(onlyfiles))
        print(path + random.choice(onlyfiles))

        image = cv.imread(path + random.choice(onlyfiles))
        axarr[index_dataset,index_image].imshow(image)
        axarr[index_dataset,index_image].axis('off')
    print('\n')
    
plt.show()