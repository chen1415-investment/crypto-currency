def main(dollarBaseLine=0,
         currentAlgord=0,
         pointsNumberToTake=0,
         withdrawAllMoneyAtLast=True):

    #先计算所有的层级
    pointsArray = getTakenPoints(pointsNumberToTake)

    #层级变化得出中间结果
    #TBD 这里要给出一个json[] 需要写明变量类型
    middleArray = pointsArray

    #加上头尾的信息
    headerInfo = {
        'dollar_base_line': dollarBaseLine,
        'current_algord': currentAlgord,
        'points_number_to_take': pointsNumberToTake
    },

    footerInfo = {'remaining_volume': 123123}

    #最后构造整个的返回结果
    result = [headerInfo]
    for item in middleArray:
        result.append(item)
    result.append(footerInfo)
    return result


def getTakenPoints(pointsNumberToTake):
    array = []

    def getPointsRecursively(pointsNumberToTake):
        if pointsNumberToTake == 0:
            return
        array.append({'point': pointsNumberToTake})
        return getPointsRecursively(pointsNumberToTake - 1)

    getPointsRecursively(pointsNumberToTake)
    return array[::-1]


def printFinalRet(ret):
    for VDPair in ret:
        print(VDPair)


if __name__ == '__main__':

    # # for test only
    # ret = main(0, 0, 5, 0)

    print('-----Welcome to use points caculater~!-----')
    dollarBaseLine = int(input("Your baseLine of dollars: "))
    currentAlgord = int(input("Your current volume of ALGORD: "))
    pointsNumberToTake = int(input("Your points number to take(1-5): "))
    withdrawAllMoneyAtLast = bool(
        input("Do you want to take all money at last(true/false): "))

    ret = main(dollarBaseLine, currentAlgord, pointsNumberToTake,
               withdrawAllMoneyAtLast)

    print('\n-----Below is the caculated result----- \n')
    printFinalRet(ret)
