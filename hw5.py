import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

def load_data(filepath):
    # open the file in read mode
    filename = open(filepath, 'r')

    # creating dictreader object
    file = csv.DictReader(filename)

    return file

def q2(years, days):

    Year = years[:, 1]
    # print("The years", Year)
    Days = days
    # print(days)

    plt.plot(Year, Days)
    plt.title('Frozen Days by Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Frozen Days')
    plt.savefig("plot.jpg")

def q3a(file):
    csv = load_data(file)
    # creating empty lists
    yearVec = []

    for col in csv:
        # print("years!", col)
        yearVec.append([1, int(col['year'])])

    x = np.array(yearVec)
    return x

def q3b(file):
    csv = load_data(file)
    days = []
    # print(csv[0])
    for col in csv:
        # print(col)
        days.append(int(col['days']))
    y = np.array(days)
    return y

def q3c(file):
    xVector = q3a(file)
    # print(xVector)
    x = np.array(xVector)
    # print(x)
    xt = np.transpose(x)
    # print(xt)
    #matrix multiplication of xT*x
    z = np.matmul(xt, x)
    # print(z)
    return z

def q3d(z):
    inv = np.linalg.inv(z)
    return inv

def q3e(zInv, x):
    xt = np.transpose(x)

    PI = np.matmul(zInv, xt)
    return PI

def q3f(PI, y):
    YVector = y
    # print(YVector)
    beta = np.matmul(PI, YVector)
    # print(beta)
    return beta


def q4(beta):
    # print(beta[0])
    # print(beta[1])
    xtest = 2021
    ytest = beta[0] + (beta[1]*xtest)
    # print(ytest)
    return ytest

def q5(beta):
    if beta[1] > 0:
        print("Q5a: >")
    elif beta[1] < 0:
        print("Q5a: <")
    else:
        print("Q5a: =")

    print("Q5b: Since there sign here is negative, it shows us that, due to "
          "external factors such as climate change, it appears the number of frozen days"
          " is decreasing")
    pass

def q6(beta):
    negB1 = beta[1] * -1
    xstar = beta[0] / negB1
    return xstar


if __name__ == '__main__':
    # filepath = sys.argv[1]
    filepath = "hw5.csv"
    print("Q3a: \n", q3a(filepath))
    print("Q3b: \n", q3b(filepath))
    q2(q3a(filepath), q3b(filepath))
    z = q3c(filepath)
    print("Q3c: \n", z)
    zInv = q3d(z)
    print("Q3d: \n", zInv)
    PI= q3e(zInv, q3a(filepath))
    print("Q3e: \n", PI)
    beta = q3f(PI, q3b(filepath))
    print("Q3f: \n", beta)
    print("Q4: \n", q4(beta))
    q5(beta)
    print("Q6a:", q6(beta))
    print("Q6b: I would have though that the year would have been much smaller than 2455, since looking over the trends shows a noticebale increase in recents years"
          " of years that have sub 80 frozen days. I would have thought climate change would make this happen in less than 430 more years, "
          "but it obviously makes sense that one day there will no longer be a frozen mendota")



