import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

# Data
omar = {
    "Total Owed": 48391.31,
    "Total Paid": 0,
    "Total Remaining": 0
}

mostafa = {
    "Total Owed": 74000,
    "Total Paid": 0,
    "Total Remaining": 0
}

# Process the CSV file
with open('all_transactions.CSV', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if '0832' in row['Description'] and ('400' in row['Amount'] or '500' in row['Amount']):
            omar['Total Paid'] += float(row['Amount'])
        elif '9853' in row['Description'] and ('200' in row['Amount'] or '250' in row['Amount']):
            mostafa['Total Paid'] += float(row['Amount'])

# Calculate remaining amounts
omar['Total Remaining'] = round(omar['Total Owed'] - omar['Total Paid'], 2)
mostafa['Total Remaining'] = round(mostafa['Total Owed'] - mostafa['Total Paid'], 2)

# Prepare data for the table
data = {
    "Name": ["Omar", "Mostafa"],
    "Total Owed": [omar['Total Owed'], mostafa['Total Owed']],
    "Total Paid": [omar['Total Paid'], mostafa['Total Paid']],
    "Total Remaining": [omar['Total Remaining'], mostafa['Total Remaining']],
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(6, 2))
ax.axis('tight')
ax.axis('off')

table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

table.auto_set_font_size(False)
table.set_fontsize(10)
header_color = '#7a7a7a'
for i in range(len(df.columns)):
    table[0, i].set_facecolor(header_color)
    table[0, i].set_text_props(color='white')

plt.savefig("financial_overview.png", bbox_inches='tight', dpi=300)