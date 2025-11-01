""" Assignment Details: 
1. You are provided with a dataset named Student_Performance.csv. 
The dataset contains multiple features (such as hours studied, sleep hours, attendance, 
etc.) and a target column Performance Index. 
2. Your task is to build a Multiple Linear Regression model to predict Performance 
Index. 
o Steps to Perform: 
1. Import Required Libraries 
2. Create a Class StudentPerformanceModel 
3. Data Preprocessing 
4. Train-Test Split 
5. Model Training 
6. Model Evaluation 
7. User Input Prediction - After evaluating the model, allow the user to enter values for all 
independent variables (for example: study hours, sleep hours, attendance 
%). - Convert the input values into a 2-D array and use the trained model to 
predict the Performance Index. - Display the predicted result clearly. 
8. Visualization  """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class StudentPerformanceModel:
    def __init__(self, filepath):
        self.filepath = filepath
        self.model = LinearRegression()
        self.rmse = None
        self.X_encoded = None
        self.X_train = None
        self.X_test = None
        self.Y_train = None
        self.Y_test = None
        self.Y_predict = None

    def load_and_preprocess(self):
        data = pd.read_csv(self.filepath)
        X = data.drop(columns="Performance Index")
        Y = data["Performance Index"]
        self.X_encoded = pd.get_dummies(X, drop_first=True)
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(
            self.X_encoded, Y, test_size=0.2, random_state=10
        )

    def train_model(self):
        self.model.fit(self.X_train, self.Y_train)

    def evaluate_model(self):
        self.Y_predict = self.model.predict(self.X_test)
        mse = mean_squared_error(self.Y_test, self.Y_predict)
        self.rmse = np.sqrt(mse)
        r2 = r2_score(self.Y_test, self.Y_predict)

        print("\n--- Model Evaluation ---")
        print(f"Intercept (β₀): {self.model.intercept_:.2f}")
        equation = f"y = {self.model.intercept_:.2f}"
        for i, col in enumerate(self.X_encoded.columns):
            equation += f" + {self.model.coef_[i]:.2f}*{col}"
        print("Model Equation:")
        print(equation)
        print(f"Mean Squared Error (MSE): {mse:.2f}")
        print(f"Root Mean Squared Error (RMSE): {self.rmse:.2f}")
        print(f"R² Score: {r2:.2f}")

    def predict_new(self, input_values):
        new_df = pd.DataFrame([input_values], columns=self.X_encoded.columns)
        prediction = self.model.predict(new_df)[0]
        print("\n--- New Prediction ---")
        print(f"Input: {new_df.values.tolist()[0]}")
        print(f"Predicted Performance Index: {prediction:.2f} ± {self.rmse:.2f}")

    def predict_from_user(self):
        print("\n--- Enter Student Details ---")
        hours_studied = float(input("Hours Studied: "))
        previous_scores = float(input("Previous Scores (out of 100): "))
        sleep_hours = float(input("Average Sleep Hours: "))
        sample_papers = int(input("Sample Papers Practiced: "))
        extracurricular = input("Extracurricular Activities? (Yes/No): ")
        extracurricular_encoded = 1 if extracurricular.lower() == "yes" else 0

        input_values = [hours_studied, previous_scores, sleep_hours, sample_papers, extracurricular_encoded]
        self.predict_new(input_values)

    def plot_actual_vs_predicted(self, feature='Hours Studied'):
        sorted_idx = self.X_test[feature].argsort()
        x_sorted = self.X_test[feature].iloc[sorted_idx]
        y_actual_sorted = self.Y_test.iloc[sorted_idx]
        y_pred_sorted = self.Y_predict[sorted_idx]

        plt.scatter(x_sorted, y_actual_sorted, color='green', label='Actual Performance Index')
        plt.plot(x_sorted, y_pred_sorted, color='blue', label='Predicted Performance Index')
        plt.xlabel(feature)
        plt.ylabel('Performance Index')
        plt.title('Actual vs Predicted Performance Index')
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_prediction_accuracy(self):
        plt.scatter(self.Y_test, self.Y_predict, color='purple', alpha=0.6)
        plt.plot([self.Y_test.min(), self.Y_test.max()], [self.Y_test.min(), self.Y_test.max()],
                 color='black', linestyle='--', label='Perfect Prediction')
        plt.xlabel('Actual Performance Index')
        plt.ylabel('Predicted Performance Index')
        plt.title('Model Accuracy: Actual vs Predicted')
        plt.legend()
        plt.tight_layout()
        plt.show()

def main():
    filepath = "Week9-ML-MultipleLinearRegression\\Home\\Student_Performance.csv"
    model = StudentPerformanceModel(filepath)
    model.load_and_preprocess()
    model.train_model()
    model.evaluate_model()

    # Predict using hardcoded values
    model.predict_new([7, 99, 9, 1, 1])

    # Predict using user input
    model.predict_from_user()

    # Visualizations
    model.plot_actual_vs_predicted()
    model.plot_prediction_accuracy()

if __name__ == "__main__":
    main()