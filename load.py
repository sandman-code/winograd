# load dogs vs cats dataset, reshape and save to a new file
from os import listdir
import numpy as np
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array


# define location of dataset
folder = 'PetImages/'
photos, labels = list(), list()
# enumerate files in the directory
for sub in listdir(folder):
 # determine class
    output = 0.0
    if sub == "Dog":
        output = 1.0
    
    for idx, file in enumerate(listdir(folder + '/' + sub)):

        if(idx > 4999):
            break
        try:
            photo = load_img(folder + sub + '/' + file, target_size=(200, 200))
            # convert to numpy array
            photo = img_to_array(photo)
            # store
            photos.append(photo)
            labels.append(output)
        except:
            print(f"Unable to load file number {idx}")


# convert to a numpy arrays
photos = np.asarray(photos)
labels = np.asarray(labels)
print(photos.shape, labels.shape)
# save the reshaped photos
save('dogs_vs_cats_photos.npy', photos)
save('dogs_vs_cats_labels.npy', labels)

