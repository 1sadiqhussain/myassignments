import pandas as pd # This command imports the pandas library as pd
import matplotlib.pyplot as plt # This command imports the matplotlib.pyplot library as plt
IndianEconomy= pd.read_csv('IndianEconomy.csv') # read_csv() command reads the csv file

# Graph 1 - Line Graph
# Plotting the line Graph for Imports and Exports of Goods and Services (% of GDP)
def linegraph():
    plt.figure() # figure() command Creates a figure
    plt.plot(IndianEconomy["Year"],IndianEconomy["Imports of goods and services (% of GDP)"],label="Imports of goods and services (% of GDP)",color='green') # In this command we are plotting the line graph of Imports of goods and services (% of GDP) defining the label and color of the graph
    plt.plot(IndianEconomy["Year"],IndianEconomy["Exports of goods and services (% of GDP)"],label="Exports of goods and services(% of GDP)",color='red') # # In this command we are plotting the line graph of Exports of goods and services (% of GDP) defining the label and color of the graph
    plt.savefig('linegraph.png') # savefig() command saves the graph
    plt.title('Indian Imports and Exports of goods and services (% of GDP)') # title() command gives the title of the graph
    plt.xlabel('Year') # xlabel() command defines the X-Axis name of the graph
    plt.ylabel('Import of goods and services Data') # ylabel() command defines the Y-Axis name of the graph
    plt.legend() # legend() command shows the index values on the graph
    plt.show() # show() command shows the plotted graph

# Graph 2 - Scatter plot
# Plotting the Scatterplot for GDP per capita (US$)
def scatterplot():
    plt.figure() # This command creates a figure
    IndianEconomy.plot.scatter(x = 'Year', y = 'GDP per capita (US$)',c="Green") # We are creating the scatter plot and menctioning the Year and Y - Axis as GDP per capita (US$) and defining the color
    plt.title('GDP per capita (US$) - SCATTER PLOT') # title() are defining the title of the graph
    plt.xlabel('Year') # xlabel() command defines the name of the X-Axis
    plt.ylabel('GDP per capita (US$)') # ylabel() command defines the name of the Y-Axis
    plt.legend(["GDP per capita (US$)"]) # legend() command shows the index on the Graph
    plt.savefig('scatterplot.png') # savefig() command saves the graph
    plt.show() # show() command shows the graph

# Graph 3 - Box plot
# Plotting the boxplot for GDP Growth (annual %)
def boxplot():
    plt.figure() # figure() command creates a figure
    dataforboxplot=IndianEconomy['GDP Growth (annual %)'] # We are defining the data for boxplot
    plt.boxplot(dataforboxplot) # Plotting the boxplot
    plt.savefig('Box plot.png') # savefig() command saves a copy of the graph
    plt.title('GDP Growth (annual %)') # title() command creates the title of the Graph
    plt.legend(['GDP Growth (annual %)']) # legend() command creates a index figure on the graph
    plt.show() # show() command shows the plot 


linegraph() # calling the lingraph function
scatterplot() # calling the scatterplot function
boxplot() # calling the boxplot function 
