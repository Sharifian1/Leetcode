


nums1 = [1,2]
nums2 = [3,4]
Array = list[int]

def sortedArray ():
    newArray = nums1 + nums2
    a = newArray
    
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            temp = int
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp

    return newArray

resultArray = sortedArray()

n = len(resultArray)

if n % 2 == 0: # if the length of the array is even
        # calculate the middle two numbers
    middle1 = (resultArray)[n//2]
    middle2 = (resultArray)[n//2 - 1]
    median = (middle1 + middle2) / 2
    print(median)
else: # if the length of the array is odd
        # find the middle number
    median = (resultArray)[n//2]
    print(median)

