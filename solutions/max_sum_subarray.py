# brute force 
def max_sum_subarray(k, arr):
    max_sum = 0
    max_window = 0

    for i in range(len(arr) - k + 1):
        window_sum = 0
        for j in range(i,i + k):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)
    return max_sum

#test case
def main():
    print("maximum of subarray of size k is: " + str(max_sum_subarray(3,[2,1,5,1,3,2,2])))
    print("maximum of subarray of size k is: " + str(max_sum_subarray(2,[2,3,4,1,5])))
main()





