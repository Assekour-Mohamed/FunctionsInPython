def max(tab):
    max = tab[0]
    for i in tab :
        if max < i:
            max = i
    return max 
def min(tab):
    min = tab[0]
    for i in tab :
        if min > i:
            min = i
    return min
def Revers(tab):
    t = []
    for i in range(5):
        t.append(tab[5-1-i])
       
    return t 


Tab = [1,3,4 , 5,44]
print(min(Tab))
print(max(Tab))
print(Revers(Tab))     
