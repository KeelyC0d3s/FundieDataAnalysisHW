import random

def rolldie():
    return random.randint(1,6)

#print(rolldie()) 

def rolldice(numdice):
    total=0
    for x in range(numdice):
        #print(rolldie())
        total = total + rolldie()
    return total

#print(rolldice(2)) 

def createdict(numdice):
    #start = numdice * 1
    #end = numdice * 6
    #start = 2
    #end = 12
    results = {}
    for x in range (numdice, (numdice * 6)+1):
        results[x] = 0
    return results

def diceroll(numdice, rolls):
    results = createdict(numdice)
    for x in range (rolls):
        roll = rolldice(numdice)
        #print(roll)

        if roll in results:
            value = results.get(roll)
            newValue = value + 1
            results[roll] = newValue
        #else:
            #results[roll] = 1
    return results


print(diceroll(2, 1000))

