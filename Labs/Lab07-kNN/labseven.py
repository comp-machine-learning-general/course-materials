import numpy as np

our_data = np.loadtxt("lab7data.csv", delimiter=",")

def get_red_inds(num_inds):
	red_inds = np.random.choice(225, num_inds, replace=False)
	return list(red_inds)

def get_blue_inds(num_inds):
	blue_inds = np.random.choice(697, num_inds, replace=False)
	blue_inds += 225
	return list(blue_inds)

def blue_points(num_inds):
	blue_inds = get_blue_inds(num_inds)
	return our_data[blue_inds,:]

def red_points(num_inds):
	red_inds = get_red_inds(num_inds)
	return our_data[red_inds,:]