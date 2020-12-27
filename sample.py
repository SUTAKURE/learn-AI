import seaborn as sns  # こちらにも再度記述
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# アヤメのデータの読み込み ※左のirisは変数名で、右側のirisはirisという花のデータセットを読み込む設定です。
iris = sns.load_dataset("iris")
# データに含まれる全ての数値変数同士での散布図を描画

# 今回はirisという変数を渡していますが、Pandasのデータフレーム(DataFrame)型を渡すことで、散布図行列を描画出来ます。
sns.pairplot(iris)  # 散布図行列
plt.show()  # こちらはJupyter Notebook上などでは、なくても描画できます
