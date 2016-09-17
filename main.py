#Gustav LD 2016

print("Number of values: ")
numberOfValues = int(input())

xValues = []
yValues = []

for i in range(numberOfValues):
    print("X"+str(i)+":")
    xValues.append(float(input()))

for i in range(numberOfValues):
    print("Y"+str(i)+":")
    yValues.append(float(input()))

print("Enter minimum value for coefficient")
minVal = float(input())

print("Enter maximum value for coefficient")
maxVal = float(input())

print("Enter step")
step = float(input())


smallestError = None
bestResult = 0

c = minVal

while c < maxVal:
    sumOfErrorsSquared = 0.0
    
    for i in range(numberOfValues):
        error = c*xValues[i]**2 - yValues[i]

        sumOfErrorsSquared += error**2

    if smallestError is None or sumOfErrorsSquared < smallestError:
        smallestError = sumOfErrorsSquared
        bestResult = c
        
    c+=step

print("y = "+str(bestResult)+"x^2 fits the data best")
