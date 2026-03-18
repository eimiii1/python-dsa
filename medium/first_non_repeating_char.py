# Problem 7: First Non-Repeating Character

# Find the first character in a string that appears only once
# If all characters repeat, return None

# Example:
# Input: "leetcode"
# Output: 'l' (first character that appears once)

def first_unique_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char in s:
        if freq[char] == 1:
            return char
        
    return None

strings = ["leetcode", "bakla", "aabb"]

for string in strings:
    print(first_unique_char(string))