from scipy import stats 

#Считается, что значение IQ (уровень интеллекта) у людей имеет нормальное распределение 
#со средним значением равным 100 и стандартным отклонением равным 15 (M = 100, sd = 15).
#Какой приблизительно процент людей обладает IQ  на промежутке от 70 до 112 

print(f'На промежутке [-2σ ; 0,8σ] расположено {(stats.norm.cdf(0.8) - stats.norm.cdf(-2)):.2%} значений')