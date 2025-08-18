def getSecondLargest(arr):
    if len(set(arr)) < 2:
        return None  

    largest = second_largest = float('-inf')

    for number in arr:
        if number > largest:
            second_largest = largest 
            largest = number          
        elif largest > number > second_largest:
            second_largest = number

    return second_largest

arr = [12, 35, 1, 10, 34, 1]
result = getSecondLargest(arr)
print(f"The second largest element is: {result}")

arr2 = [5, 5, 5]
result2 = getSecondLargest(arr2)
print(f"The second largest element in [5, 5, 5] is: {result2}")