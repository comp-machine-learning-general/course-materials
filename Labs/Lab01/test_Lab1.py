import pytest
import labone 
import os

path, _ = os.path.split(os.path.abspath(__file__))

def test_importdata():
	expected = (517,13)
	fname = os.path.join(path,"forestfires.csv")
	assert labone.importdata(fname).shape == expected

def test_addingthings():
	expected = 7
	assert labone.addingthings(3,4) == expected

def test_addfive():
	expected = 12
	assert labone.addfive(7)