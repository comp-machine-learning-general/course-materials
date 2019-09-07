import pytest
import labone 
import os


def test_importdata():
	expected = (517,13)
	#dirname = os.getcwd()
	fname = os.path.join("forestfires.csv")
	assert labone.importdata(fname).shape == expected

def test_addingthings():
	expected = 7
	assert labone.addingthings(3,4) == expected

def test_addfive():
	expected = 12
	assert labone.addfive(7)