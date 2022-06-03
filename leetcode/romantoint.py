values = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
}

def subtraction(v1, v2):
    if values.get(v1) == 10 * values.get(v2) or values.get(v1) == 5 * values.get(v2):
        return True
    else:
        return False


def toint(roman):
    val = 0
    strlen = len(roman)
    for i in range(0, strlen):
        if subtraction(roman[i], roman[i-1]) == True and i != 0:
            val -= 2 * values[roman[i-1]]
        val += values[roman[i]]
    return val

print(toint("MCMXCIV"))