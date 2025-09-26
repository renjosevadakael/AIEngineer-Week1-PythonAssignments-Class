""" Assignment Details: 
1. You are provided with the dataset country_wise_latest.csv (from Kaggle’s COVID-19 
Dataset). Build a Python program using classes and inheritance to implement the following 
tasks given in the requirement. 
 
https://www.kaggle.com/datasets/imdevskp/corona-virus-report 
Requirements: 
1. Summarize Case Counts by Region 
o Display total confirmed, death, and recovered cases for each region. 
2. Filter Low Case Records 
o Exclude entries where confirmed cases are < 10. 
3. Identify Region with Highest Confirmed Cases 
4. Sort Data by Confirmed Cases 
o Save sorted dataset into a new CSV file. 
5. Top 5 Countries by Case Count 
6. Region with Lowest Death Count 
7. India’s Case Summary (as of April 29, 2020) 
8. Calculate Mortality Rate by Region 
o Death-to-confirmed case ratio. 
9. Compare Recovery Rates Across Regions 
10. Detect Outliers in Case Counts 
 Use mean ± 2*std deviation. 
11. Group Data by Country and Region 
12. Identify Regions with Zero Recovered Cases  """

import pandas as pd
import os

class CovidCases:
    def __init__(self,country_wise_csv):
        self.dataFrame = pd.read_csv(country_wise_csv)

class CovidAnalysis(CovidCases):
    def __init__(self,country_wise_csv):
       super().__init__(country_wise_csv)
       
    def regionWiseGrouping(self):
       print("\nDisplay total confirmed, death, and recovered cases for each region.\n")
       return self.dataFrame.groupby('WHO Region')[['Confirmed', 'Deaths', 'Recovered']].sum()
    
    def filter_low_record_cases(self):
        print("\n Exclude entries where confirmed cases are < 10. \n")
        return self.dataFrame[(self.dataFrame['Confirmed']>=10)]
    
    def highest_confirmed_cases(self):
        print("\n Identify Region with Highest Confirmed Cases. \n")
        return self.dataFrame.groupby('WHO Region')['Confirmed'].sum().sort_values(ascending=False).head(1)

    def sort_data_confirmed_cases(self):
        print("\n Sort Data by Confirmed Cases \n")
        confirmed_df= self.dataFrame.sort_values('Confirmed')
        confirmed_df.to_csv('confirmedData.csv', index=False)
        return confirmed_df
       # return self.dataFrame.groupby('Country/Region')['Confirmed'].sum().sort_values()

    def top_5_countries_case_count(self):
       all_records_top_5_countries= self.dataFrame.sort_values('Confirmed',ascending=False).head(5)
       #print(all_records_top_5_countries[['Country/Region','Confirmed']].to_string(index=None))
       #return all_records_top_5_countries['Country/Region','Confirmed']
       return all_records_top_5_countries[['Country/Region','Confirmed']]
    
    def  region_with_lowest_death_count(self):
        return self.dataFrame.groupby('WHO Region')['Deaths'].sum().sort_values().head(1)
    
    def  india_case_summary(self):
        return self.dataFrame[self.dataFrame['Country/Region']=='India'] 
   
    def mortality_rate_by_region(self):
        grouped = self.dataFrame.groupby('WHO Region')[['Confirmed', 'Deaths']].sum()
        #print(grouped)
        grouped['Mortality Rate (%)'] = (grouped['Deaths'] / grouped['Confirmed']) * 100
        #print(grouped['Mortality Rate (%)'] )
        return grouped[['Mortality Rate (%)']].sort_values('Mortality Rate (%)')
    
    def compare_recovery_rate_across_region(self):
        grouped = self.dataFrame.groupby('WHO Region')[['Confirmed', 'Recovered']].sum()
        grouped['Recovery Rate (%)'] = (grouped['Recovered'] / grouped['Confirmed']) * 100
        return grouped[['Recovery Rate (%)']].sort_values(by='Recovery Rate (%)',ascending=True)
    
    #def group_by_country_region(self):
        #print(self.dataFrame.groupby(['Country/Region','WHO Region'])['Confirmed'].sum())

    def group_by_country_and_region(self):
        grouped = self.dataFrame.groupby(['Country/Region', 'WHO Region'])[['Confirmed', 'Deaths', 'Recovered']].sum()
        return grouped.sort_values(by='Confirmed', ascending=False)
    
    def region_with_zero_recovered_cases(self):
        recovered_sum = self.dataFrame.groupby('Country/Region')['Recovered'].sum()
        zero_recovered = recovered_sum[recovered_sum == 0]
        print(zero_recovered)
   
   
    


if __name__ == "__main__":
    covid = CovidAnalysis("C:\\AIEngineer\\Class1_Python\\Week4\\Home\\country_wise_latest.csv")
    print("1. Case Summary by Region:\n", covid.regionWiseGrouping())
    print("2. Filter Low Case Records:\n", covid.filter_low_record_cases())
    print("3. Identify Region with Highest Confirmed Cases:\n", covid.highest_confirmed_cases())
    print("4. Sort Data by Confirmed Cases and Write to File \n " , covid.sort_data_confirmed_cases() )
  
    print("5. Top 5 Countries by Case Count \n" ,covid.top_5_countries_case_count())
 
    print("6. Region with Lowest Death Count \n",covid.region_with_lowest_death_count())
        
    print("7. India’s Case Summary (as of April 29, 2020) \n", covid.india_case_summary()) 

    print("8. Calculate Mortality Rate by Region  \n",covid.mortality_rate_by_region()) 
    print("9. Compare Recovery Rates Across Regions \n", covid.compare_recovery_rate_across_region())
    print("11 . Group Data by Country and Region \n",covid.group_by_country_and_region())
    print("12. Identify Regions with Zero Recovered Cases", covid.region_with_zero_recovered_cases())

    
    


   


