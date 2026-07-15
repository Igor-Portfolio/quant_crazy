import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import linear_algebra_logic as lg
from src.domain.motor import *

df = yf.download(
    "JNJ",
    start="2024-01-01",
    end="2025-01-01",
    auto_adjust=True,
    group_by="ticker"
)


print(df.head())

x = np.arange(len(df.index))
y = df[('JNJ', 'Close')].values

list_x = maximuns_minumus(x, y, 30)
print(list)
df_index = df.set_index('Close')
list_y = df_index.loc[list_x].values
print(list_y)




intervalos = divide_interval(x, 30)
print(intervalos)


plt.plot(x, y)
plt.show()
plt.figure(figsize = (10,10))
plt.close()
