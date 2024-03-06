import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math

def DrawInfo(sample_20, sample_100, m1_20, m2_20, m1_100, m2_100, std1_20, std2_20, std1_100, std2_100):
    # Строим гистограмму данных
    plt.figure(figsize=(10, 6))
    sns.histplot(sample_20, kde=False, color='skyblue', edgecolor='black')

    # Добавляем вертикальные прямые
    # x1 = min_m - max_std
    # x2 = min_m
    # x3 = max_m
    # x4 = max_m + max_std
    plt.axvline(x = m1_20 - std2_20, color='red', label='min_m - max_std')
    plt.axvline(x = m1_20, color='blue', label='min_m')
    plt.axvline(x = m2_20, color='blue', label='max_m')
    plt.axvline(x = m2_20 + std2_20, color='red', label='max_m + max_std')

    plt.legend()
    plt.title('Гистограмма n = 20')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(sample_100, kde=False, color='skyblue', edgecolor='black')

    # Добавляем вертикальные прямые
    # x1 = min_m - max_std
    # x2 = min_m
    # x3 = max_m
    # x4 = max_m + max_std
    plt.axvline(x = m1_100 - std2_100, color='red', label='min_m - max_std')
    plt.axvline(x = m1_100, color='blue', label='min_m')
    plt.axvline(x = m2_100, color='blue', label='max_m')
    plt.axvline(x = m2_100 + std2_100, color='red', label='max_m + max_std')

    plt.legend()
    plt.title('Гистограмма n = 100')
    plt.show()

    # Доверительные интервалы средневыборочного матожидания
    plt.figure(figsize=(10, 6))
    plt.hlines(y = 1, xmin = m1_20, xmax = m2_20, label = 'n = 20')
    plt.hlines(y = 1.1, xmin = m1_100, xmax = m2_100, label = 'n = 100')
    plt.plot([m1_20, m2_20], [1, 1], marker='o', markersize=10, color='purple', zorder=3)  # Начальная точка
    plt.plot([m1_20, m2_20], [1, 1], marker='o', markersize=10, color='purple', zorder=3)  # Конечная точка
    plt.plot([m1_100, m2_100], [1.1, 1.1], marker='o', markersize=10, color='purple', zorder=3)  # Начальная точка
    plt.plot([m1_100, m2_100], [1.1, 1.1], marker='o', markersize=10, color='purple', zorder=3)  # Конечная точка
    plt.legend()
    plt.title('Доверительные интервалы средневыборочного матожидания')
    plt.show()

    # Доверительные интервалы средневыборочного СКО 
    plt.figure(figsize=(10, 6))
    plt.hlines(y = 1, xmin = std1_20, xmax = std2_20, label = 'n = 20')
    plt.hlines(y = 1.1, xmin = std1_100, xmax = std2_100, label = 'n = 100')
    plt.plot([std1_20, std2_20], [1, 1], marker='o', markersize=10, color='purple', zorder=3)  # Начальная точка
    plt.plot([std1_20, std2_20], [1, 1], marker='o', markersize=10, color='purple', zorder=3)  # Конечная точка
    plt.plot([std1_100, std2_100], [1.1, 1.1], marker='o', markersize=10, color='purple', zorder=3)  # Начальная точка
    plt.plot([std1_100, std2_100], [1.1, 1.1], marker='o', markersize=10, color='purple', zorder=3)  # Конечная точка
    plt.legend()
    plt.title('Доверительные интервалы средневыборочного СКО')
    plt.show()

def conf_intervals_normal(sample_20, sample_100):
    #take coefs from Student's table 
    coef_20 = 2.086 #for n = 20 
    coef_100 = 1.984 #for n = 100
    #take coefs from Hi-square table
    hii_20_1 = 32.852
    hii_20_2 = 8.907
    hii_100_1 = 128.422
    hii_100_2 = 73.361

    # n = 20
    mean_20 = np.mean(sample_20)
    std_20 = np.std(sample_20)

    m1_20 = mean_20 - std_20*coef_20/math.sqrt(20 - 1)
    m2_20 = 2*mean_20 - m1_20

    std1_20 = std_20*math.sqrt(20)/math.sqrt(hii_20_1)
    std2_20 = std_20*math.sqrt(20)/math.sqrt(hii_20_2)

    # n = 100
    mean_100 = np.mean(sample_100)
    std_100 = np.std(sample_100)

    m1_100 = mean_100 - std_100*coef_100/math.sqrt(100 - 1)
    m2_100 = 2*mean_100 - m1_100

    std1_100 = std_100*math.sqrt(100)/math.sqrt(hii_100_1)
    std2_100 = std_100*math.sqrt(100)/math.sqrt(hii_100_2)

    print("normal")
    print("n = 20")
    print("m = " + str(round(mean_20, 3)))
    print("std = " + str(round(std_20, 3)))
    print(str(round(m1_20, 3)) + " < m < " + str(round(m2_20, 3)))
    print(str(round(std1_20, 3)) + " < std < " + str(round(std2_20, 3)))
    print()
    print("n = 100")
    print("m = " + str(round(mean_100, 3)))
    print("std = " + str(round(std_100, 3)))
    print(str(round(m1_100,3)) + " < m < " + str(round(m2_100, 3)))
    print(str(round(std1_100, 3)) + " < std < " + str(round(std2_100, 3)))
    print()
    print()

    DrawInfo(sample_20, sample_100, m1_20, m2_20, m1_100, m2_100, std1_20, std2_20, std1_100, std2_100)


# эксцесс - нужен для произвольного распределения
def sample_excess(sample):
    mean = np.mean(sample)
    variance = np.var(sample)
    n = len(sample)
    excess = (np.sum((sample - mean)**4) / (n * variance**2)) - 3
    
    return excess

def conf_intervals_random(sample_20, sample_100):
    #take coefs from Student's table 
    coef = 1.96
    #excesses
    e_20 = sample_excess(sample_20)
    e_100 = sample_excess(sample_100)

    # n = 20
    mean_20 = np.mean(sample_20)
    std_20 = np.std(sample_20)

    m1_20 = mean_20 - std_20*coef/math.sqrt(20 - 1)
    m2_20 = 2*mean_20 - m1_20

    std1_20 = std_20*(1 - 0.5*coef*math.sqrt(e_20 + 2)/math.sqrt(20))
    std2_20 = std_20*(1 + 0.5*coef*math.sqrt(e_20 + 2)/math.sqrt(20))

    # n = 100
    mean_100 = np.mean(sample_100)
    std_100 = np.std(sample_100)

    m1_100 = mean_100 - std_100*coef/math.sqrt(100 - 1)
    m2_100 = 2*mean_100 - m1_100

    std1_100 = std_100*(1 - 0.5*coef*math.sqrt(e_100 + 2)/math.sqrt(100))
    std2_100 = std_100*(1 + 0.5*coef*math.sqrt(e_100 + 2)/math.sqrt(100))

    print("random")
    print("n = 20")
    print("m = " + str(round(mean_20, 3)))
    print("std = " + str(round(std_20, 3)))
    print(str(round(m1_20, 3)) + " < m < " + str(round(m2_20, 3)))
    print(str(round(std1_20, 3)) + " < std < " + str(round(std2_20, 3)))
    print()
    print("n = 100")
    print("m = " + str(round(mean_100, 3)))
    print("std = " + str(round(std_100, 3)))
    print(str(round(m1_100,3)) + " < m < " + str(round(m2_100, 3)))
    print(str(round(std1_100, 3)) + " < std < " + str(round(std2_100, 3)))
    print()
    print()

    DrawInfo(sample_20, sample_100, m1_20, m2_20, m1_100, m2_100, std1_20, std2_20, std1_100, std2_100)



def main():
    normal1 = np.random.normal(0, 1, 20)
    puasson1 = np.random.poisson(10, size=20)

    normal2 = np.random.normal(0, 1, 100)
    puasson2 = np.random.poisson(10, size=100)

    conf_intervals_normal(normal1, normal2)
    conf_intervals_random(puasson1, puasson2)

if __name__ == "__main__":
    main()