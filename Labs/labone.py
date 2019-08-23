import pandas as pd

def importdata(filename):
	df = pd.read_csv(filename, sep=",")
	return df

def addingthings(x,y):
	return x + y

#def addfive(z):
#	return 5 + z