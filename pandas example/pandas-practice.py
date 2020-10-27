# 載入 pandas 模組
import pandas as pd

# 建立 Series
data = pd.Series([20, 10, 15])
# 基本 Series 操作
# print(data)
# print("Max",data.max())
# print("Median",data.median())
# data = data * 2
# print(data)
# data = data == 20 #比較資料 若是20 輸出True 若不是 則輸出False
# print(data)

# 建立 DataFrame
data = pd.DataFrame({"name":["Amy", "John", "Bob"],
                     "salary": [30000, 50000, 40000]})

# 基本 DataFrame 操作
# print(data)

# 取得特定的欄位
# print(data["salary"])

# 取得特定的列
print(data)
print("==================")
print(data.iloc[0])  # 印出第一列
print(data.iloc[1])  # 印出第二列