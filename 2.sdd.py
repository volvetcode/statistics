#sd and d

import pandas as pd
from math import sqrt

data = {
    "numbers": [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]
}

df = pd.DataFrame(data)

print("D =", df.numbers.var(), "Sd =", sqrt(df.numbers.var()))