import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from plotly.offline import iplot

df = pd.read_csv('world-happiness-report-2021.csv')

print(df.head())

print(df.shape)

# Plotting pairwise relationships in the data set

sns.pairplot(df)

plt.show()

# Top 10 countries for each attribute



fig, axes = plt.subplots(nrows=2, ncols=2,constrained_layout=True,figsize=(12,8))

sns.barplot(x='GDP per capita',y='Country name',data=df.nlargest(10,'GDP per capita'),ax=axes[0,0],palette="Blues_d")

sns.barplot(x='Social support' ,y='Country name',data=df.nlargest(10,'Social support'),ax=axes[0,1],palette="YlGn")

sns.barplot(x='Healthy life expectancy' ,y='Country name',data=df.nlargest(10,'Healthy life expectancy'),ax=axes[1,0],palette='OrRd')

sns.barplot(x='Freedom to make life choices' ,y='Country name',data=df.nlargest(10,'Freedom to make life choices'),ax=axes[1,1],palette='YlOrBr')



plt.show()



fig, axes = plt.subplots(nrows=1, ncols=2,constrained_layout=True,figsize=(10,4))

sns.barplot(x='Generosity' ,y='Country name',data=df.nlargest(10,'Generosity'),ax=axes[0],palette='Spectral')
sns.barplot(x='Perceptions of corruption' ,y='Country name',data=df.nlargest(10,'Perceptions of corruption'),ax=axes[1],palette='RdYlGn')


plt.show()

print('Maximum Score :', df['Score'].max())
print('Minimum Score:', df['Score'].min())
add = df['Score'].max() - df['Score'].min()
grp = round(add / 3, 3)
print('Difference in Range(1-3):', (grp))

low = df['Score'].min() + grp
mid = low + grp

print('Upper bound of Low grp', low)
print('Upper bound of Mid grp', mid)
print('Upper bound of High grp', 'max:', df['Score'].max())

# df.info()

cat = []
for i in df.Score:
    if (i > 0 and i < low):
        cat.append('Low')


    elif (i > low and i < mid):
        cat.append('Mid')
    else:
        cat.append('High')

df['Category'] = cat

color = (df.Category == 'High').map({True: 'background-color: limegreen', False: 'background-color: red'})
df.style.apply(lambda s: color)

print(df.loc[df['Country name'] == 'Pakistan'])

data = {
    'Country name': ['Canada', 'US', 'UK', 'Pakistan'],
    'Score': [7.103, 6.951, 7.064, 4.934],
    'GDP per capita': [1.447, 1.533, 1.423, 0.637],
    'Social support': [1.044, 1.03, 1.062, 0.423],
    'Healthy life expectancy': [0.798, 0.621, 0.757, 0.322],
    'Freedom to make life choices': [0.648, 0.554, 0.58, 0.418],
    'Generosity': [0.246, 0.252, 0.34, 0.252],
    'Perceptions of corruption': [0.335, 0.154, 0.306, 0.097]
}
d = pd.DataFrame(data)
print(d)

ax = d.plot(y="GDP per capita", x="Country name", kind="bar",  color='C1')
d.plot(y="Social support", x="Country name", kind="bar",ax=ax, color="C3")
d.plot(y="Healthy life expectancy", x="Country name", kind="bar", ax=ax, color="C2")

plt.show()

ax = d.plot(y="Freedom to make life choices", x="Country name", kind="bar", color='C3')
d.plot(y="Generosity", x="Country name", kind="bar", ax=ax, color="C1")
d.plot(y="Perceptions of corruption", x="Country name", kind="bar", ax=ax, color="C2", )

plt.show()

data = dict(type='choropleth',
            locations=df['Country name'],
            locationmode='country names',
            colorscale='RdYlGn',
            z=df['Score'],
            text=df['Country name'],
            colorbar={'title': 'Happiness Score'})

layout = dict(title='Geographical Visualization of Happiness Score',
              geo=dict(showframe=True, projection={'type': 'azimuthal equal area'}))

choromap3 = go.Figure(data=[data], layout=layout)
iplot(choromap3)
