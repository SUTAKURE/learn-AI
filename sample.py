import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib

# 今回のcsvデータの場合そのまま読み込むとエラーがでるため、encodingを指定
df = pd.read_csv("./kpi.csv", encoding="shift-jis")
corr_mat = df.corr(method='pearson')

sns.heatmap(corr_mat,
            vmin=-1.0,
            vmax=1.0,
            center=0,
            annot=True,
            fmt='.1f',
            xticklabels=corr_mat.columns.values,
            yticklabels=corr_mat.columns.values
            )
plt.show()
