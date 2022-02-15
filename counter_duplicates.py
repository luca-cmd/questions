"""count the duplicates of a word."""


def main(string: str) -> dict[str, int]:
    dictionary: dict[str, int] = {}
    for c in string:
        char_count = string.count(c)
        if char_count > 1:
            dictionary[c] = char_count
    return dictionary


print(main("hello"))
