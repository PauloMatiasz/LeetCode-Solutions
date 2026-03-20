# two_sum.py
# Solves the Two Sum problem: returns indices of two numbers that add up to the target

def two_sum(nums, target):
    """
    Finds indices of two numbers in nums that sum to target.
    
    Args:
        nums (list[int]): List of integers
        target (int): Target sum
    
    Returns:
        list[int]: Indices of the two numbers, or an empty list if none found.
    """
    seen = {}  # Stores numbers we've seen and their indices

    for i, num in enumerate(nums):
        complement = target - num  # Number needed to reach target
        if complement in seen:
            return [seen[complement], i]  # Return indices if complement exists
        seen[num] = i  # Save current number with its index

    return []  # No solution found

# Example usagegit ss
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices found for target {target}: {result}")