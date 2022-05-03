#import libraries
import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt



# Read the CSV file and look at the first 5 rows
#PLEASE KEEP THIS FILE in your Python Working Directory I have attached with the assignment
# Any dataset can be used and then rename it accordingly
data = pd.read_csv('cluster_data.csv')  #Enter your dataset
data.head()




#Taking “Node_1” and “Node_2”.
Z = data[["Node_1","Node_2"]]

#Visualise the data points and colors are set to black
plt.scatter(Z["Node_2"],Z["Node_1"],c='black')
plt.xlabel('Node_2')
plt.ylabel('Node_1')
plt.show()




# # of clusters
# I have chosen the value for K as 2, it can be changed from the below
K=2

# Random observation as pick
pick = (Z.sample(n=K))
plt.scatter(Z["Node_2"],Z["Node_1"],c='black')
plt.scatter(pick["Node_2"],pick["Node_1"],c='red')
plt.xlabel('Node_2')
plt.ylabel('Node_1')
plt.show()




# Assign the points to the closest cluster centroid
# Recomputing the centroids of newly formed clusters

difference = 1
j=0

while(difference!=0):
    i=1
    _xdiff=Z
    #iterrows() is used to iterate over a pandas Data frame rows in the form of (index, series) pair.
    for ind1, c_row in pick.iterrows():
        _ed=[]
        for ind2, d_row in _xdiff.iterrows():
            _d1=(c_row["Node_2"] - d_row["Node_2"])**2
            _d2=(c_row["Node_1"] - d_row["Node_1"])**2
            d=np.sqrt(_d1 + _d2)
            _ed.append(d)
        Z[i] = _ed
        i = i+1

    _c=[]
    for index, row in Z.iterrows():
        _mindist = row[1]
        pos = 1
        for i in range(K):
            if row[i+1] < _mindist:
                _mindist = row[i+1]
                pos = i+1
        _c.append(pos)

    Z["Cluster"] = _c
    pick_new = Z.groupby(["Cluster"]).mean()[["Node_1","Node_2"]]
    if j == 0:
        difference = 1
        j = j+1
    else:
        difference = (pick_new['Node_1'] - pick['Node_1']).sum() 
        + (pick_new['Node_2'] - pick['Node_2']).sum()
        print(difference.sum())
    pick = Z.groupby(["Cluster"]).mean()[["Node_1","Node_2"]]
    
    # I have used color to identify clusters in final plot
    color=['green','blue', 'cyan']




# Final cluster plot for graphical view as discussed during TA hours  
for k in range(K):
    data=Z[Z["Cluster"]==k+1]
    plt.scatter(data["Node_2"],data["Node_1"],c=color[k])
plt.scatter(pick["Node_2"],pick["Node_1"],c='red')
plt.xlabel('Node_2')
plt.ylabel('Node_1')
plt.show()
