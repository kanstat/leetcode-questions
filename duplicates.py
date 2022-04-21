#  Contains Duplicate
# Easy

# 4419

# 946

# Add to List

# Share
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

def duplicate(nums):
    l = len(nums)
    visited = list()
    for i in range(l):
        if nums[i] not in visited:
            visited.append(nums[i])
        else:
            return True
    return False


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 7, 8, 10, 12, 14, 17, 3]
    print(duplicate(nums))
