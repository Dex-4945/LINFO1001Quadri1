#Every function has been tested with seeds going from -900 to 900 and an interval of 500, but a little more would have triggered a timeout
#So I settled on seeds from -100 to 100 and an interval of 100

#Are the generated numbers comprised between 0 and the upper limit defined by the decided interval.
def intervalRespected(tempSeed, tempInterval, tempPRNG):
    output = memorise(tempSeed, tempInterval, tempPRNG)
    for i in range(tempInterval):
        if output[i] < 0 or output[i] >= tempInterval:
            return False
    return True

#Will all the numbers ranging from 0 to the upper limit defined by the decided interval eventually be drawn.
def intervalComplete(tempSeed, tempInterval, tempPRNG):
    all = []
    prng = tempPRNG(tempSeed, tempInterval)
    for i in range(tempInterval):
        all.append(i)
    for j in range(tempInterval * 10):
        all[prng.next_int()] = -1
    for k in range(tempInterval):
        if all[k] != -1:
            return False
    return True

#Would the seed change, will the sequence effectively change accordingly and
#Would we try the same seed multiple times, will the sequence remain the same?
def seedNoImpact(tempSeed, tempInterval, tempPRNG):
    initOutput = memorise(tempSeed, tempInterval, tempPRNG)
    for otherSeed in range(-100, 100):
        otherOutput = memorise(otherSeed, tempInterval, tempPRNG)
        if abs(tempSeed) != abs(otherSeed) and initOutput == otherOutput:
            return False
        if abs(tempSeed) == abs(otherSeed) and initOutput != otherOutput:
            return False
    return True

#Test if the difference between two adjacent or numbers is at least 6 times the same.
#In that case function discards the PRNG
def notCycling(tempSeed, tempInterval, tempPRNG):
    output = memorise(tempSeed, tempInterval, tempPRNG)
    delta = []
    same = 0
    highest = 0
    for index in range(tempInterval - 1):
        delta.append(abs(output[index] - output[index + 1]))
    for index in range(tempInterval - 6):
        if delta[index] == delta[index + 1]:
            same += 1
        else:
            if same > highest:
                highest = same
            same = 0
    if highest > 6:
        return False
    return True

#Function used to output a sequence from the PRNG and send it to the needed functions as a list.
def memorise(tempSeed, tempInterval, tempPRNG):
    output = []
    prng = tempPRNG(tempSeed, tempInterval)
    for index in range(tempInterval):
        output.append(prng.next_int())
    return output

#Main function calling one by one each method to test the PRNG. 
#Tests are conducted on seeds from -100 to 100 with a 100 range wide interval
def is_correct(PRNG):
    interval = 100
    for seed in range(-100, 100):
        if not intervalRespected(seed, interval, PRNG):
            return False
        if not intervalComplete(seed, interval, PRNG):
            return False
        if not notCycling(seed, interval, PRNG):
            return False
        if not seedNoImpact(seed, interval, PRNG):
            return False
    return True
