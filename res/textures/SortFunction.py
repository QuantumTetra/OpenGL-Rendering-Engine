def sortBubble(L):
    for i in range(0,len(L)):
        for j in range(1,len(L)):
            if L[j] < L[j-1]:
                temp = L[j-1]
                L[j-1] = L[j]
                L[j] = temp
    return L

def sortInsert(L):
    for i in range(1,len(L)):
        val = L[i]
        pos = i
        while pos > 0 and L[pos - 1] > val:
            L[pos] = L[pos - 1]
            pos -= 1
        L[pos] = val
    return L
