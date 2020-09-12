def partition(array, lo, hi):
    pivot =array[hi]
    i=lo-1
    for j in range(lo, hi-1):
        if array[j]<=pivot :
            i+=1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[hi]=array[hi],array[i+1]
    return i+1,array
def QuickSort(array):
    if len(array)<2:
        return array
    else:
        pivot,array=partition(array,0,len(array)-1)
        return QuickSort(array[:pivot])+[array[pivot]]+QuickSort(array[pivot+1:])

a=[1,4,3,5,8,9]
print(QuickSort(a))