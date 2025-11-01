import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2011, 2018)
methods = ['Retrain-ST', 'Pretrain-ST','TrafficStream', 'STKEC', 'EAC', 'MRFlow']

# 模拟数据 - 请替换为你的实际数据
# MRFlow表现最好，其他方法根据图中趋势微调
avg_mean_mape = [
    [22.0, 23.8, 23.9, 24.7, 23.2, 25.5, 24.8],  # Retrain-ST
    [22.2, 22.3, 23.5, 24.1, 24.3, 25.1, 27.5],  # Pretrain-ST

    [22.3, 23.2, 23.8, 24.8, 24.7, 24.9, 25.2],  # TrafficStream
    [22.0, 23.5, 24.1, 24.5, 23.5, 25.2, 25.3],  # STKEC
    [21.8, 20.9, 22.5, 23.9, 23.0, 24.1, 24.5],  # EAC
    [21.2, 19.7, 22.0, 23.2, 22.5, 23.5, 23.3],  # MRFlow (最优)
]

avg_std_mape = [
    [0.8, 0.9, 1.0, 1.1, 1.0, 1.2, 1.1],
    [0.9, 0.8, 1.0, 1.1, 1.2, 1.3, 1.4],
  
    [0.9, 1.0, 1.0, 1.2, 1.1, 1.2, 1.2],
    [0.8, 0.9, 1.0, 1.1, 1.0, 1.1, 1.2],
    [0.7, 0.6, 0.8, 1.0, 0.9, 1.0, 1.0],
    [0.6, 0.4, 0.6, 0.8, 0.8, 0.85, 0.8],
]

twelve_mean_mape = [
    [25.2, 27.3, 27.8, 28.8, 28.2, 29.5, 28.9],  # Retrain-ST
    [25.5, 25.8, 27.2, 28.5, 29.0, 29.8, 31.5],  # Pretrain-ST

    [25.6, 26.8, 27.5, 28.9, 28.8, 29.0, 29.3],  # TrafficStream
    [25.3, 27.0, 27.8, 28.6, 28.0, 29.3, 29.5],  # STKEC
    [24.8, 23.8, 25.8, 27.2, 26.3, 27.5, 27.9],  # EAC
    [24.2, 23.2, 25.0, 26.5, 25.8, 26.8, 27.2],  # MRFlow (最优)
]

twelve_std_mape = [
    [1.0, 1.1, 1.2, 1.3, 1.2, 1.4, 1.3],
    [1.1, 1.0, 1.2, 1.3, 1.4, 1.5, 1.6],
  
    [1.1, 1.2, 1.2, 1.4, 1.3, 1.4, 1.4],
    [1.0, 1.1, 1.2, 1.3, 1.2, 1.3, 1.4],
    [0.9, 0.8, 1.0, 1.2, 1.1, 1.2, 1.2],
    [0.6, 0.65, 0.8, 1.0, 0.9, 0.8, 1.0],
]

mean_mape1 = np.array(avg_mean_mape)
std_mape1 = np.array(avg_std_mape)
mean_mape2 = np.array(twelve_mean_mape)
std_mape2 = np.array(twelve_std_mape)

fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# 颜色和标记配置
colors = ['blue', 'orange',  'green', 'silver', 'red', 'purple']
markers = ['o', 's', 'v', 'D', 'd', '*']

# 左图：Avg. @ RMSE
for i, method in enumerate(methods):
    axs[0].plot(years, mean_mape1[i], marker=markers[i], label=method, 
                markersize=12 if i == 6 else 10, linewidth=2.5 if i == 6 else 2,
                color=colors[i])
    axs[0].fill_between(years, mean_mape1[i] - std_mape1[i], 
                        mean_mape1[i] + std_mape1[i], alpha=0.2, color=colors[i])

axs[0].set_title('Avg. @ RMSE', fontsize=26, pad=20)
axs[0].set_xlabel('Year', fontsize=26)
axs[0].set_ylabel('RMSE Value', fontsize=26)
axs[0].set_ylim(19.5, 30)
axs[0].legend(ncol=2, columnspacing=0.5, loc='upper left', fontsize=20)
axs[0].grid(True, alpha=0.4)
axs[0].tick_params(axis='both', labelsize=20)

# 右图：12 @ RMSE
for i, method in enumerate(methods):
    axs[1].plot(years, mean_mape2[i], marker=markers[i], label=method, 
                markersize=12 if i == 6 else 10, linewidth=2.5 if i == 6 else 2,
                color=colors[i])
    axs[1].fill_between(years, mean_mape2[i] - std_mape2[i], 
                        mean_mape2[i] + std_mape2[i], alpha=0.2, color=colors[i])

axs[1].set_title('12 @ RMSE', fontsize=26, pad=20)
axs[1].set_xlabel('Year', fontsize=26)
axs[1].set_ylabel('RMSE Value', fontsize=26)
axs[1].set_ylim(22, 32)
axs[1].legend(ncol=2, columnspacing=0.5, loc='lower right', fontsize=20)
axs[1].grid(True, alpha=0.4)
axs[1].tick_params(axis='both', labelsize=20)

plt.tight_layout()
plt.savefig('few_shot.pdf', dpi=600, bbox_inches='tight')
plt.show()
