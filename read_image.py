#import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd
#import seaborn as sns
import tensorflow as tf

num_vectors = 1000
num_clusters = 3
num_steps = 100
vector_values = []

for i in range(num_vectors):
  if np.random.random() > 0.5:
    vector_values.append([np.random.normal(0.5, 0.6),
                          np.random.normal(0.3, 0.9)])
  else:
    vector_values.append([np.random.normal(2.5, 0.4),
                         np.random.normal(0.8, 0.5)])

f = open("result.txt", "w")
f.write("Data points\n");
for i in range(num_vectors):
  f.write("({}, {})\n".format(vector_values[i][0], vector_values[i][1]))
f.close()



