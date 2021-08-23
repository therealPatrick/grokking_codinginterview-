import math

def smallest_subarr(s, arr):
    window_sum = 0
    min_length = math.inf
    window_start = 0

    for window_end in range (0, len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == math.inf:
        return 0
    return min_length


def main():
    print("smallest subarray length: " + str(smallest_subarr(7,[2,3,5,1,6,7])))
    print("smallest subarray length: " + str(smallest_subarr(2,[2,3,5,6,4,7])))


main()


