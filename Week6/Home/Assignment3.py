""" Use the existing COVID-19 dataset (country_wise_latest.csv) and focus on the 
following two numerical features: 
 Confirmed Cases 
 New Cases 
You are required to perform the following tasks step-by-step: 
1. Create a class CovidEDA to perform the below operations. 
o Load the dataset using Pandas. 
o Keep only the columns Confirmed and New cases for analysis. 
2. Compute Statistical Measures 
o Calculate and print: 
 Mean 
 Median 
 Variance 
 Standard Deviation 
 Correlation Matrix (between Confirmed and New cases) 
3. Outlier Detection using IQR Technique 
o Identify outliers in both Confirmed and New cases. 
o Remove the outliers and store the cleaned data in a new DataFrame. 
o Display the cleaned dataset. 
4. Normalization using Standard Scaler 
o Apply StandardScaler from sklearn.preprocessing to normalize the 
Confirmed and New Cases. 
o Display the scaled (normalized) output as a new DataFrame. 
5. Visualization Tasks 
o Plot Histograms for Confirmed and New cases (before and after 
normalization) using Seaborn, to visualize the bell curve. 
o Plot a Heatmap between Confirmed and New cases to display their 
correlation visually.  """

import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sns





class CovidEDA:
    def __init__(self,country_wise_csv):
        self.dataFrame = pd.read_csv(country_wise_csv)
        self.df_columns=['Confirmed' , 'New cases']
        self.analysis_df = self.dataFrame[self.df_columns]

    def printDataSet(self):
        return self.dataFrame[self.df_columns]
    def mean(self):
        df_mean= self.dataFrame[self.df_columns].mean()
        return df_mean
    def variance(self):
        df_variance= self.dataFrame[self.df_columns].var()
        return df_variance
    def median(self):
        df_median= self.dataFrame[self.df_columns].median()
        return df_median
    def stddev(self):
        df_stddev= self.dataFrame[self.df_columns].std()
        return df_stddev
    def corelation(self):
        return self.dataFrame[self.df_columns[0]].corr( self.dataFrame[self.df_columns[1]])
    def correlation_matrix(self):
         return self.analysis_df.corr()

    def outlierdetectionIQRCleaned(self):
        Q1= self.dataFrame[self.df_columns].quantile(0.25)
        Q3= self.dataFrame[self.df_columns].quantile(0.75)
        IQR = Q3 - Q1
        lower_outlier = Q1 - 1.5 * IQR
        print("lower_outlier" ,lower_outlier)
        upper_outlier = Q3 + 1.5 * IQR
        print("upper_outlier" ,upper_outlier)
        # Extract outliers
        mask = pd.DataFrame(False, index=self.analysis_df.index, columns=self.df_columns)
        for col in self.df_columns:
            mask[col] = (self.analysis_df[col] < lower_outlier[col]) | (self.analysis_df[col] > upper_outlier[col])
        outlier_rows = mask.any(axis=1)
        # With Outliers
        outliers = self.analysis_df[outlier_rows]
        #Remove the outliers and store the cleaned data in a new DataFrame. 
        self.cleaned_df = self.analysis_df[~outlier_rows]
        return  self.cleaned_df
    
    def normalize_standard_scaler(self):
        scaler = StandardScaler()
        # Fit and transform the selected columns
        scaled_values = scaler.fit_transform(self.analysis_df)
        # Create a new DataFrame with normalized values
        self.normalized_df = pd.DataFrame(scaled_values, columns=self.df_columns, index=self.analysis_df.index)
        return self.normalized_df
    
    def plot_histograms_seaborn(self):
        normalized_df = self.normalize_standard_scaler()

        # Original data
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        #sns.histplot(self.df_columns['Confirmed'], bins=20, kde=True, ax=axes[0], color='skyblue')
        sns.histplot(self.dataFrame['Confirmed'], bins=20, kde=True, ax=axes[0], color='skyblue')
        axes[0].set_title('Original: Confirmed Cases')
       # sns.histplot(self.df_columns['New cases'], bins=20, kde=True, ax=axes[1], color='salmon')
        sns.histplot(self.dataFrame['New cases'], bins=20, kde=True, ax=axes[1], color='salmon')
        axes[1].set_title('Original: New Cases')
        plt.tight_layout()
        plt.savefig('seaborn_histograms_original.png')
        plt.close()

        # Normalized data
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        sns.histplot(normalized_df['Confirmed'], bins=20, kde=True, ax=axes[0], color='skyblue')
        axes[0].set_title('Normalized: Confirmed Cases')
        sns.histplot(normalized_df['New cases'], bins=20, kde=True, ax=axes[1], color='salmon')
        axes[1].set_title('Normalized: New Cases')
        plt.tight_layout()
        plt.savefig('seaborn_histograms_normalized.png')
        plt.close()

   
    def plot_heatmap_seaborn(self):
        plt.figure(figsize=(6, 4))
        sns.heatmap(self.analysis_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Heatmap: Confirmed vs New Cases')
        plt.savefig('seaborn_heatmap.png')
        plt.close()

     
 




if __name__ == "__main__":
    covid_eda = CovidEDA("C:\\AIEngineer\\Class1_Python\\Week6\\Home\\country_wise_latest.csv")
    print("1. Print with 2 Cols - Confirmed and New cases\n", covid_eda.printDataSet())
    print("2. Compute Statistical Measures -  Mean :\n", covid_eda.mean())
    print("2. Compute Statistical Measures -  Median :\n", covid_eda.median())
    print("2. Compute Statistical Measures -  Variance :\n", covid_eda.variance())
    print("2. Compute Statistical Measures -  StdDev :\n", covid_eda.stddev())
    print("2. Compute Statistical Measures -  Corelation :\n", covid_eda.corelation())
    print("2. Compute Statistical Measures -  Corelation MAtrix:\n", covid_eda.correlation_matrix())
    print("3.  Outlier Detection using IQR Technique :\n",covid_eda.outlierdetectionIQRCleaned())
    print("4. normalize_standard_scaler \n", covid_eda.normalize_standard_scaler())
    covid_eda.plot_histograms_seaborn()
    covid_eda.plot_heatmap_seaborn()
    print("5. Visualizations saved: seaborn_histograms_original.png, seaborn_histograms_normalized.png, seaborn_heatmap.png")





