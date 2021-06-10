import os
import argparse

parser = argparse.ArgumentParser("This script parses amber mdout files to extract the total energy")
parser=add.argument("filepath", help="The filepath to the file to be analyzed")

filename = os.path.join('data','03_Prod.mdout')
f = open(filename,'r')
data = f.readlines()
f.close()

# 03_Prod.mdout
# 03_Prod.Etot.txt

output_filename = os.path.basename(filename)
output_filename = output_filename.split('.')[0]
output_filename = F"{output filename}_Etot.txt"

f_write = open(F"Writing output to {output_filename}")

f_write= open(output_filename, 'w+')
energies= []

for line in data:
    if 'Etot' in line:
        split_line = line.split()
        f_write.write(split_line[2])
        
f_write.close()

print(f"Done analyzying {filename}")