#%%
medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
from urllib.request import urlretrieve
urlretrieve(medical_charges_url,'medical.csv')

import pandas as pd
medical_df = pd.read_csv('medical.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(medical_df)
print(medical_df.head())
print(medical_df.info())
print(medical_df.describe())
# %%
import jovian
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
print("Howdi!!??")

# %%
print(medical_df.age.describe())
plt.show()

# %%
fig = px.histogram(medical_df, x='age', marginal='box', nbins=47, title='Distribution of Age')
fig.update_layout(bargap=0.1)
fig.show()
# %%
fig = px.histogram(medical_df, x='bmi', marginal='box', color_discrete_sequence=['red'], title='Distribution of BMI (Body Mass Index)')
fig.update_layout(bargap=0.1)
fig.show()
# %%
fig = px.histogram(medical_df, x='charges', marginal='box', color='smoker', color_discrete_sequence=['green', 'grey'], title='Annual Medical Charges')
fig.update_layout(bargap=0.1)
fig.show()

# %%
medical_df.smoker.value_counts()
px.histogram(medical_df, x='smoker', color='sex', title='Smoker')
# %%
fig = px.scatter(medical_df, x = 'age', y = 'charges', color = 'smoker', opacity = 0.8, hover_data = ['sex'], title = 'Age vs Charges')
fig.update_traces(marker_size = 5)
fig.show()
# %%
fig = px.scatter(medical_df, x='bmi', y='charges', color='smoker', opacity=0.8, hover_data=['sex'], title='BMI vs. Charges')
fig.update_traces(marker_size=5)
fig.show()
# %%
px.violin(medical_df, x = 'children', y = 'charges')
# %%
medical_df.charges.corr(medical_df.age)
# %%
medical_df.charges.corr(medical_df.bmi)
# %%
medical_df.charges.corr(medical_df.children)
# %%
smoker_values = {'no': 0, 'yes': 1}
smoker_numeric = medical_df.smoker.map(smoker_values)
smoker_numeric
# %%
medical_df.smoker
# %%
medical_df.charges.corr(smoker_numeric)
# %%
medical_df[['age', 'bmi', 'children', 'charges']].corr()
# medical_df.corr(), but it will give an error because of the non-numeric columns
# %%
px.scatter(medical_df, x = 'age', y = 'age')
# %%
sns.heatmap(medical_df[['age', 'bmi', 'children', 'charges']].corr(), cmap = 'Reds', annot = True)
plt.title('Correlation Heatmap')

# %%
#LINEAR REGRESSION USING A SINGLE FEATURE
non_smoker_df = medical_df[medical_df.smoker == 'no']
# %%
plt.title('Age vs. Charges')
sns.scatterplot(data=non_smoker_df, x='age', y='charges', alpha=0.7, s=15)
# %%
def estimate_charges(age, w, b):
    return w * age + b
# %%
w = 50
b = 100
# %%
estimate_charges(0, w, b)
# %%
ages = non_smoker_df.age
ages
# %%
estimate_charges = estimate_charges(ages, w, b)

# %%
estimate_charges
# %%
non_smoker_df.charges
# %%
plt.plot(ages, estimate_charges,'r-')
plt.xlabel('Age')
plt.ylabel('Estimated Charges')
# %%
target = non_smoker_df.charges
plt.plot(ages, estimate_charges, 'r', alpha = 0.9)
plt.scatter(ages, target, s = 8, alpha = 0.8)
plt.xlabel('Age')
plt.ylabel('Charges')
plt.legend(['Estimated Charges', 'Actual Charges'])
# %%
def try_parameters(w, b):
    ages = non_smoker_df.age
    target = non_smoker_df.charges
    estimated_charges = estimate_charges(ages, w, b)
    plt.plot(ages, estimate_charges, 'r', alpha = 0.9)
    plt.scatter(ages, target, s = 9, alpha = 0.8)
    plt.xlabel('Age')
    plt.ylabel('Charges')
    plt.legend(['Estimate', 'Actual'])
# %%
try_parameters(60, 200)
# %%
