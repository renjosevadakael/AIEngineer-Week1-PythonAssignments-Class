import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report)

# 1. Load the dataset
df = pd.read_csv('Class/sales_data.csv')

# 2. Preprocessing
# Encode the target variable 'CardType' (BaseCard -> 0, PrivilegedCard -> 1)
le = LabelEncoder()
df['CardType_Encoded']=le.fit_transform(df['CardType'])

# Define feature X and target  y ; We need to reshape X  to a 2 D array as we are having only 1 feature
X = df[['Total Amount']]
y = df['CardType_Encoded']

# 3. Split to train and test sets ( 80/20)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=12)

# 4 Initialise and train the Logistic regresion model , use class_weight=balanced so that both cards are equally balanced
model = LogisticRegression(class_weight='balanced',random_state=12)
model.fit(X_train,y_train) # Sigmoid function conversion

# 5 Predictions
y_pred = model.predict(X_test)

#6 Evaluate Model
print(f"Accuracy Score  {accuracy_score(y_test,y_pred):.2f}")
print(f"Precision Score  {precision_score(y_test,y_pred,zero_division=0):.2f}")
print(f"Recall Score  {recall_score(y_test,y_pred,zero_division=0):.2f}")
print(f"F1 Score  {f1_score(y_test,y_pred,zero_division=0):.2f}")
print(f"Confusion Matrix {confusion_matrix(y_test,y_pred)}")


#Classification Report
print(f"Classification Report")
print(classification_report(y_test,y_pred, target_names=le.classes_))

# Threshold 
# For Logistic Regression: 0 = coefficient * x + intercept
threshold = -model.intercept_[0] / model.coef_[0][0]
print(f"\nModel Threshold: Cards with Amount > {threshold:.2f} are classified as PrivilegedCard")


# For getting Input and Predict using Logistic Regression
# 1. Input the new amount
new_amount = float(input("Enter the Total Amount to classify: "))

# Create a DataFrame with proper column name (matches training data)
input_data = pd.DataFrame({'Total Amount': [new_amount]})

# Predict using the trained model
predicted_index = model.predict(input_data)

# Get prediction probabilities
probabilities = model.predict_proba(input_data)[0]
print(f"\nPrediction Probabilities:")
print(f"  BaseCard: {probabilities[0]:.2%}")
print(f"  PrivilegedCard: {probabilities[1]:.2%}")

# Convert the numerical prediction back to a readable label
predicted_card_type = le.inverse_transform(predicted_index)

# 5. Display the result
print(f"\nFor an amount of {new_amount}, the predicted Card Type is: {predicted_card_type[0]}")

