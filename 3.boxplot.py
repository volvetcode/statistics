import pandas as pd
import matplotlib.pyplot as plot

data = {
    "numbers": [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]
}

df = pd.DataFrame(data)
b_plot = df.boxplot(column = 'numbers')
print (b_plot.plot())