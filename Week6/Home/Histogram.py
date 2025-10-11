import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("C:\\AIEngineer\\Class1_Python\\Week6\\Home\\country_wise_latest.csv")

# Keep only the relevant columns
df_selected = df[['Confirmed', 'New cases']]
scaler = StandardScaler()
normalized_values = scaler.fit_transform(df_selected)

# Create a normalized DataFrame
df_normalized = pd.DataFrame(normalized_values, columns=['Confirmed', 'New cases'])
# Create a 2x2 grid for before and after normalization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Original: Confirmed
sns.histplot(df_selected['Confirmed'], bins=20, kde=True, ax=axes[0, 0], color='skyblue')
axes[0, 0].set_title('Original: Confirmed Cases')

# Original: New Cases
sns.histplot(df_selected['New cases'], bins=20, kde=True, ax=axes[0, 1], color='salmon')
axes[0, 1].set_title('Original: New Cases')

# Normalized: Confirmed
sns.histplot(df_normalized['Confirmed'], bins=20, kde=True, ax=axes[1, 0], color='skyblue')
axes[1, 0].set_title('Normalized: Confirmed Cases')

# Normalized: New Cases
sns.histplot(df_normalized['New cases'], bins=20, kde=True, ax=axes[1, 1], color='salmon')
axes[1, 1].set_title('Normalized: New Cases')

plt.tight_layout()
plt.savefig('seaborn_histograms.png')


plt.figure(figsize=(6, 4))

sns.heatmap(df[['Confirmed', 'New cases']].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap: Confirmed vs New Cases')
plt.savefig('seaborn_heatmap.png')
plt.close()


