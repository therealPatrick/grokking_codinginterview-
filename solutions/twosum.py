def twoSum(nums, target):
    hash_map = { }
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash_map:
            return[hash_map[diff],i]
        hash_map[num] = i
    return
# time = O(N) where N is the number of elements in a given array | space = O(N) worst case we will be pushing N elements in the hashtable 
def main():
    print(twoSum([2,7,11,15], 9))
main()