import pandas as pd

# Example stock data
data = {
    "date": ["2025-01-01", "2025-01-02"],
    "symbol": ["AAPL", "AAPL"],
    "close": [150.25, 153.00]
}

df = pd.DataFrame(data)
df.to_csv("extracted_data.csv", index=False)

print("✅ Data extracted and saved to extracted_data.csv")
