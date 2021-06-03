import pandas as pd

data = pd.read_csv("output/input.csv")

fig = data.sex.plot.hist(rot = 0, dodge = False).get_figure()
fig.savefig("output/descriptive1.png")