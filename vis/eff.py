import matplotlib.pyplot as plt
import matplotlib.patches as patches

#plt.rcParams["font.family"] = "Times New Roman"

# Data points
training_time = [205.05, 184.38, 143.86, 113.53, 93.03, 96.59, 72.18]  # x-axis: training time (s/period)
mae = [21.78, 20.84, 22.31, 21.27, 22.43, 20.75, 20.12]        # y-axis: MAE
memory_usage = [3308, 3308, 3308, 3308, 3596, 7170, 5840]  # Memory footprint
memory_usage_size = ['3.3E3, 205s', '3.3E3, 184s', '3.3E3, 144s', '3.3E3, 114s', '3.6E3, 93s', '7.1E3, 97s', '5.8E3, 72s']

scale = 4

# Bubble sizes - proportional to memory usage (scaled for visibility)
bubble_size = [size * scale for size in memory_usage]

# Labels for each point
labels = ['Retrain-ST', 'Continual-ST-AN', 'Continual-ST-NN', 'TrafficStream', 'STKFC', 'EAC', 'MRFlow']

# Color for each point
colors = ['c', 'violet', 'orange', 'green', '#6ba2f9', 'pink', 'red']

# Create scatter plot
plt.figure(figsize=(10, 7))
scatter = plt.scatter(training_time, mae, s=bubble_size, alpha=0.6, c=colors)

# Add text labels
plt.text(210, 22.75, labels[0], fontsize=24, color=colors[0])
plt.text(210, 22.49, memory_usage_size[0], fontsize=20, color='black')

plt.text(200, 20.25, labels[1], fontsize=24, color=colors[1])
plt.text(200, 19.99, memory_usage_size[1], fontsize=20, color='black')

plt.text(140, 23.35, labels[2], fontsize=24, color=colors[2])
plt.text(140, 23.09, memory_usage_size[2], fontsize=20, color='black')

plt.text(140, 20.68, labels[3], fontsize=24, color=colors[3])
plt.text(140, 20.42, memory_usage_size[3], fontsize=20, color='black')

plt.text(50, 23.45, labels[4], fontsize=24, color=colors[4])
plt.text(50, 23.19, memory_usage_size[4], fontsize=20, color='black')

plt.text(130, 20.1, labels[5], fontsize=24, color=colors[5])
plt.text(130, 19.84, memory_usage_size[5], fontsize=20, color='black')

plt.text(95, 19.53, labels[6], fontsize=24, color=colors[6], fontweight='bold')
plt.text(95, 19.27, memory_usage_size[6], fontsize=20, color='black', fontweight='bold')

# Add grid, labels, title
plt.grid(True, alpha=0.4)
plt.xlabel('Average Training Time (s / period)', fontsize=28, labelpad=10)
plt.ylabel('MAE', fontsize=28, labelpad=10)
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
plt.xlim(40, 280)
plt.ylim(19.2, 23.8)
plt.title('Air-Stream', fontsize=28, pad=20)

plt.tight_layout()
plt.savefig('air_mae_time_memory.pdf', dpi=600, bbox_inches='tight')
plt.show()
