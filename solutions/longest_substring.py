# use hashmap 
def longest_substring(str, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

    
        while len(char_frequency) > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length

# test case
def main():
    print("length of the smallest substring is: " + str(longest_substring("araaci", 2)))
    print("length of the smallest substring is: " + str(longest_substring("araaci", 1)))
    print("length of the smallest substring is: " + str(longest_substring("cbbebi", 3)) )

main()



