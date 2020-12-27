import pandas as pd
# 今回のcsvデータの場合そのまま読み込むとエラーがでるため、encodingを指定
df = pd.read_csv("./kpi.csv", encoding="shift-jis")
corr_mat = df.corr(method='pearson')
print(corr_mat)
