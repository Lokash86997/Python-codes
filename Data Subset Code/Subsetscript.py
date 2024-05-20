import gzip
import shutil
import pandas as pd

print("Paste file path without quotation marks ")

#input of file path
file_path = input("File path: ")

#code the extracts the file and make a copy of the data as a txt file
with gzip.open(file_path, 'rb') as f_in:
    with open('data.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

#add the data.txt file as a dataframe
data = pd.read_table("data.txt",header=None, sep='\t')

#input of the query/sample
sample = input('Sample: ')

#check if query typed in is in the data file
check = sample in data.values
if check != True:
    print("Your sample is not present in the data! ")

#creating a subset dataframe with associated sample
subset = data[data[0]==sample]

#making the new dataframe into a txt file and compressing it into gzip file
subset.to_csv('subset.txt', sep='\t', index=False, header=None)
with open('subset.txt', 'rb') as f_in, gzip.open('subset.txt.gz', 'wb') as f_out:
    f_out.writelines(f_in)