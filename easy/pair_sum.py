# Problem 5: Find Pairs that Sum to Target

# Find all pairs of numbers in a list that sum to a target
# Each number can only be used once

# Example:
# find_pairs([1, 2, 3, 4, 5], target=6)
# Output: [(1, 5), (2, 4)]

def find_pairs(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = (nums[i], nums[j])
                pairs.append(pair)
            
    return pairs

nums = [1, 3, 5, 7, 9]
target = 10

print(find_pairs(nums, target))