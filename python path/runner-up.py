if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    # print(arr)
    
    # # finding the max number

    arr_max = arr[0]
    for a in arr:
        if a > arr_max:
            arr_max = a
            
    # print(arr_max)
    
    # # removing the max number from arr
    max_index = []
    max_index = max_index.append(arr.index(arr_max))
    arr = arr.pop(max_index)
    
    print((arr.index(arr_max)))
    
    # # finding the max number again hence the runner-up
    
    print(arr)
    
    # arr_max = arr[0]
    # for a in arr:
    #     if a > arr_max:
    #         arr_max = a
            
    # print (arr_max)
