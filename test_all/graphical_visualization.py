import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import linear_algebra_logic as lg
from src.domain.motor import *
import pandas as pd

numero_de_sep = 22

df = yf.download(
    "JNJ",
    start="2023-01-01",
    end="2025-01-01",
    auto_adjust=True,
    group_by="ticker"
)


x = np.arange(len(df.index))
y = df[('JNJ', 'Close')].values

data = {'dias': x, 'prices': y}
df_aux = pd.DataFrame(data)

pass

list_x = maximuns_minumus(df_aux['dias'].to_numpy(), df_aux['prices'].to_numpy(), numero_de_sep)
print(list_x)

list_y = df_aux.loc[list_x, 'prices']
print(list_y)


intervalos = divide_interval(x, numero_de_sep)
cortes = [bloco[-1] for bloco in intervalos]
print(intervalos)


plt.figure(figsize = (10,10))
plt.plot(x, y)
plt.scatter(list_x, list_y, color = 'red')
plt.vlines(x=cortes, ymin=df_aux['prices'].min(), ymax=df_aux['prices'].max(), color = 'green')
plt.show()
plt.close()
