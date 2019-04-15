import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

# Read SVHN file and return 4 numpy arrays of trainng/testing data/labels
def readsvhn():
	image_ind = 2
	train_data = sio.loadmat('SVHN/train_32x32.mat')
	test_data = sio.loadmat('SVHN/test_32x32.mat')

	# access to the dict
	x_train = train_data['X']
	y_train = train_data['y']

	x_test = test_data['X']
	y_test = test_data['y']

	x_train = x_train[:,:,0, :]*0.33 + x_train[:,:,1, :]*0.33 + x_train[:,:,2, :]*0.33
	x_test = x_test[:,:,0, :]*0.33 + x_test[:,:,1, :]*0.33 + x_test[:,:,2, :]*0.33
	return x_train, y_train, x_test, y_test
	