import numpy
import pandas as pd

def pearson (x, y):
    std1 = numpy.std(x)
    std2 = numpy.std(y)
    cov = numpy.cov(x,y)
    return  (cov[0][1]) / (std1*std2)

def rank_spear(x, y):
    X_arr = pd.DataFrame(x, columns=["values"])
    Y_arr = pd.DataFrame(y, columns=["values"])
    X_arr['Rank'] = X_arr.rank(method='max')
    Y_arr['Rank'] = Y_arr.rank(method='max')
    valX = X_arr['Rank'].array
    valY = Y_arr['Rank'].array
    cov = numpy.cov(valX, valY)
    std1 = numpy.std(valX)
    std2 = numpy.std(valY)

    return (cov[0][1])/(std1*std2)