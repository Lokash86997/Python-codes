# Code to calculate mutation rate
import pandas as pd

# Importing the subset of data as a dataframe
data = pd.read_table("subset.txt", header=None, sep="\t")

# Making a smaller subset with only ncl reads to calculate total reads
nclreads = data[12]

# Splitting nclreads by ';' to get a dataframe with all the different reads
nclreads = nclreads.str.split(";", expand=True)

# Converting the data type to string
nclreads = nclreads.astype('string')

# Replacing empty values in the dataframe as Nan
nclreads.dropna()

# For loop to go through all the columns to replace '---' and '+++' with a 2 character string
# so string slice will only produce numbers
# Its possible to use str.replace for all the columns instead of str.slice but str.slice makes the code shorter
# For example using str.replace('A:', '') Which removes the A: and just gives only the number value
for i in range(0, 10):
    nclreads[i] = nclreads[i].str.replace('---:','-:').str.replace('+++:','+:')
    nclreads[i] = nclreads[i].str.slice(2)

# Making a new column with the added up values of the rows
# Also I use data type float because NaN data type works with float
nclreads['Sum_of_row'] = nclreads.astype('float').sum(axis = 1)

# Calculating and making a new column with the mutation rate
nclreads['Mut_rate'] = data[8] / nclreads['Sum_of_row']

print(nclreads)