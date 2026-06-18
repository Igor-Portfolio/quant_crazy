import yfinance as yf

df = yf.download(
    ["JNJ"],
    start="2020-01-01",
    end="2025-01-01",
    auto_adjust=True,
    group_by="ticker"
)

pass

