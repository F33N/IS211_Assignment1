def listDivide(numbers, divide=2):
    x = 0
    for everyNum in numbers:
        if everyNum % divide == 0:
            x = x + 1
        return x


class ListDivideException:
    pass


def testListDivide():
    if not listDivide([1, 2, 3, 4, 5]) == 2:
        raise ListDivideException
    if not listDivide([2, 4, 6, 8, 10]) == 5:
        raise ListDivideException
    if not listDivide([30, 54, 63, 98, 100], divide=2) == 2:
        raise ListDivideException
    if not listDivide([]) == 0:
        raise ListDivideException
    if not listDivide([1, 2, 3, 4, 5], 1) == 5:
        raise ListDivideException
