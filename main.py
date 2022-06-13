import numpy as np

# -------------------Problem N1-----------
N = 10000
r = np.zeros(N)
v = np.zeros(N)
omg1 = -1
omg2 = 4
R1 = 2
R2 = 8
r[0] = R1
step = (R2-R1)/N
nyu = omg2/omg1
eta = R1/R2

A = (omg1*(nyu-eta**2))/(1-eta**2)
B = ((omg1*R1**2)*(1-nyu))/(1-eta**2)

for i in range(N):
    r[i] = r[0] + step*i
    v[i] = A*r[i] + B/r[i]
    print(r[i], ";", v[i])

# -------------------------Problem N2--------------------------
# N = 1000
# r = np.zeros(N)
# v = np.zeros(N)
# omg1 = 8
# omg2 = 0
# R1 = 20
# R2 = 0
# r[0] = 0
# step = np.abs((R2 - R1)) / N
#
# A = (R2**2*omg2-omg1*R1**2)/(R2**2 - R1**2)
# B = ((R1**2*R2**2)*(omg1-omg2))/(R2**2-R1**2)
#
# for i in range(N - 1):
#    r[i + 1] = r[i] + step
#    v[i] = A * r[i+1] + B / r[i+1]
#    print(r[i], ";", v[i])

# -------------------------Problem N3--------------------------
# N = 1000
# r = np.zeros(N)
# v = np.zeros(N)
# omg1 = 10
# omg2 = 20
# R1 = 5
# R2 = 10
# r[0] = R1
# step = np.abs((R2 - R1)) / N
#
# A = (R2**2*omg2-omg1*R1**2)/(R2**2 - R1**2)
# B = ((R1**2*R2**2)*(omg1-omg2))/(R2**2-R1**2)
#
# for i in range(N - 1):
#    r[i + 1] = r[i] + step
#    v[i] = A * r[i+1] + B / r[i+1]
#    print(r[i], ";", v[i])