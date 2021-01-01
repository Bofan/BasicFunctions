#!

"""
T I M
"""

def insertionSort(nums, lo, hi):
    """
    
    """
    for i in range(lo+1, hi+1):
        to_sort = nums[i]
        j = i - 1
        while nums[j] > to_sort and j >= lo:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = to_sort

def merge(nums, lo, mid, hi):
    """
    Combines the sorted sub-arrays.
    """
    size = run
    lenL, lenR = mid-lo+1, hi-mid
    left, right = [], []
    for i in range(lenR):
        left.append(nums[i+1])
    for i in range(lenL):
        right.append(nums[i+m+1])
    # Compare and merge the two smaller sub-arrays into a larger sub/array.
    i, j, k = 0, 0, lo
    while i < lenL and j < lenR:
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    # Copy over any remaining elements of the two smaller sub-arrays.
    while i < lenL:
        nums[k] = left[i]
        k += 1
        i += 1
    while j < lenR:
        nums[k] = right[j]
        k += 1
        j += 1

def timSort(nums, n, run):
    """
    The original array is split into two parts. [...]
    """
    # Sort the sub-arrays of length "run".
    for i in range(0, n, run):
        insertionSort(nums, i, min(i+run-1, n-1))
    # Merge sub-arrays beginning at size "run".
    size = run
    while size < n:
        for lo in range(0,n, 2*size):
            mid = lo + size - 1
            hi = min(lo + 2*size - 1, n - 1)
        merge(nums, lo, mid, hi)
        size *= 2

def main():
    nums = []
    n = len(nums)
    timSort(nums, n, run = 32)
    print(nums)

if __name__ == "__main__":
    main()
