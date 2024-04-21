import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    '''
    return the list of bmi(s) of the inputted weights and heights
    formula to calculate the bmi => weight/(height)**2
    '''
    try:
        height = np.square(np.array(height))
        weight = np.array(weight)
        bmi = np.divide(weight, height)
        bmi = list(bmi)
        return bmi
    except:
        print("input error")
        return []
    #your code here
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        return [True if value > limit else False for value in bmi]
    except:
        print("input error")
        return []

