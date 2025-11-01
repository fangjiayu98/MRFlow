import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置字体和样式

rcParams['font.size'] = 10


# 创建图表 - 2行3列
fig, axes = plt.subplots(2, 3, figsize=(10, 4))
fig.subplots_adjust(hspace=0.3, wspace=0.35)

color1 = '#2E86AB'
color2 = '#A23B72'

# ==================== 第一行: PEMS-Stream ====================

# (a) 分辨率阶段数 S
S_values = [1, 2, 3, 4, 5]
pems_mae_s = [14.57, 14.12, 13.85, 13.73, 13.82]
pems_mape_s = [20.45, 19.85, 19.38, 19.16, 19.35]

ax1 = axes[0, 0]
ax1.set_xlabel('Number of Resolution Stages (S)', fontsize=11, fontweight='bold')
ax1.set_ylabel('MAE', color=color1, fontsize=11, fontweight='bold')
ax1.plot(S_values, pems_mae_s, 'o-', color=color1, linewidth=2.5, 
         markersize=8, label='MAE', markeredgewidth=1.5, markeredgecolor='white')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.set_xticks(S_values)
ax1.tick_params(axis='x', rotation=45)
ax1.set_ylim([13.5, 14.8])

ax1_twin = ax1.twinx()
ax1_twin.set_ylabel('MAPE (%)', color=color2, fontsize=11, fontweight='bold')
ax1_twin.plot(S_values, pems_mape_s, 's-', color=color2, linewidth=2.5, 
              markersize=8, label='MAPE', markeredgewidth=1.5, markeredgecolor='white')
ax1_twin.tick_params(axis='y', labelcolor=color2)
ax1_twin.set_ylim([19.0, 20.7])
ax1_twin.tick_params(axis='x', rotation=45)
best_idx = np.argmin(pems_mae_s)
ax1.scatter(S_values[best_idx], pems_mae_s[best_idx], s=200, c='gold', 
            edgecolors='black', linewidths=2, zorder=5, marker='*')
#ax1.set_title('(a) PEMS-Stream - Resolution Stages', fontsize=12, fontweight='bold', pad=10)

# (b) 锚点维度 d_a
da_values = [8, 16, 32, 64, 128, 256]
pems_mae_da = [14.25, 14.02, 13.85, 13.73, 13.78, 14.05]
pems_mape_da = [20.08, 19.68, 19.42, 19.16, 19.35, 19.72]

ax2 = axes[0, 1]
ax2.set_xlabel('Anchor Dimension ($d_a$)', fontsize=11, fontweight='bold')
ax2.set_ylabel('MAE', color=color1, fontsize=11, fontweight='bold')
ax2.plot(da_values, pems_mae_da, 'o-', color=color1, linewidth=2.5, 
         markersize=8, markeredgewidth=1.5, markeredgecolor='white')
ax2.tick_params(axis='y', labelcolor=color1)
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.set_xscale('log', base=2)
ax2.set_xticks(da_values)
ax2.tick_params(axis='x', rotation=45)
ax2.set_xticklabels(da_values)
ax2.set_ylim([13.6, 14.4])

ax2_twin = ax2.twinx()
ax2_twin.set_ylabel('MAPE (%)', color=color2, fontsize=11, fontweight='bold')
ax2_twin.plot(da_values, pems_mape_da, 's-', color=color2, linewidth=2.5, 
              markersize=8, markeredgewidth=1.5, markeredgecolor='white')
ax2_twin.tick_params(axis='y', labelcolor=color2)
ax2_twin.set_ylim([19.0, 20.3])
ax2_twin.tick_params(axis='x', rotation=45)
best_idx = np.argmin(pems_mae_da)
ax2.scatter(da_values[best_idx], pems_mae_da[best_idx], s=200, c='gold', 
            edgecolors='black', linewidths=2, zorder=5, marker='*')
#ax2.set_title('(b) PEMS-Stream - Anchor Dimension', fontsize=12, fontweight='bold', pad=10)

# (c) 分辨率权重 λ_s
lambda_values = [0.5, 0.7, 0.9, 1.0, 1.1, 1.3]
pems_mae_lambda = [14.02, 13.88, 13.78, 13.73, 13.80, 13.95]
pems_mape_lambda = [19.68, 19.45, 19.28, 19.16, 19.35, 19.62]

ax3 = axes[0, 2]
ax3.set_xlabel('Resolution Weight ($\\lambda_s$)', fontsize=11, fontweight='bold')
ax3.set_ylabel('MAE', color=color1, fontsize=11, fontweight='bold')
ax3.plot(lambda_values, pems_mae_lambda, 'o-', color=color1, linewidth=2.5, 
         markersize=8, markeredgewidth=1.5, markeredgecolor='white')
ax3.tick_params(axis='y', labelcolor=color1)
ax3.grid(True, alpha=0.3, linestyle='--')
ax3.set_xticks(lambda_values)
ax3.tick_params(axis='x', rotation=45)
ax3.set_ylim([13.6, 14.2])

ax3_twin = ax3.twinx()
ax3_twin.set_ylabel('MAPE (%)', color=color2, fontsize=11, fontweight='bold')
ax3_twin.plot(lambda_values, pems_mape_lambda, 's-', color=color2, linewidth=2.5, 
              markersize=8, markeredgewidth=1.5, markeredgecolor='white')
ax3_twin.tick_params(axis='y', labelcolor=color2)
ax3_twin.tick_params(axis='x', rotation=45)
ax3_twin.set_ylim([19.0, 19.8])

best_idx = np.argmin(pems_mae_lambda)
ax3.scatter(lambda_values[best_idx], pems_mae_lambda[best_idx], s=200, c='gold', 
            edgecolors='black', linewidths=2, zorder=5, marker='*')
#ax3.set_title('(c) PEMS-Stream - Resolution Weight', fontsize=12, fontweight='bold', pad=10)

# ==================== 第二行: Energy-Stream ====================

# (d) 分辨率阶段数 S
energy_mae_s = [5.95, 5.72, 5.58, 5.48, 5.56]
energy_mape_s = [53.82, 52.15, 51.08, 50.44, 51.25]

ax4 = axes[1, 0]
ax4.set_xlabel('Number of Resolution Stages (S)', fontsize=11, fontweight='bold')
ax4.set_ylabel('MAE', color=color1, fontsize=11, fontweight='bold')
ax4.plot(S_values, energy_mae_s, 'o-', color=color1, linewidth=2.5, 
         markersize=8, markeredgewidth=1.5, markeredgecolor='white')
ax4.tick_params(axis='y', labelcolor=color1)
ax4.grid(True, alpha=0.3, linestyle='--')
ax4.set_xticks(S_values)
ax4.tick_params(axis='x', rotation=45)
ax4.set_ylim([5.3, 6.1])

ax4_twin = ax4.twinx()
ax4_twin.set_ylabel('MAPE (%)', color=color2, fontsize=11, fontweight='bold')
ax4_twin.plot(S_values, energy_mape_s, 's-', color=color2, linewidth=2.5, 
              markersize=8, markeredgewidth=1.5, markeredgecolor='white')
ax4_twin.tick_params(axis='y', labelcolor=color2)
ax4_twin.tick_params(axis='x', rotation=45)
ax4_twin.set_ylim([50.0, 54.5])

best_idx = np.argmin(energy_mae_s)
ax4.scatter(S_values[best_idx], energy_mae_s[best_idx], s=200, c='gold', 
            edgecolors='black', linewidths=2, zorder=5, marker='*')
#ax4.set_title('(d) Energy-Stream - Resolution Stages', fontsize=12, fontweight='bold', pad=10)

# (e) 锚点维度 d_a
energy_mae_da = [5.78, 5.65, 5.55, 5.48, 5.53, 5.72]
energy_mape_da = [52.15, 51.42, 50.88, 50.44, 50.82, 51.68]

ax5 = axes[1, 1]
ax5.set_xlabel('Anchor Dimension ($d_a$)', fontsize=11, fontweight='bold')
ax5.set_ylabel('MAE', color=color1, fontsize=11, fontweight='bold')
ax5.plot(da_values, energy_mae_da, 'o-', color=color1, linewidth=2.5, 
         markersize=8, markeredgewidth=1.5, markeredgecolor='white')
ax5.tick_params(axis='y', labelcolor=color1)
ax5.grid(True, alpha=0.3, linestyle='--')
ax5.set_xscale('log', base=2)
ax5.set_xticks(da_values)
ax5.set_xticklabels(da_values)
ax5.tick_params(axis='x', rotation=45)
ax5.set_ylim([5.4, 5.9])

ax5_twin = ax5.twinx()
ax5_twin.set_ylabel('MAPE (%)', color=color2, fontsize=11, fontweight='bold')
ax5_twin.plot(da_values, energy_mape_da, 's-', color=color2, linewidth=2.5, 
              markersize=8, markeredgewidth=1.5, markeredgecolor='white')
ax5_twin.tick_params(axis='y', labelcolor=color2)
ax5_twin.tick_params(axis='x', rotation=45)
ax5_twin.set_ylim([50.0, 52.5])

best_idx = np.argmin(energy_mae_da)
ax5.scatter(da_values[best_idx], energy_mae_da[best_idx], s=200, c='gold', 
            edgecolors='black', linewidths=2, zorder=5, marker='*')
#ax5.set_title('(e) Energy-Stream - Anchor Dimension', fontsize=12, fontweight='bold', pad=10)

# (f) 分辨率权重 λ_s
energy_mae_lambda = [5.68, 5.58, 5.52, 5.48, 5.54, 5.66]
energy_mape_lambda = [51.62, 51.05, 50.72, 50.44, 50.88, 51.45]

ax6 = axes[1, 2]
ax6.set_xlabel('Resolution Weight ($\\lambda_s$)', fontsize=11, fontweight='bold')
ax6.set_ylabel('MAE', color=color1, fontsize=11, fontweight='bold')
ax6.plot(lambda_values, energy_mae_lambda, 'o-', color=color1, linewidth=2.5, 
         markersize=8, markeredgewidth=1.5, markeredgecolor='white')
ax6.tick_params(axis='y', labelcolor=color1)
ax6.grid(True, alpha=0.3, linestyle='--')
ax6.set_xticks(lambda_values)
ax6.tick_params(axis='x', rotation=45)
ax6.set_ylim([5.4, 5.8])

ax6_twin = ax6.twinx()
ax6_twin.set_ylabel('MAPE (%)', color=color2, fontsize=11, fontweight='bold')
ax6_twin.plot(lambda_values, energy_mape_lambda, 's-', color=color2, linewidth=2.5, 
              markersize=8, markeredgewidth=1.5, markeredgecolor='white')
ax6_twin.tick_params(axis='y', labelcolor=color2)
ax6_twin.tick_params(axis='x', rotation=45)
ax6_twin.set_ylim([50.2, 51.8])

best_idx = np.argmin(energy_mae_lambda)
ax6.scatter(lambda_values[best_idx], energy_mae_lambda[best_idx], s=200, c='gold', 
            edgecolors='black', linewidths=2, zorder=5, marker='*')
#ax6.set_title('(f) Energy-Stream - Resolution Weight', fontsize=12, fontweight='bold', pad=10)

# # 添加图例
# lines1, labels1 = ax1.get_legend_handles_labels()
# lines2, labels2 = ax1_twin.get_legend_handles_labels()
# fig.legend(lines1 + lines2, labels1 + labels2, loc='upper center', 
#            bbox_to_anchor=(0.5, 0.99), ncol=2, frameon=True, 
#            fontsize=11, edgecolor='black', fancybox=False)

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig('parameter_sensitivity.pdf', dpi=300, bbox_inches='tight')
plt.show()

print("图表已保存！")
print(f"最优配置: S=4, d_a=64, λ_s=1.0")