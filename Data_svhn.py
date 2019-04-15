import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

def readsvhn():
	image_ind = 21
	train_data = sio.loadmat('SVHN/train_32x32.mat')
	test_data = sio.loadmat('SVHN/test_32x32.mat')

	# access to the dict
	x_train = train_data['X']
	y_train = train_data['y']

	x_test = test_data['X']
	y_test = test_data['Y']

	# show sample
	plt.imshow(x_train[:,:,:,image_ind])
	plt.show()

	return x_train, y_train, x_test, y_test