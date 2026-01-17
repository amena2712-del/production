

dd_feat = (
    dd_price
        .groupby("ticker", group_keys=False)
        .apply(
            lambda x: (
                x.sort_values("Date", ascending=True)
                 .assign(
                     # Lags
                     Close_lag_1=x["Close"].shift(1),
                     Adj_Close_lag_1=x["Adj Close"].shift(1),

                     # Returns based on Close
                     returns=(x["Close"] / x["Close"].shift(1)) - 1,

                     # High–Low range
                     hi_lo_range=x["High"] - x["Low"]
                 )
            ),
            meta=pd.DataFrame(
                data={
                    "Date": "datetime64[ns]",
                    "Open": "f8",
                    "High": "f8",
                    "Low": "f8",
                    "Close": "f8",
                    "Adj Close": "f8",
                    "Volume": "i8",
                    "source": "object",
                    "Year": "int32",
                    "Close_lag_1": "f8",
                    "Adj_Close_lag_1": "f8",
                    "returns": "f8",
                    "hi_lo_range": "f8",
                },
                index=pd.Index([], dtype=pd.StringDtype(), name="ticker")
            )
        )
)