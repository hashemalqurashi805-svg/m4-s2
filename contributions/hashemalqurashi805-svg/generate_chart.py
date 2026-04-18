import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Prepare dummy data reflecting hospital admission records
data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Admissions': [120, 115, 110, 130, 150, 180, 175]
}
df = pd.DataFrame(data)

# 2. Set the visual style of the plot
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")
palette = sns.color_palette("viridis", len(df))

# 3. Create the bar chart
ax = sns.barplot(x='Day', y='Admissions', data=df, palette=palette, hue='Day', legend=False)

# 4. Add titles and labels (Meeting quality standards)
plt.title('Weekly Trends in Hospital Admissions', fontsize=16, pad=20)
plt.xlabel('Day of the Week', fontsize=12)
plt.ylabel('Number of Admissions', fontsize=12)

# 5. Add data annotations on top of each bar
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 9), 
                textcoords='offset points',
                fontsize=10,
                fontweight='bold')

# 6. Save the chart with high quality (DPI 150) as required
plt.savefig('chart.png', dpi=150, bbox_inches='tight')

print("Chart generated successfully as chart.png")