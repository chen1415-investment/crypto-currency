def main(dolladollrBaseLine, currentAlgord,
         pointsNumberToTake, withdrawAllMoneyAtLast):

    ret = [
        ("dolladollrBaseLine", dolladollrBaseLine),
        ("currentAlgord", currentAlgord),
        ("pointsNumberToTake", pointsNumberToTake),
        ("withdrawAllMoneyAtLast", withdrawAllMoneyAtLast),

    ]

    return ret


def printFinalRet(ret):
    for i in ret:
        print(i)


if __name__ == '__main__':
    print('-----Welcome to use points caculater~!-----')
    dolladollrBaseLine = input("Your baseLine of dollars: ")
    currentAlgord = input("Your current volume of ALGORD: ")
    pointsNumberToTake = input("Your points number to take(1-5): ")
    withdrawAllMoneyAtLast = input(
        "Do you want to take all money at last(true/false): ")

    ret = main(dolladollrBaseLine, currentAlgord,
               pointsNumberToTake, withdrawAllMoneyAtLast)

    print('\n-----Below is the caculated result----- \n')
    printFinalRet(ret)
