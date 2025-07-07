
# Implementation for Zomato Data Analysis Using python

# Importing necessary python libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# creating data frame
dataframe = pd.read_csv(r"C:/Users/kendr/OneDrive/Desktop/Zomato-data-.csv")
print(dataframe.head())

#Data cleaning and preparation
def handleRate(value):
    try:
      value = str(value).split('/')[0].strip()
      return float(value)
    except:
      return np.nan

dataframe['rate'] = dataframe['rate'].apply(handleRate)
print(dataframe.head())

#Getting summary of the dataframe use df.info()
dataframe.info()

# Exploring restaurant types
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#votes by restaurant type
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes' : grouped_data})
result.plot(kind= 'line', color='green', marker= 'o')
plt.xlabel('Type of restaurant', color= 'purple', size=12)
plt.ylabel('Votes', color='red', size=12)
plt.xticks(rotation = 45)
plt.title('Votes by Restaurant Type')
plt.tight_layout()
plt.show()

# Identity the most voted restaurant 
max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes,'name']
print('Restaurant(s) with the maximun votes:')
print(restaurant_with_max_votes)

# Online order availability
sns.countplot(x=dataframe['online_order'])
plt.title('online order Availability')
plt.show()

#Analyze ratings 
plt.hist(dataframe['rate'].dropna(), bins=5, edgecolor='black')
plt.title('Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Approximate cost for couples
dataframe['approx_cost(for two people)'] = dataframe['approx_cost(for two people)'].replace(',','', regex= True)
dataframe['approx_cost(for two people)'] = pd.to_numeric(dataframe['approx_cost(for two people)'], errors='coerce')

sns.histplot(dataframe['approx_cost(for two people)'].dropna(), bins=15)
plt.title('Approximate cost for two people')
plt.xlabel('cost')
plt.show()

# Ratings comparison - online vs offline orders
plt.figure(figsize=(6,6))
sns.boxplot(x = 'online_order', y= 'rate', data = dataframe)
plt.title('Rating: online Order vs Offline')
plt.show()

#Order mode preferences by Restaurant type
pivot_table = dataframe.pivot_table(index='listed_in(type)', columns = 'online_order',aggfunc='size',fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Heatmap: Order Preferenace by Type')
plt.xlabel('Online Order')
plt.ylabel('Restaurant Type')
plt.xticks(rotation = 0)
plt.yticks(rotation = 0)
plt.tight_layout()
plt.show()





                                    

