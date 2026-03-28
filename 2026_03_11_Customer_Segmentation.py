from sklearn.cluster import KMeans
import numpy as np

X = np.array([[25,500],[45,1000],[30,600],[50,1200]])
model = KMeans(n_clusters=2, n_init=10)
model.fit(X)
print("Cluster labels:", model.labels_)

