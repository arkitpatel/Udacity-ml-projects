#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from tools.feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
# feature_3 = "total_payments"
poi  = "poi"
# features_list = [poi, feature_1, feature_2, feature_3]
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )

max_val = 0
for name in data_dict:
    if data_dict[name]['exercised_stock_options'] != "NaN":
        if data_dict[name]['exercised_stock_options'] >= max_val:
            max_val = data_dict[name]['exercised_stock_options']
min_val = max_val
for name in data_dict:
    if data_dict[name]['exercised_stock_options'] != "NaN":
        if data_dict[name]['exercised_stock_options'] <= min_val:
            min_val = data_dict[name]['exercised_stock_options']
print "max exercised stock options =", max_val
print "min exercised stock options =", min_val


max_val = 0
for name in data_dict:
    if data_dict[name]['salary'] != "NaN":
        if data_dict[name]['salary'] >= max_val:
            max_val = data_dict[name]['salary']
min_val = max_val
for name in data_dict:
    if data_dict[name]['salary'] != "NaN":
        if data_dict[name]['salary'] <= min_val:
            min_val = data_dict[name]['salary']
print "max salary =", max_val
print "min salary =", min_val
### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
feat1 = list()
feat2 = list()
from sklearn.preprocessing import MinMaxScaler
scale = MinMaxScaler()
scale.fit_transform(finance_features)
scaler = scale.transform(finance_features)
for f1, f2 in scaler:
    feat1.append(f1)
    feat2.append(f2)
plt.scatter( feat1, feat2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.cluster import KMeans
print scale.transform([[200000., 1000000.]])
cluster = KMeans(n_clusters=2)
cluster.fit(scaler)
pred = cluster.predict(scaler)

### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, scaler, poi, mark_poi=False, name="clusters3.pdf", f1_name=feat1, f2_name=feat2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
