#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print len(enron_data)
print len(enron_data['METTS MARK'])
poi = 0
for name in enron_data:
    if enron_data[name]['poi'] is True:
        poi += 1
print poi

file = open("poi_names.txt", "r")
names = file.read()
inter_list = names.split("\n")
for i in range(len(inter_list)):
    inter_list[i] = inter_list[i][4:]
    inter_list[i] = inter_list[i].split(", ")

final_list = list()
inter_list = inter_list[:-1]
for lists in inter_list:
    final_list.append(lists[1].upper() + " " + lists[0].upper())
print len(final_list)

for name in enron_data:
    if "JAMES" in name and "Prentice".upper() in name:
        print enron_data[name], name
    if "Wesley".upper() in name and "Colwell".upper() in name:
        print enron_data[name], name
    if "Jeffrey".upper() in name and "Skilling".upper() in name:
        print enron_data[name], name

