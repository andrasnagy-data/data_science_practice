import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans

# data set
df = pd.read_csv('iris.data', header= None)
df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

# iris species vectors
setosa_x = df.loc[0:49, "sepal_length"]
setosa_y = df.loc[0:49, "sepal_width"]
versicolor_x = df.loc[50:99, "sepal_length"]
versicolor_y = df.loc[50:99, "sepal_width"]
virginica_x = df.loc[100:149, "sepal_length"]
virginica_y = df.loc[100:149, "sepal_width"]

# using only 2 features for simplicity
X = np.array(df.loc[:, "sepal_length": "sepal_width"])

# creating clustering object
kmeans = KMeans(n_clusters= 3)
kmeans.fit(X)

# KMeans attributes (cluster centers & labels)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# colors for clusters
colors = ["g.", "r.", "b."]

# visualizing outcome of KMeans clustering
fig = plt.figure(figsize= (18, 6))
plt.subplot2grid((1, 2), (0, 0))
for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize= 10)
plt.scatter(centroids[:, 0], centroids[:, 1], marker= "x", s= 150, linewidths= 5, zorder=10)
plt.title("Clusters via KMeans")
plt.xlabel("sepal-length")
plt.ylabel("sepal-width")

# visualizing labeled data set (OG)
plt.subplot2grid((1, 2), (0, 1))
plt.scatter(setosa_x, setosa_y)
plt.scatter(versicolor_x, versicolor_y)
plt.scatter(virginica_x, virginica_y)
plt.title("Iris species labeled")
plt.xlabel("sepal-length")
plt.ylabel("sepal-width")
plt.show()