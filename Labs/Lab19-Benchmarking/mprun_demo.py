
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from numpy import linalg as LA
import pandas as pd

def tune_fit(in_vars,classes):
    grove = RandomForestClassifier(n_estimators=10, max_features = 3, max_depth=2, random_state=0)
    grove.fit(in_vars,classes)
