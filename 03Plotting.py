# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:15:55 2021

@author: ed006315
"""

#%matplotlib inline
#%config InlineBackend.figure_formats = {'png', 'retina'}
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set custom white background
sns.set_context("notebook", font_scale=1.2, rc={"lines.linewidth": 1.2})
custom_style = {
            'grid.color': '0.8',
            'grid.linestyle': '--',
            'grid.linewidth': 0.5,
}
sns.set_style("whitegrid", custom_style)

def label_positioning(y):
    initpos = {column: df[column].values[-1] - 0.5 for column in y}
    sortedpos = sorted(initpos.items(),key=lambda x:x[1], reverse=True)
    for i in range(len(y)-1):
        diff = sortedpos[i][1] - sortedpos[i+1][1]
        if diff < 2.5:
            initpos[sortedpos[i][0]] += (2.5 - diff) / 3
            initpos[sortedpos[i+1][0]] -= (2.5 - diff) / 1.7
            sortedpos = sorted(initpos.items(),key=lambda x:x[1], reverse=True)
    return initpos

df = pd.read_csv("https://raw.githubusercontent.com/maxberggren/legend-right/master/percent-bachelors-degrees-women-usa.csv")

x = 'Year'
y = df.drop('Year', axis=1).columns
positions = label_positioning(y)

f, ax = plt.subplots(figsize=(8,11))
cmap = plt.cm.get_cmap('tab20', len(y))

plt.yticks(range(0, 91, 10), [str(x) + "%" for x in range(0, 91, 10)], fontsize=14)
plt.xticks(fontsize=14)

for i, (column, position) in enumerate(positions.items()):

    # Get a color
    color = cmap(float(i)/len(positions))
    # Plot each line separatly so we can be explicit about color
    ax = df.plot(x=x, y=column, legend=False, ax=ax, color=color)

    # Add the text to the right
    plt.text(
        df[x][df[column].last_valid_index()] + 0.5,
        position, column, fontsize=12,
        color=color # Same color as line
    )

ax.set_ylabel('Female bachelor degrees')
# Add percent signs
ax.set_yticklabels(['{:3.0f}%'.format(x) for x in ax.get_yticks()])
sns.despine()


# matplotlib's title() call centers the title on the plot, but not the graph,
# so I used the text() call to customize where the title goes.

# Make the title big enough so it spans the entire plot, but don't make it
# so big that it requires two lines to show.

# Note that if the title is descriptive enough, it is unnecessary to include
# axis labels; they are self-evident, in this plot's case.
plt.text(1995, 93, "Percentage of Bachelor's degrees conferred to women in the U.S.A."
        ", by major (1970-2012)", fontsize=17, ha="center")

# Always include your data source(s) and copyright notice! And for your
# data sources, tell your viewers exactly where the data came from,
# preferably with a direct link to the data. Just telling your viewers
# that you used data from the "U.S. Census Bureau" is completely useless:
# the U.S. Census Bureau provides all kinds of data, so how are your
# viewers supposed to know which data set you used?
plt.text(1964, -15, "Data source: nces.ed.gov/programs/digest/2013menu_tables.asp"
        "\nAuthor: Randy Olson (randalolson.com / @randal_olson)"
        "\nNote: Some majors are missing because the historical data "
        "is not available for them", fontsize=10)

# Finally, save the figure as a PNG.
# You can also save it as a PDF, JPEG, etc.
# bbox_inches="tight" removes all the extra whitespace on the edges of your plot.
plt.savefig("percent-bachelors-degrees-women-usa.png", bbox_inches="tight")
