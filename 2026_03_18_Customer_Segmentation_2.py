# Another clustering example
from sklearn.cluster import KMeans
import numpy as np

X = np.array([[5,100],[10,200],[6,120],[12,220]])
model = KMeans(n_clusters=2, n_init=10)
model.fit(X)
print("Cluster labels:", model.labels_)