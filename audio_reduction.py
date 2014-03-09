import csv
import math
import numpy as np
import scipy as sp
from scipy import optimize
FILE = 'sample-data1.txt'
RESULT = 'RESULT.txt'
time = 1.0/44100

def reduction(filename, startf=5000.0, endf=5100.0, length=10.0):
    results = []
    counter = 0
    with open(filename, 'r') as inputfile:
        linenumber = 0
        for row in csv.reader(inputfile):
            linenumber+=1
            if linenumber>5: 
                if (row[0]!="[-inf]" and row[0]!="[inf]"):   
                    results.append(row[0])

    for elem in results:

        sample = float(elem)
        ratio = 10**(sample/10.0)
        if (ratio>0.9):
            point2 = 10**(float(results[counter])/10.0)
            point3 = 10**(float(results[counter+1])/10.0)

            amp = solve(func, point2, point3)
            determinetime = 0
            errortime = 1
            for i in range(20):
                error = abs(function((time+i*(time/20.0)), amp, startf, endf, length)-ratio)
                if (error<errortime):
                    errortime = error
                    determinetime = time+i*(time/20.0)
            break
    counter+=1

    for j in range((int)(length/1000.0*time)):
        origin = 10**(float(results[counter-1+j])/10.0)
        reduction = abs(function(determinetime+(j-1)*time))
        results[counter-1+j] = 10.0*math.log10(abs(origin-reduction))

    with open(RESULT, 'w') as resultfile:
        for elem in results:
            resultfile.write(elem)


def solve(func, point1, point2):
    print (point1, point2)
    a= abs(sp.optimize.newton(func, -800, None, (point1, point2)))
    return a

def function(t, a, start_fr, end_fr, length):
    k = math.pow(end_fr/start_fr, 1.0/length);
    den = math.log(k)
    num = math.pow(k,t)-1
    rest = math.pi*2*start_fr
    result = math.sin(1.0*num*rest/den)
    return a*result


def func(a, point1, point2):
    #TODO
    # function()
    # point1=asin(t)
    # point2=asin(t+time)
    # t=arcsin(point1/a)
    # t+time=arcsin(point2/a)
    return np.arcsin(point1/a)-np.arcsin(point2/a)-time
    


def main():
    reduction(FILE)

if __name__ == "__main__":
    main()