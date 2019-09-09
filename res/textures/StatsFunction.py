import math
import sys

def RepresentsFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

def getValuesPrompt():
    lists = []
    
    quits = False
    print("Entering a blank value will finish data")
    while not quits:
        ins = input("value: ")
        if RepresentsFloat(ins):
            lists.append(float(ins))
        else:
            quits = True
    return lists

def findQs(lists):
    qs = []
    
    max1 = 0.0
    min1 = sys.float_info.max
    
    for x in lists:
        if x > max1:
            max1 = x
    for x in lists:
        if x < min1:
            min1 = x
    
    for x in lists:
        closest = sys.float_info.max
        close = 0.0
        for y in lists:
            if not y == x:
                temp = abs(x-y)
                if temp < closest:
                    closest = temp
                    close = y
        q = abs(x - close) / abs(max1 - min1)
        qs.append(q)
    return(qs)

def findMean(lists):
    sums = 0
    for num in lists:
        sums += num
    sums /= float(len(lists))
    return sums

def findMedian(lists):
    if len(lists) % 2 == 0:
        dist = len(lists) // 2
        return (lists[dist - 1] + lists[dist]) / 2.0
    else:
        dist = len(lists) // 2
        return lists[dist]

def findRange(lists):
    max1 = 0.0
    min1 = sys.float_info.max
    for x in lists:
        if x > max1:
            max1 = x
    for x in lists:
        if x < min1:
            min1 = x
    return max1 - min1

def findMode(lists):
    currentMode = 0.0
    highFreq = 0
    editingSum = 0
    for num in lists:
        editingSum = 0
        for num2 in lists:
            if num == num2:
                editingSum += 1
        if editingSum > highFreq:
            highFreq = editingSum
            currentMode = num
    return currentMode

def findStandardDeviation(lists):
    average = findMean(lists)
    sums = 0.0
    for item in lists:
        sums += ((item - average) * (item - average))
    sums /= float(len(lists)) - 1.0
    sums = math.sqrt(sums)
    return sums

def findRelativeStandardDeviation(lists):
    return 100.0 * (findStandardDeviation(lists) / findMean(lists))
