import random

def rolldie():
    return random.randint(1, 6)

def rolldice(num_dice):
    result = 0
    for roll in range(num_dice):
        result += rolldie()
    return result

def dicerolls(num_dice, dicerolls):
    results = {}
    for roll in range(dicerolls):
        # for roll in range(num_dice):
        #     roll_value = generateNumber(1, 6)
        #     if roll_value in results:
        #         value = results.get(roll_value)
        #         newValue = value + 1
        #         results[roll_value] = newValue
        #     else:
        #         results[roll_value] = 1
        roll_value = rolldice(num_dice)
        if roll_value in results:
            value = results.get(roll_value)
            newValue = value + 1
            results[roll_value] = newValue
        else:
            results[roll_value] = 1
    return results

print(dicerolls(2, 1000))