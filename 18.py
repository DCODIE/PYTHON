#bubblesort
def bubbleSort(a,*var):

    l=a+ list(var)

    for i in range(1,len(l)):
        for j in range(0,len(l)-1):
            if(l[j]>l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]
    print(l)
a = [54,26,93,17,77,31,44,55,20]
bubbleSort(a,3,2,4,1)

