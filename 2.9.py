import pandas as pd
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\加州房价数据集.csv")
# 1. 查看前5行数据（快速预览）
print("=== 数据前5行 ===")
print(df.head())

# 2. 查看数据基本信息（列名、数据类型、非空值数量）
print("\n=== 数据基本信息 ===")
print(df.info())

# 3. 查看数据形状（行数, 列数）
print("\n=== 数据形状（行, 列）===")
print(df.shape)

# 4. 查看数据的统计摘要（数值列的均值、最值等，可选）
print("\n=== 数值列统计信息 ===")
print(df.describe())

print("=== 每列空值数量 ===")
null_count = df.isnull().sum()
print(null_count)

dup_count = df.duplicated().sum()
print(f"\n=== 重复行数量：{dup_count} ===")
df_clean = df.fillna(0)
print(df_clean.head())