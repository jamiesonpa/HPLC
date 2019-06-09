#When you dont have a functioning fractionator, this is what happens.

#It beeps at regular intervals.

import time
import winsound

frequency = 440  # Set Frequency To 2500 Hertz
duration = 250  # Set Duration To 1000 ms == 1 second
dropInterval = 4.2 # Set this to the time it takes for your capillaries to drop 1 drop
dropsPerFraction = 3 # Set this to the number of drops you want in each fraction

def main():
    counter = 0

    while counter < 1000:
        if counter % dropsPerFraction == 0:
            beephigh()
            counter = counter +1
        else:
            beep()
            counter = counter + 1


def beep():
    time.sleep(dropInterval)
    winsound.Beep(frequency, duration)

def beephigh():
    time.sleep(dropInterval)
    winsound.Beep(frequency*2, duration)



main()
