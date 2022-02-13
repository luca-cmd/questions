# Google coding interview question: sum of two

Array = list[int]
array1 = [1, 4, 6, 7]
array2 = [2, 5, 7, 4]

def sum_of_two(array1: Array, array2: Array, target: int) -> bool:
    complements = set(())
    for v in array1:
        complements.add(target - v)

    for x in complements:
        for v in array2:
            if v == x:
                return True
    return False

print(sum_of_two(array1=array1, array2=array2, target=10))
