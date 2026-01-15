""" Problem Statement 
You are provided with a Sales dataset that captures the relationship between Advertising 
Spend and Sales Revenue. 
Initial analysis shows that sales growth does not increase linearly with advertising spend. 
Your task is to: 
 Build a Polynomial Regression model 
 Compare it against a Linear Regression baseline 
 Decide which model better represents the data 
 
Dataset Description 
Dataset file: sales_data.csv 
Column Name Description 
Advertising_Spend Amount spent on advertising 
Sales Revenue generated """
from sklearn.model_selection import train_test_split
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score



""" Step 1: Data Exploration 
 Load the dataset using Pandas 
 Display summary statistics 
 Plot a scatter plot between Advertising Spend and Sales 
 Comment on whether the relationship appears linear or non-linear """

# Step 1: Load the dataset
data = pd.read_csv('sales_data.csv')
# Rename 'Total Amount' to 'Sales' for clarity
data = data.rename(columns={'Total Amount': 'Sales'})
df_model = data[['Advertising_Spend', 'Sales']]
df_cleaned = df_model.dropna()
# Display summary statistics
print(df_cleaned.describe())

adv_Q1 = df_cleaned['Advertising_Spend'].quantile(0.25)
adv_Q3 = df_cleaned['Advertising_Spend'].quantile(0.75)

adv_IQR = adv_Q3 - adv_Q1
lower_limit = adv_Q1 - 1.5 * adv_IQR
upper_limit = adv_Q3 + 1.5 * adv_IQR

adv_outliers_removed = df_cleaned[(df_cleaned['Advertising_Spend'] > lower_limit) & (df_cleaned['Advertising_Spend'] < upper_limit)]
print(adv_outliers_removed)
#sns.histplot(adv_outliers_removed,x=adv_outliers_removed['Advertising_Spend'],bins=10,kde=True, label='Advertising_spend Outliers removed')
#plt.legend()
#plt.show()

# Plot scatter plot between Advertising Spend and Sales
plt.figure(figsize=(10, 6))
plt.scatter(adv_outliers_removed['Advertising_Spend'], adv_outliers_removed['Sales'], color='blue', alpha=0.6, edgecolors='black')
plt.xlabel('Advertising Spend ($)', fontsize=12)
plt.ylabel('Sales Revenue ($)', fontsize=12)
plt.title('Advertising Spend vs Sales Revenue', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Comment on the relationship
print("\n=== Observation ===")
print("Based on the scatter plot:")
print("- NON-LINEAR relationship")

""" Step 2: Baseline Model – Simple Linear Regression 
 Build a Linear Regression model using: 
o X = Advertising_Spend 
o y = Sales 
 Train and predict on the same dataset 
 Evaluate the model using: 
o Mean Squared Error (MSE) 
o R² Score 
 Plot the regression line over the scatter plot """


X=adv_outliers_removed['Advertising_Spend'].to_numpy().reshape(-1,1)
y=adv_outliers_removed['Sales'].to_numpy()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Build Linear Regression Model
model_linear = LinearRegression()
model_linear.fit(X_train, y_train)
print("=== Model Parameters ===")
print(f"Slope: {model_linear.coef_[0]:.2f}")      # ← Part of model.fit()
print(f"Intercept: {model_linear.intercept_:.2f}") # ← Part of model.fit()
#Predict
y_pred_linear = model_linear.predict(X_test)

linear_mse = mean_squared_error(y_test, y_pred_linear)
linear_r2 = r2_score(y_test, y_pred_linear)
print("\n=== Model Evaluation ===")
print(f"MSE: {linear_mse:.2f}")    # ← Uses predict output
print(f"R²: {linear_r2:.4f}")      # ← Uses predict output


# Visualize the regression line
sorted_idx = X_test.flatten().argsort()  # ✓ ADDED: Sort for smooth line
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color="blue", label="Actual data", alpha=0.6)
plt.plot(X_test, y_pred_linear, color="red", label="Predictions", linewidth=2)  # ✓ FIXED
plt.xlabel("Advertising Spend ($)")
plt.ylabel("Sales Revenue ($)")
plt.title("Linear Regression: Actual vs Predicted")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

""" Step 3: Polynomial Feature Transformation 
 Use PolynomialFeatures to transform the independent variable 
 Train Polynomial Regression models with: 
o Degree 2 
o Degree 3 
 Clearly mention which degree you are using for final evaluation
 """

""" print("\n" + "="*60)
print("STEP 3: POLYNOMIAL FEATURE TRANSFORMATION")
print("="*60)

# ============= DEGREE 2 =============
print("\n--- Training Polynomial Regression (Degree 2) ---")
poly_2 = PolynomialFeatures(degree=2)
X_train_poly_2 = poly_2.fit_transform(X_train)
X_test_poly_2 = poly_2.transform(X_test)

# Fit model
model_poly_2 = LinearRegression()
model_poly_2.fit(X_train_poly_2, y_train)

# Predict
y_pred_poly_2 = model_poly_2.predict(X_test_poly_2)

# Evaluate
mse_2 = mean_squared_error(y_test, y_pred_poly_2)
r2_2 = r2_score(y_test, y_pred_poly_2)

print(f"Intercept (a0): {model_poly_2.intercept_:.2f}")
print(f"Coefficients (a1, a2): {model_poly_2.coef_[1]:.4f}, {model_poly_2.coef_[2]:.6f}")
print(f"MSE: {mse_2:.2f}")
print(f"R²: {r2_2:.4f}")

# ============= DEGREE 3 =============
print("\n--- Training Polynomial Regression (Degree 3) ---")
poly_3 = PolynomialFeatures(degree=3)
X_train_poly_3 = poly_3.fit_transform(X_train)
X_test_poly_3 = poly_3.transform(X_test)

# Fit model
model_poly_3 = LinearRegression()
model_poly_3.fit(X_train_poly_3, y_train)

# Predict
y_pred_poly_3 = model_poly_3.predict(X_test_poly_3)

# Evaluate
mse_3 = mean_squared_error(y_test, y_pred_poly_3)
r2_3 = r2_score(y_test, y_pred_poly_3)

print(f"Intercept (a0): {model_poly_3.intercept_:.2f}")
print(f"Coefficients (a1, a2, a3): {model_poly_3.coef_[1]:.4f}, {model_poly_3.coef_[2]:.6f}, {model_poly_3.coef_[3]:.8f}")
print(f"MSE: {mse_3:.2f}")
print(f"R²: {r2_3:.4f}")

# ============= MODEL COMPARISON =============
print("\n" + "="*60)
print("MODEL COMPARISON & FINAL SELECTION")
print("="*60)
print(f"Degree 2 - MSE: {mse_2:.2f}, R²: {r2_2:.4f}")
print(f"Degree 3 - MSE: {mse_3:.2f}, R²: {r2_3:.4f}")

# Select best model based on R² score
if r2_3 > r2_2:
    print(f"\n✓ FINAL MODEL: Degree 3 (Higher R²: {r2_3:.4f} vs {r2_2:.4f})")
    final_model = model_poly_3
    final_poly = poly_3
    final_y_pred = y_pred_poly_3
    final_degree = 3
else:
    print(f"\n✓ FINAL MODEL: Degree 2 (Higher R²: {r2_2:.4f} vs {r2_3:.4f})")
    final_model = model_poly_2
    final_poly = poly_2
    final_y_pred = y_pred_poly_2
    final_degree = 2

print("="*60) """

# Transform 
poly = PolynomialFeatures(degree=3)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
print(X_train_poly)
# Fit 
model_poly = LinearRegression()
model_poly.fit(X_train_poly, y_train)
# Print coefficients
print("=== Model Coefficients ===")
print(f"Intercept (a0): {model_poly.intercept_:.2f}")
print(f"Coefficients (a1, a2, a3): {model_poly.coef_[1]:.2f}, {model_poly.coef_[2]:.2f},{model_poly.coef_[3]:.2f}")
# Predict
y_pred_poly = model_poly.predict(X_test_poly)
# Calculate metrics
poly_mse = mean_squared_error(y_test, y_pred_poly)
poly_r2 = r2_score(y_test, y_pred_poly)
print("=== Model Evaluation ===")
print(f"MSE: {poly_mse:.2f}")
print(f"R²: {poly_r2:.4f}")
# Plotting
sorted_idx = X_test.flatten().argsort()
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='red', label='Actual Data', alpha=0.6)
plt.plot(X_test[sorted_idx], y_pred_poly[sorted_idx], color='blue', label='Polynomial Predictions', linewidth=2)
plt.xlabel('Advertising Spend ($)')
plt.ylabel('Sales Revenue ($)')
plt.title('Polynomial Regression (Degree 3): Actual vs Predicted')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

""" Step 5: Model Evaluation and Comparison 
Evaluate both Linear and Polynomial models using: 
 Mean Squared Error (MSE) 
 Root Mean Squared Error (RMSE) 
 R² Score 
Create a small comparison table showing: 
 
 Model Type 
 MSE 
 R² Score """

print("\n" + "="*60)
print("STEP 5: MODEL EVALUATION AND COMPARISON")
print("="*60)

# Calculate RMSE (values not yet calculated)
linear_rmse = np.sqrt(linear_mse)
poly_rmse = np.sqrt(poly_mse)

# Create comparison table
comparison_data = {
    'Model Type': ['Linear Regression', 'Polynomial Regression (Degree 3)'],
    'MSE': [linear_mse, poly_mse],
    'RMSE': [linear_rmse, poly_rmse],
    'R² Score': [linear_r2, poly_r2]
}

comparison_df = pd.DataFrame(comparison_data)

print("\n")
print(comparison_df.to_string(index=False))
print("\n" + "="*60)


""" Step 6: Visualization 
 Plot: 
o Actual sales data (scatter) 
o Linear regression line 
o Polynomial regression curve (smooth curve) 
 Ensure: 
o Clear labels 
o Legend 
o Proper title
 """
print("\n" + "="*60)
print("STEP 6: FINAL VISUALIZATION")
print("="*60)

# Sort indices for smooth curve plotting
sorted_idx = X_test.flatten().argsort()

# Create the comparison plot
plt.figure(figsize=(12, 7))

# 1. Scatter plot of actual sales data
plt.scatter(X_test, y_test, color='black', label='Actual Sales Data', 
            alpha=0.7, s=80, edgecolors='white', linewidth=1.5, zorder=3)

# 2. Linear regression line
plt.plot(X_test[sorted_idx], y_pred_linear[sorted_idx], 
         color='red', label='Linear Regression', 
         linewidth=2.5, linestyle='--', zorder=2)

# 3. Polynomial regression curve (smooth)
plt.plot(X_test[sorted_idx], y_pred_poly[sorted_idx], 
         color='blue', label='Polynomial Regression (Degree 3)', 
         linewidth=3, zorder=2)

# Labels and title
plt.xlabel('Advertising Spend ($)', fontsize=13, fontweight='bold')
plt.ylabel('Sales Revenue ($)', fontsize=13, fontweight='bold')
plt.title('Sales Forecast: Comparing Linear vs Polynomial Regression', 
          fontsize=15, fontweight='bold', pad=20)

# Legend
plt.legend(loc='upper left', fontsize=11, frameon=True, shadow=True, fancybox=True)

# Grid
plt.grid(True, alpha=0.3, linestyle=':', linewidth=1)

# Tight layout
plt.tight_layout()

# Show plot
plt.show()

print("✓ Visualization Complete")
print("="*60)

""" Step 7: User Input Prediction 
 Ask the user to enter a new Advertising Spend value 
 Predict sales using: 
o Linear Regression model 
o Polynomial Regression model 
 Print both predictions and briefly comment on the difference
 """

print("\n" + "="*60)
print("STEP 7: USER INPUT PREDICTION")
print("="*60)

# Get user input
user_spend = float(input("\nEnter Advertising Spend ($): "))
# Prepare input
X_new = np.array([[user_spend]])

# Predict using Linear Regression
linear_pred = model_linear.predict(X_new)[0]

# Predict using Polynomial Regression
X_new_poly = poly.transform(X_new)
poly_pred = model_poly.predict(X_new_poly)[0]

# Display results
print("\n--- PREDICTIONS ---")
print(f"Linear Regression: ${linear_pred:.2f}")
print(f"Polynomial Regression: ${poly_pred:.2f}")

# Comment on difference
diff = poly_pred - linear_pred
print("\n--- ANALYSIS ---")
print(f"Difference: ${abs(diff):.2f}")