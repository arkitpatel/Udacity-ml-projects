#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from tools.feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
max_sal = 0
outlier = ""
for name in data_dict:
    if data_dict[name]["salary"] != "NaN":
        if data_dict[name]["salary"] >= max_sal:
            max_sal = data_dict[name]["salary"]
            outlier = name
print outlier
data_dict.pop(outlier)

for name in data_dict:
    if data_dict[name]["salary"] != "NaN":
        if data_dict[name]["salary"] >= 1000000 and data_dict[name]["bonus"] >= 5000000:
            print name
data = featureFormat(data_dict, features)


### your code below

salary = []
bonus = []
for point in data:
    salary.append(point[0])
    bonus.append(point[1])

matplotlib.pyplot.scatter(salary, bonus)
matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


