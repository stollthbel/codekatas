def increment_left_offset(input, starting_offset):
    start_value = input[starting_offset]
    current_offset = starting_offset
    count = 0
    while (current_offset < len(input) - 1) and (start_value == input[current_offset + 1]):
        current_offset += 1
        count +=1
    return count

def increment_right_offset(input, starting_offset):
    start_value = input[starting_offset]
    current_offset = starting_offset
    while (current_offset > 0) and (start_value == input[current_offset - 1]):
        current_offset -= 1
    return current_offset


def increment_offset(input, starting_offset, direction=1):
    start_value = input[starting_offset]
    current_offset = starting_offset
    count = 0
    while (current_offset < len(input)) and (current_offset >= 0) and (start_value == input[current_offset]):
        current_offset += direction
        count += 1
    return count * direction
    
def is_generalized_palindrome(input):
    #if empty, return -1
    if not input:
        return -1
   

    # Left and right pointers
    left = 0
    right = len(input) - 1


    # Iterate while left pointer < right pointer
    while left < right and  left < len(input)-1 and right > 0:
            if input[left] != input[right]:
                return -1
            print(f"{left},{right}")
            left += increment_offset(input, left, 1)
            right += increment_offset(input, right, -1)


    if left > right:
            return right+1, left - 1
    
    #If generalized palindrome, return the offset
    return left, right



inputs = [
    "aaaba",
    [1,2,2,2,3,3,222,3,2,1],
    [1,2,2,2,3,3,222,222,3,2,1],
    [1,2,2,2,3,3,222,222,222,3,2,1],
    [1,2,2,2,3,3,222,222,222,222,222,3,2,1]
]
for i in inputs:
    print(f"testing input {i}")
    offset = is_generalized_palindrome(i)
    if offset == -1:
        print("The input is not a generalized palindrome")
    else:
        print(f"The input is a generalized palindrome. Offset: {offset} ")


