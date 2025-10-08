import numpy as np

def statisticalSummary(arr):
    mean = np.mean(arr)
    mean_rounded=float(round(mean,2))
    median = np.median(arr)
    median_rounded=float(round(median,2))
    std_dev= np.std(arr)
    std_dev_rounded= float(round(std_dev,2))
    return (mean_rounded,median_rounded,std_dev_rounded)

arr = np.array([10,20,30,40,50])
result =statisticalSummary(arr)
print(result)