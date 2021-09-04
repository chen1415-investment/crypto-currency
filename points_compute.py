from constants import profitTakenMap, smallerProfitTakenMap, fiftyOnlyMap
import math


def main(dollarBaseLine=0,
         currentAlgord=0,
         pointsNumberToTake=0,
         computeByRemaining=False,
         withdrawAllMoneyAtLast=False):

    #先计算所有的层级
    pointsArray = getTakenPoints(pointsNumberToTake)

    #层级变化得出中间结果
    #TBD 这里要给出一个json[] 需要写明变量类型
    middleArray = computeMiddleParams(dollarBaseLine, int(currentAlgord),
                                      pointsArray, computeByRemaining)

    #加上头尾的信息
    headerInfo = {
        'dollar_base_line':
        '$' + str(dollarBaseLine),
        'current_ALGORD':
        currentAlgord,
        'balance_point':
        '$' + str(float('%.3f' % (dollarBaseLine / currentAlgord))),
        'points_number_to_take':
        pointsNumberToTake
    },

    def getFooterVolume():
        if withdrawAllMoneyAtLast:
            middleArray[-1]['number_to_sell'] = 'all'
            middleArray[-1].pop('remaining_currency')
            return 0
        return middleArray[-1]['remaining_currency']

    footerInfo = {
        'take_all_money_at_last': withdrawAllMoneyAtLast,
        'remaining_volume': getFooterVolume()
    }

    #最后构造整个的返回结果
    result = [headerInfo]
    for item in middleArray:
        result.append(item)
    result.append(footerInfo)
    return result


def computeMiddleParams(dollarBaseLine, currentAlgord, pointsArray,
                        computeByRemaining):
    '''
    dollarBaseLine: 10000   
    currentAlgord: 7xxx

    pointsArray: json[]
    {'point': 1, 'taken_profit': '$50'}
    {'point': 2, 'taken_profit': '$100'}
    {'point': 3, 'taken_profit': '$150'}
    {'point': 4, 'taken_profit': '$200'}
    {'point': 5, 'taken_profit': '$500'}
    {'point': 6, 'taken_profit': '$1000'}
    '''

    for index in range(len(pointsArray)):

        level = pointsArray[index]
        takenProfit = profitTakenMap[level['point']]['value']
        '''
        这里如果index==0 意味着当前的taken profit是50 
        这是第一级take的profit 那么currentAlgord就是原样
        如果不是的话 那么就要用currentAlgord减掉之前的和
        '''
        if index != 0:
            if computeByRemaining:
                currentAlgord = pointsArray[index - 1]['remaining_currency']
            else:
                currentAlgord = currentAlgord
        priceToSell = float('%.3f' %
                            ((dollarBaseLine + takenProfit) / currentAlgord))
        numberToSell = math.ceil(takenProfit / priceToSell)
        level['price_to_sell'] = '$' + str(priceToSell)
        level['number_to_sell'] = numberToSell
        if computeByRemaining:
            level['remaining_currency'] = currentAlgord - numberToSell
        else:
            level['remaining_currency'] = currentAlgord
    return pointsArray


def getTakenPoints(pointsNumberToTake):
    array = []

    def getPointsRecursively(pointsNumberToTake):
        if pointsNumberToTake == 0:
            return

        array.append({
            'point':
            pointsNumberToTake,
            'taken_profit':
            profitTakenMap[pointsNumberToTake]['text']
        })
        return getPointsRecursively(pointsNumberToTake - 1)

    getPointsRecursively(pointsNumberToTake)
    return array[::-1]


def printFinalRet(ret):
    for VDPair in ret:
        print(VDPair)


if __name__ == '__main__':

    # for test only
    # ret = main(0, 0, 5, 0)

    print('-----Welcome to use points caculater~!-----')
    dollarBaseLine = input("Your baseLine of dollars -- default 10000: ")
    if dollarBaseLine == '':
        dollarBaseLine = 10000
    else:
        dollarBaseLine = int(dollarBaseLine)

    currentAlgord = int(input("Your current volume of ALGORD: "))

    pointsNumberToTake = input(
        "Your points number to take(1-6) -- default 6: ")
    if pointsNumberToTake == '':
        pointsNumberToTake = 6
    else:
        pointsNumberToTake = int(pointsNumberToTake)

    computeByRemaining = input(
        "Do you want to compute by remaning(1/0) - default False: ")
    if computeByRemaining == '':
        computeByRemaining = False
    else:
        computeByRemaining = bool(computeByRemaining)

    withdrawAllMoneyAtLast = input(
        "Do you want to take all money at last(1/0) - default False: ")
    if withdrawAllMoneyAtLast == '':
        withdrawAllMoneyAtLast = False
    else:
        withdrawAllMoneyAtLast = bool(withdrawAllMoneyAtLast)

    ret = main(dollarBaseLine, currentAlgord, pointsNumberToTake,
               computeByRemaining, withdrawAllMoneyAtLast)

    print('\n-----Below is the caculated result-----')
    printFinalRet(ret)
