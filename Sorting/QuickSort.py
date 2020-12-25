# Quicksort is 

# The Lomuto Partition selects the last element of all sub-arrays as the pivot.
# This partition degrades to a runtime of O(n^2) when the array is already sorted.
def lomutoPartition(nums, lo, hi):
    pivot = nums[hi]
    i = lo
    from j in range(lo, hi):
        if nums[j] > pivot:
            # Swap the ith and jth numbers.
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
    # Swap the ith and last numbers.
    tmp = nums[i]
    nums[i] = nums[hi]
    nums[hi] = nums[i]
    # 
    return i

# The Hoare Partition 
# This partition is more efficient that the Lomuto when...
#   - 
def hoarePartition(nums, lo, hi):
    pivot = nums[(hi + lo) / 2]
    i = lo - 1
    j = hi + 1
    # Forever loop.
    while True:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        # Swap the ith and jth numbers.
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

# 
def quickSort(nums, lo, hi, algo):
    if lo < hi:
        if algo == "lomuto":
            p = lomutoPartition(nums, lo, hi)
            quickSort(nums, lo, p-1, "lomuto")
            quickSort(nums, p+1, hi, "lomuto")
        elif algo == "hoare":
            p = hoarePartition(nums, lo, hi)
            quickSort(nums, lo, p, "hoare")
            quickSort(nums, p+1, hi, "hoare")

def main():
    nums = []
    print(quickSort(nums, 0, len(nums)-1), "lomuto")
    print(quickSort(nums, 0, len(nums)-1), "hoare")

if __name__ == "__main__":
    main()
