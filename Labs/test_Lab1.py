import pytest
import labone 


def test_importdata():
	expected = (517,13)
	assert labone.importdata("../Data/forestfires.csv").shape == expected

def test_addingthings():
	expected = 7
	assert labone.addingthings(3,4) == expected

def test_addfive():
	expected = 12
	assert labone.addfive(7)