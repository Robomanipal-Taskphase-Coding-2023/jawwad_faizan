import pandas as pd

def graddesc(m10, m20, m30, m40, m50, b0, points, L):
    m1_grad = 0
    m2_grad = 0
    m3_grad = 0
    m4_grad = 0
    m5_grad = 0
    b_grad = 0
    error = 0
    n = len(points)

    for i in range(n):
        y = points.iloc[i].TOTCHG
        x1 = points.iloc[i].AGE
        x2 = points.iloc[i].RACE
        x3 = points.iloc[i].FEMALE
        x4 = points.iloc[i].APRDRG
        x5 = points.iloc[i].LOS

        y_app = (m10 * x1) + (m20 * x2) + (m30 * x3) + (m40 * x4) + (m50 * x5) + b0

        m1_grad += -(1 / n) * x1 * (y - y_app)
        m2_grad += -(1 / n) * x2 * (y - y_app)
        m3_grad += -(1 / n) * x3 * (y - y_app)
        m4_grad += -(1 / n) * x4 * (y - y_app)
        m5_grad += -(1 / n) * x5 * (y - y_app)
        b_grad += -(1 / n) * (y - y_app)

        error += (y - y_app)** 2

    m1 = m10 - (L * m1_grad)
    m2 = m20 - (L * m2_grad)
    m3 = m30 - (L * m3_grad)
    m4 = m40 - (L * m4_grad)
    m5 = m50 - (L * m5_grad)
    b = b0 - (L * b_grad)
    error = error/(2*n)
    print(error)

    return m1, m2, m3, m4, m5, b

data = pd.read_csv('linear_regression_dataset.csv')

data['APRDRG'] = data['APRDRG'] / 952
data['AGE'] = data['AGE'] / 17.0

print(data)

m1 = 0
m2 = 0
m3 = 0
m4 = 0
m5 = 0
b = 0
L = 0.09

for i in range(1000):
    if i % 50 == 0:
        print(i)
    m1, m2, m3, m4, m5, b = graddesc(m1, m2, m3, m4, m5, b, data, L)

r = 0

for i in range(len(data)):
    y = data.iloc[i].TOTCHG
    x1 = data.iloc[i].AGE
    x2 = data.iloc[i].RACE
    x3 = data.iloc[i].FEMALE
    x4 = data.iloc[i].APRDRG
    x5 = data.iloc[i].LOS
    y_app = m1 * x1 + m2 * x2 + m3 * x3 + m4 * x4 + m5 * x5 + b

    r += ((y_app - y) / y) ** 2

print(float(r / len(data))) #this is the accuracy getting printed
