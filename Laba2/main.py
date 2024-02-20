import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
import statistics
np.random.seed(42)

def trimmed_mean(sample, trim_fraction):
    sorted_sample = sorted(sample)
    trim_size = int(len(sorted_sample) * trim_fraction)
    trimmed_sample = sorted_sample[trim_size:-trim_size]
    return sum(trimmed_sample) / len(trimmed_sample)

def quartile_1_4(sample):
    n = len(sample)
    sorted_sample = sorted(sample)
    index = n // 4
    if n % 4 == 0:
        return sorted_sample[index - 1]
    else:
        return sorted_sample[index]

def quartile_3_4(sample):
    n = len(sample)
    sorted_sample = sorted(sample)
    index = 3 * n // 4
    if n % 4 == 0:
        return sorted_sample[index - 1]
    else:
        return sorted_sample[index]

rows = 5
columns = 3

normal_v = [[[int(0), 0, 0] for _ in range(columns)] for _ in range(rows)]
cauchy_v = [[[int(0), 0, 0] for _ in range(columns)] for _ in range(rows)]
student_v = [[[int(0), 0, 0] for _ in range(columns)] for _ in range(rows)]
puasson_v = [[[int(0), 0, 0] for _ in range(columns)] for _ in range(rows)]
uniform_v = [[[int(0), 0, 0] for _ in range(columns)] for _ in range(rows)]

base_v = [normal_v, cauchy_v, student_v, puasson_v, uniform_v]

for i in range(0, 1000):

    normal = np.random.normal(0, 1, 980)
    cauchy = np.random.standard_cauchy(250)
    student = np.random.standard_t(df=3, size=1001)
    puasson = np.random.poisson(10, size=1001)
    uniform = np.random.uniform(-(math.sqrt(3)), math.sqrt(3), 1001)

    array_of_distributions = [normal, cauchy, student, puasson, uniform]
    array_of_powers = [int(10), int(50), int(1000)]
    for distribution, j in zip(array_of_distributions, range(0, 5)):
        for power, k in zip(array_of_powers, range(0, 3)):
            base_v[j][0][k][0] = int(power)
            base_v[j][0][k][1] += (sum(distribution[:power]) / len(distribution[:power])) / 1000
            base_v[j][0][k][2] += (sum(distribution[:power]) / len(distribution[:power])) ** 2 / 1000
            base_v[j][1][k][0] = int(power)
            base_v[j][1][k][1] += statistics.median(distribution[:power]) / 1000
            base_v[j][1][k][2] += statistics.median(distribution[:power]) ** 2 / 1000
            base_v[j][2][k][0] = int(power)
            base_v[j][2][k][1] += ((max(distribution[:power]) + min(distribution[:power])) / 2) / 1000
            base_v[j][2][k][2] += ((max(distribution[:power]) + min(distribution[:power])) / 2) ** 2 / 1000
            q1 = quartile_1_4(distribution[:power])
            q3 = quartile_3_4(distribution[:power])
            base_v[j][3][k][0] = int(power)
            base_v[j][3][k][1] += ((q1 + q3) / 2) / 1000
            base_v[j][3][k][2] += ((q1 + q3) / 2) ** 2 / 1000
            base_v[j][4][k][0] = int(power)
            base_v[j][4][k][1] += trimmed_mean(distribution[:power], 0.25) / 1000
            base_v[j][4][k][2] += trimmed_mean(distribution[:power], 0.25) ** 2 / 1000

for i in range(0, 5):
    for k in range (0, 5):
        for j in range(0, 3):
            base_v[i][k][j][2] = base_v[i][k][j][2] - base_v[i][k][j][1] ** 2

names = ["normal", "cauchy", "student", "puasson", "uniform"]
params = ["sample", "med", "z_r", "z_q", "z_tr"]
for i, name in zip(range(0, 5), names):
    for j, param in zip(range (0, 5), params):
        fig, ax = plt.subplots()
        df = pd.DataFrame(base_v[i][j], columns=['Power', 'Average', 'Dispersion'])
        table = ax.table(cellText = df.values, colLabels=df.columns,   loc='center')
        table.set_fontsize (35)
        table.scale (1,6)
        ax.axis('off')
        plt.savefig(f'{name}, {param}')
