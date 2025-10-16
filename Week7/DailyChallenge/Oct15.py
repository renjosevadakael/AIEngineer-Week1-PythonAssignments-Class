"""Random Array with mean, max, min"""

import numpy as np

def randomArrayAnalysis(n):
    np.random.seed(0)
    random_array=np.random.randint(low=10,high=101,size=n)
    max=np.max(random_array)
    min=np.min(random_array)
    mean= np.mean(random_array)
    round_mean=round(mean,2)
    return (max, min, round_mean)

n=5
print(randomArrayAnalysis(n))
