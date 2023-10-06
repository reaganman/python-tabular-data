'''takes a csv file of flower specimines and creates a scatter plot w/ linear
regression of petal length vs sepal length for each species '''


import sys
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats


#get lists of petal and sepal length for species
def get_samples(df, species):
    samples = df[df.species==species]
    x = samples.petal_length_cm
    y = samples.sepal_length_cm
    return (x, y)


#create scatterplot for specified species
def make_plot(df, species):
    samples = get_samples(df, species)
    x = samples[0]
    y = samples[1]
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label='Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel(species+" petal length (cm)")
    plt.ylabel(species+" sepal length (cm)")
    plt.legend()
    plt.savefig(species+" petal_v_sepal_length_regress.png")

if __name__ == '__main__':
    infile = sys.argv[1]
    df = pd.read_csv(infile)
    species = df.species.unique()
    for i in species:
        make_plot(df, i)

#example usage: python3 plot_species.py iris.csv

