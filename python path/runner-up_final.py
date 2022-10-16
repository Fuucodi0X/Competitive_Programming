if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    
    # # finding the max number

    
    arr_max = arr[0]
    for a in arr:
        if a > arr_max:
            arr_max = a
            
    
    # # removing the max number from arr
    
        # max_index = [i for i in range(len(arr)) if arr_max == arr[i]]
    
        # for a in max_index:
        #     arr.pop(a)
    for a in range(arr.count(arr_max)):
        arr.remove(arr_max)    
        
    
    # # finding the max number again hence the runner-up
    
    
    arr_max = max(arr)
    
    print (arr_max)
