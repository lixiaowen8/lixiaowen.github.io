import json
import pandas as pd
import matplotlib.pyplot as plt

# 读取问卷数据
with open("data.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)
df = pd.DataFrame(raw_data)

# 解决中文乱码
plt.rcParams["font.family"] = ["SimHei", "Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

# 1. 性别饼图
gender = df["gender"].value_counts()
plt.figure()
plt.pie(gender.values, labels=gender.index, autopct="%1.1f%%")
plt.title("问卷填写人性别分布")
plt.savefig("1_性别分布.png")
plt.close()

# 2. AI使用频率柱状图
freq = df["ai_use_freq"].value_counts()
plt.figure()
plt.bar(freq.index, freq.values)
plt.title("AI工具使用频率统计")
plt.savefig("2_使用频率.png")
plt.close()

# 3. 满意度柱状图
sat = df["ai_satisfaction"].value_counts()
plt.figure()
plt.bar(sat.index, sat.values, color="#ff8844")
plt.title("AI工具满意度分布")
plt.savefig("3_满意度统计.png")
plt.close()

# 打印统计表格
print("====问卷数据汇总统计====")
print(f"总有效填写人数：{len(df)}")
print("\n性别统计：\n", gender)
print("\nAI使用频率：\n", freq)
print("\n满意度统计：\n", sat)

# 导出Excel表格
df.to_excel("问卷汇总数据.xlsx", index=False)
print("\n已生成Excel数据表与3张分析图表")