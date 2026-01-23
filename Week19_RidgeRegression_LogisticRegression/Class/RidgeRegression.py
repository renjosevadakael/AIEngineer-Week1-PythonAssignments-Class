
import numpy as np
from sklearn.linear_model import Ridge

# Sample data 
X = np.array([[1, 1],[1, 2],[1, 3]])
y = np.array([1,2,2])  

alpha = 1.0  # regularization strength (lambda)

model = Ridge(alpha=alpha,fit_intercept=False)
model.fit(X, y)

print("--- Ridge Model (Multivariate) ---")
print(f"alpha (λ): {alpha}")
print(f"Intercept: {model.intercept_:.4f}")
print(f"Shrunk Coefficient for x1: {model.coef_[0]:.4f}")
print(f"Shrunk Coefficient for x2: {model.coef_[1]:.4f}")
print(f"Shrunk Coefficient Matrixs: {model.coef_}")

# User input for prediction
try:
    x1_input = float(input("Enter x1 value: "))
    x2_input = float(input("Enter x2 value: "))
    y_hat = model.predict(np.array([[x1_input, x2_input]]))[0]
    print(f"Predicted y for x1={x1_input}, x2={x2_input} -> {y_hat:.4f}")
except ValueError:
    print("Please enter valid numeric values.")

"""     fit_intercept=True → Model learns intercept + coefficients (both shrunk by Ridge)
fit_intercept=False → Model learns only coefficients (shrunk), intercept forced to 0 """