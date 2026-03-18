# Problem 6: Remove Duplicates and Sort

def remove_duplicates_and_sort(nums):
    unique_list = []
    for num in nums:
        if num not in unique_list:
            unique_list.append(num)

    for i in range(len(unique_list) - 1):
        for j in range(len(unique_list) - i - 1):
            if unique_list[j] > unique_list[j + 1]:
                temp = unique_list[j]
                unique_list[j] = unique_list[j + 1]       
                unique_list[j + 1] = temp

    return unique_list

nums = [4, 2, 2, 8, 3, 3, 1]
print(remove_duplicates_and_sort(nums))