import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create the DataFrame
data = pd.DataFrame({
    'Product_ID': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'Store_ID': ['S01', 'S02', 'S01', 'S03', 'S02'],
    'Advertisement_Spend': [10000, 5000, 12000, 4000, 8000],
    'Promotion': ['Yes', 'No', 'Yes', 'No', 'Yes'],
    'Season': ['Winter', 'Summer', 'Spring', 'Autumn', 'Winter'],
    'Previous_Sales': [200, 150, 300, 100, 220],
    'Sales': [250, 160, 340, 120, 260]
})

# Group by Store_ID to aggregate values
grouped = data.groupby('Store_ID').agg({
    'Advertisement_Spend': 'mean',
    'Sales': 'sum'
}).reset_index()

# Extract values for plotting
stores = grouped['Store_ID']
avg_spend = grouped['Advertisement_Spend']
total_sales = grouped['Sales']
x = np.arange(len(stores))

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart for Average Advertisement Spend
bar = ax1.bar(x, avg_spend, width=0.4, color='#4c72b0', label='Avg Advertisement Spend')
ax1.set_ylabel('Average Advertisement Spend', color='#4c72b0', fontsize=12)
ax1.set_xlabel('Store ID', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(stores, fontsize=11)
ax1.tick_params(axis='y', labelcolor='#4c72b0')

# Bar labels
for rect in bar:
    height = rect.get_height()
    ax1.annotate(f'{height:.0f}', xy=(rect.get_x() + rect.get_width()/2, height),
                 xytext=(0, 5), textcoords="offset points", ha='center', fontsize=10, color='#4c72b0')

# Line chart for Total Sales
ax2 = ax1.twinx()
line = ax2.plot(x, total_sales, color='#dd8452', marker='o', linewidth=2.5, label='Total Sales')
ax2.set_ylabel('Total Sales', color='#dd8452', fontsize=12)
ax2.tick_params(axis='y', labelcolor='#dd8452')

# Line labels
for i, val in enumerate(total_sales):
    ax2.annotate(str(val), xy=(x[i], val), xytext=(0, 8), textcoords="offset points",
                 ha='center', fontsize=10, color='#dd8452', weight='bold')

# Title and legend
plt.title('Store-wise Advertisement Spend vs Total Sales', fontsize=14, weight='bold')
fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.08), ncol=2)

plt.tight_layout()
plt.show()
