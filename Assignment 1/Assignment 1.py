import pandas as pd

data = pd.read_csv("Data/Toyota.csv")

## data.plot.scatter(x="Age",y="Price")
## data.plot(x="KM",y="CC")
data["CC"].plot(kind="hist")
