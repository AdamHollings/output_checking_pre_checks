import csv
import random

# Generate random data for the table
data = []
for age_band in range(1, 6):
    for has_cancer in [True, False]:
        for lsoa_num in range(1000,1005):
            lsoa = f"LSOA{lsoa_num}"
            count = random.choices([random.randint(11, 50) // 5 * 5, '*'], weights=(90, 10))
            data.append([age_band, lsoa, has_cancer, count])

# Write the data to a CSV file
with open('sample_table.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['age_band', 'LSOA', 'has_cancer', 'count'])
    writer.writerows(data)

print("CSV table with rows for each combination of age_band and has_cancer has been generated and saved to 'sample_table.csv'.")
