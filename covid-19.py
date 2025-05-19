# COVID-19 Data Analyzer

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv(r"C:\Users\Amit kumar\Desktop\covid.csv")

# Data Processing
data['Date'] = pd.to_datetime(data['Date'])
data['Recovered'] = data['Recovered']  # Correcting the column name

# Exploratory Data Analysis
# Summary statistics
summary = data.describe()

# Confirmed cases over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='Date', y='Confirmed', hue='State')
plt.title('Confirmed COVID-19 Cases Over Time by State')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=45)
plt.legend(title='State')
plt.tight_layout()
plt.show()

# Deaths over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='Date', y='Deaths', hue='State')
plt.title('COVID-19 Deaths Over Time by State')
plt.xlabel('Date')
plt.ylabel('Deaths')
plt.xticks(rotation=45)
plt.legend(title='State')
plt.tight_layout()
plt.show()

# Recoveries over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='Date', y='Recovered', hue='State')
plt.title('COVID-19 Recoveries Over Time by State')
plt.xlabel('Date')
plt.ylabel('Recoveries')
plt.xticks(rotation=45)
plt.legend(title='State')
plt.tight_layout()
plt.show()
