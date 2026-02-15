import csv
import matplotlib.pyplot as plt
import os
import sys

# ==================== 动态获取项目根目录 ====================
# __file__ 是当前脚本文件的绝对路径
script_path = os.path.abspath(__file__)

# 取当前脚本所在目录（如果代码在子文件夹里也能适应）
script_dir = os.path.dirname(script_path)

# 如果你的代码文件在项目根目录，直接用 script_dir 作为根目录
# 如果代码在子文件夹里，再往上一层（视情况调整层级）
project_root = script_dir  # 大多数情况直接用这一层就够了

# 如果项目结构是：根目录下有 data/ 和你的 .py 文件，就这样
filename = os.path.join(project_root, 'data', 'new_eq_data.csv')

# ==================== 调试输出（强烈建议保留，方便排查） ====================
print("当前脚本路径：", script_path)
print("项目根目录：", project_root)
print("尝试读取的文件：", filename)

# ==================== 正式读取数据 ====================
mags, lons, lats = [], [], []

with open(filename, encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  # 跳过标题行
    print("\n标题行：", header)

    for row in reader:
        try:
            mag = float(row[4])   # 震级
            lon = float(row[2])   # 经度
            lat = float(row[1])   # 纬度
            mags.append(mag)
            lons.append(lon)
            lats.append(lat)
        except (ValueError, IndexError):
            continue

# ==================== 绘图 ====================
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(12, 6))
plt.scatter(lons, lats, c=mags, cmap='Reds', s=[mag * 20 for mag in mags],
            alpha=0.7, edgecolors='black', linewidth=0.5)

plt.title('全球近期地震分布图（震级越大点越大/越红）', fontsize=16)
plt.xlabel('经度')
plt.ylabel('纬度')
plt.colorbar(label='震级 (Magnitude)')
plt.grid(True, alpha=0.3)

plt.savefig('earthquake_map.png', dpi=300, bbox_inches='tight')
plt.show()