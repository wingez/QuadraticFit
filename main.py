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


leastSquare = None
bestValue = 0

c = minVal

while c < maxVal:
    sumOfSquares = 0.0
    for i in range(numberOfValues):
        differens = c*xValues[i]**2 - yValues[i]
        sumOfSquares += differens**2

    if leastSquare is None or sumOfSquares < leastSquare:
        leastSquare = sumOfSquares
        bestValue = c
        
    c+=step

print("y = "+str(bestValue)+"x^2 fits the data best")
