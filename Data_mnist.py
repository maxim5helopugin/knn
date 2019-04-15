import numpy
import struct

def read_idx(filename):															#
	with open(filename, 'rb') as f:												#
		zero, data_type, dims = struct.unpack('>HBB', f.read(4))				#
		shape = tuple(struct.unpack('>I', f.read(4))[0] for d in range(dims))	#
		return numpy.fromstring(f.read(), dtype=numpy.uint8).reshape(shape)

def readmnist():
	test_images = numpy.array(read_idx('MNIST/t10k-images.idx3-ubyte'), dtype=numpy.int32)
	test_labels = numpy.array(read_idx('MNIST/t10k-labels.idx1-ubyte'), dtype=numpy.int32)
	train_images = numpy.array(read_idx('MNIST/train-images.idx3-ubyte'), dtype=numpy.int32)
	train_labels = numpy.array(read_idx('MNIST/train-labels.idx1-ubyte'), dtype=numpy.int32)	

	print(train_images.shape)
	return train_images.reshape(train_images.shape[0],-1), train_labels.reshape(train_labels.shape[0],-1), test_images.reshape(test_images.shape[0],-1), test_labels.reshape(test_labels.shape[0],-1)