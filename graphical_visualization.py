import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import linear_algebra_logic as lg

df = yf.download(
    ["JNJ"],
    start="2024-01-01",
    end="2025-01-01",
    auto_adjust=True,
    group_by="ticker"
)

a = len(df.index)


x = np.arange(len(df.index))
y = df[('JNJ', 'Close')].values

pass
# coeficients = lg.coef(x, y, len(df.index))
# f = lg.polynomial_value(coeficients)

# y_valores = f(x)

#derivada
# dp_coef = np.polyder(coeficients)
# dp = np.poly1d(dp_coef)

# y_derivate = dp(x)



pass

plt.plot(x,y, color="red")
# plt.plot(x,y_valores, color="blue")
# plt.plot(x,y_derivate, color="orange")
plt.show()
plt.savefig("grafico.png", dpi=150, bbox_inches="tight")
plt.close()

