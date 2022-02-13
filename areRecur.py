"""Check if two string are the reverse of the other one."""


def main(s1: str, s2: str):
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] == s2[(len(s1) - 1) - i]:
                return True
    return False


print(main(s1="ciao", s2="oaic"))
