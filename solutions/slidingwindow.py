def find_average(k,arr):
    result = [ ]
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr [windowEnd] #add the next element 
        if windowEnd >=  k - 1:
            result.append(windowSum / k)
            windowSum -= arr[windowStart]
            windowStart -= arr [windowStart]
            windowStart += 1
    return result


#test case
def main():
    result = find_average (5, [1,3,2,6,-1,4,1,8,2] )
    print("Average  subarray of size k is : "  + str(result))
main()

# software




