def plusOne(digits):
    digits = digits[::-1]
    curr = 1
    i = 0

    while curr:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                curr = 0
        else:
            digits.append(1)
            curr = 0
        i += 1
    return digits[::-1]