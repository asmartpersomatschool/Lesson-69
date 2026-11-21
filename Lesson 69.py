#You are a part of a survey team trying to analyze the life expectancy of different categories. A dataset of Life Expectancy for different countries for the year 2007 is provided to you. Various features may be a responsible factor for different life expectancies.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "gapminder(2007).csv"
df = pd.read_csv(url)

df_2007 = df[df['year'] == 2007]

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x='gdp_cap',
    y='life_exp',
    hue='continent',
    alpha=0.8,
    s=80
)

plt.title('Relationship Between GDP per Capita and Life Expectancy (2007)', fontsize=14, fontweight='bold')
plt.xlabel('GDP per Capita (USD)', fontsize = 12)
plt.ylabel('Life Expectancy (Years)', fontsize = 12)

plt.tight_layout()
plt.show()