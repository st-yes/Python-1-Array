import numpy as np
def slice_me(family: list, start: int, end: int) -> list:
    try:
        family_array = np.array(family)
        print(f"My shape is : {family_array.shape}")
        sliced_array = family_array[start:end]
        print(f"My new shape is : {sliced_array.shape}")
        return [list(array) for array in sliced_array]
    except:
        print("input error")
        return []
    