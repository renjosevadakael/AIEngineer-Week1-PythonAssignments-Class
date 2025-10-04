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
import matplotlib.pyplot as plt


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

    def detect_outliers_case_count_2(self):
        mean_val = self.dataFrame["Confirmed"].mean()
        std_val  = self.dataFrame["Confirmed"].std()
        lower_bound = mean_val - 2*std_val
        upper_bound = mean_val + 2*std_val

        outliers = self.dataFrame[(self.dataFrame["Confirmed"] < lower_bound) | (self.dataFrame["Confirmed"] > upper_bound)]
        print("Outliers in Confirmed Cases:")
        print(outliers)

class CovidVisualization(CovidAnalysis):
    def __init__(self, country_wise_csv):
        super().__init__(country_wise_csv)

    def bar_top10_confirmed(self):
        top10 = self.dataFrame.groupby('Country/Region')['Confirmed'].sum().nlargest(10)
        plt.figure(figsize=(10,6))
        plt.barh(top10.index, top10.values, color='tomato')
        plt.xlabel('Confirmed Cases')
        plt.title('Top 10 Countries by Confirmed Cases')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.show()

    def pie_death_distribution_by_region(self):
        region_deaths = self.dataFrame.groupby('WHO Region')['Deaths'].sum()
        plt.figure(figsize=(8,8))
        plt.pie(region_deaths, labels=region_deaths.index, autopct='%1.1f%%', startangle=140)
        plt.title('Global Death Distribution by Region')
        plt.tight_layout()
        plt.show()

    def line_confirmed_vs_deaths_top5(self):
        top5 = self.dataFrame.groupby('Country/Region')['Confirmed'].sum().nlargest(5).index
        plt.figure(figsize=(12,6))
        for country in top5:
            confirmed = self.dataFrame[self.dataFrame['Country/Region'] == country]['Confirmed'].values[0]
            deaths = self.dataFrame[self.dataFrame['Country/Region'] == country]['Deaths'].values[0]
            plt.plot([0, 1], [0, confirmed], label=f'{country} - Confirmed')
            plt.plot([0, 1], [0, deaths], linestyle='--', label=f'{country} - Deaths')
        plt.title('Confirmed vs Deaths - Top 5 Countries')
        plt.ylabel('Cases')
        plt.legend()
        plt.tight_layout()
        plt.show()

    def scatter_confirmed_vs_recovered(self):
        plt.figure(figsize=(10,6))
        plt.scatter(self.dataFrame['Confirmed'], self.dataFrame['Recovered'], alpha=0.6, c='green')
        plt.xlabel('Confirmed Cases')
        plt.ylabel('Recovered Cases')
        plt.title('Confirmed vs Recovered Cases')
        plt.tight_layout()
        plt.show()

    def histogram_deaths_by_region(self):
        plt.figure(figsize=(10,6))
        for region in self.dataFrame['WHO Region'].unique():
            subset = self.dataFrame[self.dataFrame['WHO Region'] == region]
            plt.hist(subset['Deaths'], bins=30, alpha=0.5, label=region)
        plt.title('Histogram of Death Counts by Region')
        plt.xlabel('Deaths')
        plt.ylabel('Frequency')
        plt.legend()
        plt.tight_layout()
        plt.show()

    def stacked_bar_selected_countries(self, countries):
        subset = self.dataFrame[self.dataFrame['Country/Region'].isin(countries)]
        confirmed = subset.set_index('Country/Region')['Confirmed']
        deaths = subset.set_index('Country/Region')['Deaths']
        recovered = subset.set_index('Country/Region')['Recovered']

        plt.figure(figsize=(10,6))
        plt.bar(confirmed.index, confirmed.values, label='Confirmed', color='orange')
        plt.bar(deaths.index, deaths.values, bottom=confirmed.values, label='Deaths', color='red')
        plt.bar(recovered.index, recovered.values, bottom=confirmed.values + deaths.values, label='Recovered', color='green')
        plt.title('Stacked Bar Chart: Confirmed, Deaths, Recovered')
        plt.ylabel('Cases')
        plt.legend()
        plt.tight_layout()
        plt.show()

    def boxplot_confirmed_by_region(self):
        regions = self.dataFrame['WHO Region'].unique()
        data = [self.dataFrame[self.dataFrame['WHO Region'] == region]['Confirmed'] for region in regions]
        plt.figure(figsize=(10,6))
        plt.boxplot(data, labels=regions)
        plt.title('Box Plot of Confirmed Cases by Region')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def trendline_india_vs_country(self, other_country):
        countries = ['India', other_country]
        plt.figure(figsize=(10,6))
        for country in countries:
            confirmed = self.dataFrame[self.dataFrame['Country/Region'] == country]['Confirmed'].values[0]
            plt.plot([0, 1], [0, confirmed], label=country)
        plt.title(f'Trend Line: India vs {other_country}')
        plt.ylabel('Confirmed Cases')
        plt.legend()
        plt.tight_layout()
        plt.show()

   
   
    


if __name__ == "__main__":
    covid_viz = CovidVisualization("C:\\AIEngineer\\Class1_Python\\Week4\\Home\\country_wise_latest.csv")
    print("1. Case Summary by Region:\n", covid_viz.regionWiseGrouping())
    print("2. Filter Low Case Records:\n", covid_viz.filter_low_record_cases())
    print("3. Identify Region with Highest Confirmed Cases:\n", covid_viz.highest_confirmed_cases())
    print("4. Sort Data by Confirmed Cases and Write to File \n " , covid_viz.sort_data_confirmed_cases() )
  
    print("5. Top 5 Countries by Case Count \n" ,covid_viz.top_5_countries_case_count())
 
    print("6. Region with Lowest Death Count \n",covid_viz.region_with_lowest_death_count())
        
    print("7. India’s Case Summary (as of April 29, 2020) \n", covid_viz.india_case_summary()) 

    print("8. Calculate Mortality Rate by Region  \n",covid_viz.mortality_rate_by_region()) 
    print("9. Compare Recovery Rates Across Regions \n", covid_viz.compare_recovery_rate_across_region())
    print("10. Detect Outliers in Case Counts :: Use mean ± 2*std deviation.")
    covid_viz.detect_outliers_case_count_2()
    print("11 . Group Data by Country and Region \n",covid_viz.group_by_country_and_region())
    print("12. Identify Regions with Zero Recovered Cases", covid_viz.region_with_zero_recovered_cases())

    
    
    # Visualization Tasks
    covid_viz.bar_top10_confirmed()
    covid_viz.pie_death_distribution_by_region()
    covid_viz.line_confirmed_vs_deaths_top5()
    covid_viz.scatter_confirmed_vs_recovered()
    covid_viz.histogram_deaths_by_region()
    covid_viz.stacked_bar_selected_countries(['India', 'US', 'Brazil', 'Russia', 'UK'])
    covid_viz.boxplot_confirmed_by_region()
    covid_viz.trendline_india_vs_country('US')


   


