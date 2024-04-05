import combinations

def all_subsets(nums):
    subset_list = []
    # range = 7
    for i in range(len(nums) + 1):
        for combo in combinations(nums, i):
            subset_list.append(list(combo))
    return subset_list

# Example usage
nums = [1, 8, 27, 64, 125, 216, 343]
print(all_subsets(nums))

