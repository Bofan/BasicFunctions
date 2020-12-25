# 

# This file uses the Lomuto partitioning scheme, 
#   whereby the pivot for each subarray is the last element.
# When an array has already been sorted, 
#   this algorithm degrades to a runtime of O(n^2).

# The partitioning step.
def partition(nums, lo, hi):
    pivot = hi
    i = lo
    while pivot > i:
        if nums[i] >= nums[pivot]:
            nums[i], nums[pivot-1], nums[pivot] = \
              nums[pivot-1], nums[pivot], nums[i]
            pivot -= 1
        else:
            i += 1
    return pivot

# 
def quickSort(nums, lo, hi):
    if lo < hi:
        p = partition(nums, lo, hi)
        quickSort(nums, lo, p-1)
        quickSort(nums, p+1, hi)

def main():
    nums = []
    quickSort(nums, 0, len(nums)-1)
    print(nums)

if __name__ == "__main__":
    main()
