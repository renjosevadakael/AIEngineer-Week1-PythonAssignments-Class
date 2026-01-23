import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report)
import matplotlib.pyplot as plt
import seaborn as sns
# 1. Load the dataset
df = pd.read_csv('Home/Social_Network_Ads.csv')

# Display: First few rows
print("First few rows of the dataset:")
print(df.head())
print("\n" + "="*50 + "\n")

# Display: Dataset shape
print(f"Dataset Shape: {df.shape}")
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print("\n" + "="*50 + "\n")

# Display: Summary statistics
print("Summary Statistics:")
print(df.describe())
print("\n" + "="*50 + "\n")

# Check for missing values
print("Missing Values:")
print(df.isnull().sum())
print(f"\nTotal missing values: {df.isnull().sum().sum()}")
print("\n" + "="*50 + "\n")


# 2. Preprocessing
# Encode the target variable 'Purchased' (No -> 0, Yes -> 1)
le = LabelEncoder()

df['Purchased_Encoded']=le.fit_transform(df['Purchased'])

""" # Check what labels the encoder found
print(f"Original labels found: {le.classes_}") """

# Independent Variables or Features (X): Age and EstimatedSalary
X = df[['Age', 'EstimatedSalary']]
# Dependent Variable or Label  (y): Purchased_Encoded
y = df['Purchased_Encoded']

""" print("Feature Variables (X):")
print(X.head())
print(f"\nX shape: {X.shape}")

print("Target Variable (y):")
print(y.head())
print(f"\ny shape: {y.shape}") """

# 3. Split to train and test sets ( 80/20)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=12)
print("Train-Test Split:")
print(f"Training set size: {X_train.shape[0]} samples ({(X_train.shape[0]/len(X))*100:.1f}%)")
print(f"Testing set size: {X_test.shape[0]} samples ({(X_test.shape[0]/len(X))*100:.1f}%)")
print("\n" + "="*50 + "\n")

# 4 Initialise and train the Logistic regresion model , use class_weight=balanced so that both cards are equally balanced
# Create the Logistic Regression Model
model = LogisticRegression(class_weight='balanced',random_state=12)
# Train the model with training data
model.fit(X_train,y_train) # Sigmoid function conversion
print("Model training completed")
print("\n" + "="*50 + "\n")

# Predict: Class labels (y) for test data
y_pred = model.predict(X_test)
""" print("Predicted Class Labels (first 10):")
print(y_pred[:10])
print("\n" + "="*50 + "\n") """
y_pred = model.predict(X_test)
print("Test Data with Predicted Class Labels (first 10):")
print(f"{'Age':<8} {'Salary':<15} {'Actual y':<12} {'Predicted y':<12}")
print("-" * 50)
for i in range(min(10, len(X_test))):
    age = X_test.iloc[i]['Age']
    salary = X_test.iloc[i]['EstimatedSalary']
    actual = y_test.iloc[i]
    predicted = y_pred[i]
    print(f"{age:<8} {salary:<15.0f} {actual:<12} {predicted:<12}")
print("\n" + "="*50 + "\n")

# Predict: Probabilities for test data
y_pred_proba = model.predict_proba(X_test)
print("Predicted Probabilities for Test Data (first 5 samples):")
print("Sample | P(Not Purchased) | P(Purchased)")
print("-" * 45)
for i in range(min(5, len(y_pred_proba))):
    print(f"  {i+1}    |      {y_pred_proba[i][0]:.4f}      |    {y_pred_proba[i][1]:.4f}")
print("\n" + "="*50 + "\n")

# Display model coefficients
print("Model Coefficients:")
print(f"Age coefficient: {model.coef_[0][0]:.4f}")
print(f"EstimatedSalary coefficient: {model.coef_[0][1]:.4f}")
print(f"Intercept: {model.intercept_[0]:.4f}")
print("\n" + "="*50 + "\n")

#Step 5: Model Evaluation (Important)

print(f"Accuracy Score  {accuracy_score(y_test,y_pred):.2f}")
print(f"Precision Score  {precision_score(y_test,y_pred,zero_division=0):.2f}")
print(f"Recall Score  {recall_score(y_test,y_pred,zero_division=0):.2f}")
print(f"F1 Score  {f1_score(y_test,y_pred,zero_division=0):.2f}")
print(f"Confusion Matrix {confusion_matrix(y_test,y_pred)}")

#Step 6: Visualization
# Plot the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
# Extract True Negative, False Positive, False Negative, True Positive
tn, fp, fn, tp = cm.ravel()

print(f"\nConfusion Matrix Breakdown:")
print(f"True Negatives (TN):  {tn}")
print(f"False Positives (FP): {fp}")
print(f"False Negatives (FN): {fn}")
print(f"True Positives (TP):  {tp}")
print("\n" + "="*50 + "\n")

# Create a figure
plt.figure(figsize=(8, 6))
class_labels = ['Not Purchased', 'Purchased']
# Plot confusion matrix using seaborn heatmap
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=class_labels, 
            yticklabels=class_labels,
            cbar_kws={'label': 'Count'})

# Add labels and title
plt.xlabel('Predicted Class', fontsize=12, fontweight='bold')
plt.ylabel('Actual Class', fontsize=12, fontweight='bold')
plt.title('Confusion Matrix - Customer Purchase Prediction', fontsize=14, fontweight='bold')

# Add TN, FP, FN, TP labels in each cell
# True Negative (top-left)
plt.text(0.5, 0.7, 'TN', ha='center', va='center', 
         fontsize=12, color='darkblue', fontweight='bold')

# False Positive (top-right)
plt.text(1.5, 0.7, 'FP', ha='center', va='center', 
         fontsize=12, color='red', fontweight='bold')

# False Negative (bottom-left)
plt.text(0.5, 1.7, 'FN', ha='center', va='center', 
         fontsize=12, color='red', fontweight='bold')

# True Positive (bottom-right)
plt.text(1.5, 1.7, 'TP', ha='center', va='center', 
         fontsize=12, color='darkgreen', fontweight='bold')


# Adjust layout and display
plt.tight_layout()
plt.show()


