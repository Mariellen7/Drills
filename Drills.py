import csv 
import pandas as pd
df = pd.DataFrame()

#Adds a new empty column to the csv file
with open('table1.csv', 'r') as f:
        reader = csv.reader (f)
        rows = list(reader)

for row in rows:
        columns = len(rows)
        row.append(range(1, columns))

with open('DrillOutput.csv', 'w', newline='') as f:
          writer=csv.writer(f)
          writer.writerows(rows)
print('DrillOutput.csv')