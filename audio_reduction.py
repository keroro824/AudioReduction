import csv
import math
FILE = 'sample-data1.txt'
RESULT = 'RESULT.txt'
time = 1.0/44100

def reduction(filename, startf=5000, endf=5100, length=10, function):
    results = []
    counter = 0
    with open(filename, 'r') as inputfile:
        linenumber = 0
        for row in csv.reader(inputfile):
            linenumber+=1
            if linenumber>5:        
                results.append(row[0])

    for elem in results:

        if (elem[0]=="[-inf]" or elem[0]=="[inf]"):

        else:
            sample = float(elem[0])
            ratio = 10**(sample/10.0)
            if (ratio>0.9):
                point2 = 10**(float(results[counter+1][0])/10.0)
                point3 = 10**(float(results[counter+2][0])/10.0)

                function = solve(function, ratio, point2, point3)
                determinetime = 0
                errortime = 1
                for i in range(20):
                    error = abs(function(time+i*(time/20.0))-ratio)
                    if (error<errortime):
                        errortime = error
                        determinetime = time+i*(time/20.0)
                break
        counter+=1

    for j in range(length/1000.0*time):
        origin = 10**(float(results[counter-1+j][0])/10.0)
        reduction = abs(function(determinetime+(j-1)*time))
        results[counter-1+j] = 10.0*math.log10(abs(origin-reduction))

    with open(RESULT, 'w') as resultfile:
        for elem in results:
            resultfile.write(elem[0])


def solve(function, point1, point2, point3):
    #TODO
    # function()
    # point1=bsin(t)
    # point2=bsin(t+time)


def main():
    reduction(FILE)

if __name__ == "__main__":
    main()