import scipy
import numpy as np

# Считается, что значение IQ (уровень интеллекта) у людей имеет нормальное распределение
# со средним значением равным 100 и стандартным отклонением равным 15 (M = 100, sd = 15).
# Какой приблизительно процент людей обладает IQ > 125?

mean = 100
sd = 15
IQ = 125
IQ2 = 500

a = np.array([[ 125 ]])
b = np.array([[ 500 ]])

zIQ = scipy.stats.zscore(a)
zIQ2 = scipy.stats.zscore(b)
print(scipy.stats.norm.cdf(zIQ2) - scipy.stats.norm.cdf(zIQ))