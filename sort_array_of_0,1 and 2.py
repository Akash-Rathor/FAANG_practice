def sort012(arr,n):
    low = mid = 0
    high = n-1

    while mid<high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        if arr[mid]==2:
            arr[high],arr[mid]=arr[mid],arr[high]
            high-=1
        if arr[mid]==1:
            mid+=1

    return arr

arr = [0,1,2,0,0,2,1]
n = len(arr)
print(sort012(arr,n))