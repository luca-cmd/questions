"""find in an array the missing value to continue the stroke."""


def main(array: list[int]) -> int:
    expected = array[0]
    for n in array:
        if n != expected:
            return expected
        expected = n + 1
    return 0


array = [1, 2, 3, 5, 6, 7, 8]
print(main(array=array))
