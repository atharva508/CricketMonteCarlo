import cricketGame
import matplotlib.pyplot as plt
import numpy as np


recordOfRuns = []
NumberOfCenturies = 0
NumberOfHalfs = 0
NumberOfDucks = 0
numSims = 5*(10**5)
sampleSize = 30
for i in range(1,numSims+1):

    tempRuns = 0
    tempCents = 0
    temphalfs = 0
    tempDucks = 0
    for j in range(0,sampleSize):
        currentGame = cricketGame.simulateGame()
        listOfResults = currentGame.startGame()
        tempRuns+= listOfResults[0]
        if(tempRuns==0):
            tempDucks+=1
        tempCents+=listOfResults[1]
        temphalfs+=listOfResults[2]
    NumberOfDucks+=tempDucks
    recordOfRuns.extend([tempRuns])
    NumberOfCenturies+=tempCents
    NumberOfHalfs += temphalfs
    print("{SIMULATION %2d} RUNS SCORED = %3d, CENTURIES = %d, HALF CENTURIES = %d "%(i,tempRuns,tempCents,temphalfs))

mean = np.mean(recordOfRuns)
median = np.median(recordOfRuns)
print("NUMBER OF CENTURIES  = ", NumberOfCenturies)
print("NUMBER OF HALF CENTURIES = ",NumberOfHalfs)
plt.hist(recordOfRuns, bins='auto', edgecolor='blue')

# Add labels and title
plt.xlabel('Runs Scored')
plt.ylabel('Frequency')
plt.title('Cricket Monte Carlo')
plt.text(0.40, 0.90, f"Number Of Simulations : {numSims}", transform=plt.gca().transAxes)
plt.text(0.40, 0.85, f"Mean: {mean:.2f}", transform=plt.gca().transAxes)
plt.text(0.40, 0.80, f"Median: {median}", transform=plt.gca().transAxes)
plt.text(0.40, 0.75, f"NUMBER OF CENTURIES : {NumberOfCenturies}", transform=plt.gca().transAxes)
plt.text(0.40, 0.70, f"NUMBER OF HALF CENTURIES : {NumberOfHalfs}", transform=plt.gca().transAxes)
plt.text(0.40, 0.65, f"NUMBER OF DUCKS : {NumberOfDucks}", transform=plt.gca().transAxes)
plt.text(0.40, 0.60, f"Sample Size : {sampleSize}", transform=plt.gca().transAxes)
# Show the histogram
plt.show()
plt.close()


