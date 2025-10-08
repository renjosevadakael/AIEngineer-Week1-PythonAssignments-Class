

""" Breakout Session Qsn: 
Use Standard Scalar method to transform the data [[1, 2], [3, 4], [5, 6]]) """

from sklearn.preprocessing import StandardScaler

data =[[1, 2], [3, 4], [5, 6]]

scaler = StandardScaler()
# Method1
scaled_data = scaler.fit_transform(data)
print(scaled_data)
# Method2
scaler.fit(data)
scaler.transform(data)
print(scaler.transform(data))



