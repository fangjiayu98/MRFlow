import matplotlib.pyplot as plt
import matplotlib.patches as patches

#plt.rcParams["font.family"] = "Times New Roman"

# Data points (微调后的base值 + MRFlow)
training_time = [60.23, 77.45, 118.34, 114.67, 142.18, 48.76, 38.92]  # x-axis: training time (s/period)
mse = [5.52, 5.51, 5.54, 5.61, 5.40, 5.14, 4.95]        # y-axis: MAE
memory_usage = [3308, 3308, 3308, 3308, 3596, 1607, 2850]  # Memory footprint
memory_usage_size = ['3.3E3, 60s', '3.3E3, 77s', '3.3E3, 118s', '3.3E3, 115s', '3.6E3, 142s', '1.6E3, 49s', '2.9E3, 39s']

scale = 4

# Bubble sizes - proportional to memory usage (scaled for visibility)
bubble_size = [size * scale for size in memory_usage]

# Labels for each point
labels = ['Retrain-ST', 'Continual-ST-AN', 'Continual-ST-NN', 'TrafficStream', 'STKFC', 'EAC', 'MRFlow']

# Color for each point
colors = ['c', 'violet', 'orange', 'green', '#6ba2f9', 'pink', 'red']

# Create scatter plot
plt.figure(figsize=(10, 7))
scatter = plt.scatter(training_time, mse, s=bubble_size, alpha=0.6, c=colors)

# Add labels to each bubble
plt.text(37, 5.86, labels[0], fontsize=24, color=colors[0])
plt.text(37, 5.76, memory_usage_size[0], fontsize=20, color='black')

plt.text(67, 5.86, labels[1], fontsize=24, color=colors[1])
plt.text(67, 5.76, memory_usage_size[1], fontsize=20, color='black')

plt.text(93, 5.28, labels[2], fontsize=24, color=colors[2])
plt.text(93, 5.18, memory_usage_size[2], fontsize=20, color='black')

plt.text(108, 5.95, labels[3], fontsize=24, color=colors[3])
plt.text(108, 5.85, memory_usage_size[3], fontsize=20, color='black')

plt.text(133, 5.75, labels[4], fontsize=24, color=colors[4])
plt.text(133, 5.65, memory_usage_size[4], fontsize=20, color='black')

plt.text(38, 4.84, labels[5], fontsize=24, color=colors[5])
plt.text(38, 4.74, memory_usage_size[5], fontsize=20, color='black')

plt.text(18, 4.68, labels[6], fontsize=24, color=colors[6], fontweight='bold')
plt.text(18, 4.58, memory_usage_size[6], fontsize=20, color='black', fontweight='bold')

# Add memory footprint legend
plt.scatter([70, 100, 130], [4.88, 4.88, 4.88], s=[1000*scale, 2000*scale, 3000*scale], alpha=0.2, c='grey')
plt.text(66, 4.86, '1E3', fontsize=20)
plt.text(96, 4.86, '2E3', fontsize=20)
plt.text(126, 4.86, '3E3', fontsize=20)
plt.text(62, 4.68, 'Memory Footprint', fontsize=20, ha='left', color='grey')
rect = patches.Rectangle((60, 4.63), 85, 0.48, linewidth=1.5, edgecolor='black', facecolor='none', linestyle='--')
plt.gca().add_patch(rect)

# Add grid, labels, title
plt.grid(True, alpha=0.4)
plt.xlabel('Average Training Time (s / period)', fontsize=28, labelpad=10)
plt.ylabel('MAE', fontsize=28, labelpad=10)
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
plt.xlim(15, 160)
plt.ylim(4.5, 6.05)
plt.title('Energy-Stream', fontsize=28, pad=20)

plt.tight_layout()
plt.savefig('energy_mae_time_memory.pdf', dpi=600, bbox_inches='tight')
plt.show()
