import csv

rows=[]
with open("raw.githubusercontent.com_whitehatjr_Data-cleaning_master_main.csv","r") as f:
  csvreader=csv.reader(f)
  for row in csvreader:
    rows.append(row)

headers=rows[0]
planet_data_rows=rows[1:]
print(headers)
print(planet_data_rows[0])