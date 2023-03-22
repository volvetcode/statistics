#mode, mean and median
import pandas as pd

data = {
    "height": [185, 175, 170, 169, 171, 172, 175, 157, 170, 172, 167, 173, 168, 167, 166, 167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171]
}

df = pd.DataFrame(data)

print('мода:', df.height.mode()[0], 'среднее арифмитическое:', df.height.mean(), 'медиана:', df.height.median())
