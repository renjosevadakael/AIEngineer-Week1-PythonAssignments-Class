import numpy as np
simplearr=np.array([1,2,3,4])
x=simplearr.copy()
print("Copied X Before", x)
simplearr[0]=44

print("simplearr",simplearr)
print("Copied X after", x)

y=simplearr.view()
print("View Y Before", y)
simplearr[1]=43
print("simplearr",simplearr)
print("View Y After", y)
