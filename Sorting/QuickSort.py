#!/usr/bin/env python3

"""
This file uses the Lomuto partitioning scheme, 
  whereby the pivot for each sub/array is the last element.
Best- and average-case runtimes for quicksort are O(nlogn).
When an array has already been sorted, 
  this algorithm degrades to a runtime of O(n^2).
"""

def partition(nums, lo, hi):
    """
    Sorts an array into two portions - 
      one with elements smaller than a pre-selected "pivot" element
      and one with elements larger than or equal to said pivot.
    
    Parameters
      > "nums" - The given sub/array.
      > "lo" - The index of the first element in the sub/array to be sorted.
      > "hi" - The index of the last element in the sub/array to be sorted.
    
    Returns
      > "pivot" - The index of the pivot element, now in its correct position.
    """
    pivot = hi
    i = lo
    while pivot > i:
        # Move elements larger than the pivot element 
        #   to the position after said pivot.
        if nums[i] > nums[pivot]:
            nums[i], nums[pivot-1], nums[pivot] = \
              nums[pivot-1], nums[pivot], nums[i]
            pivot -= 1
        else:
            i += 1
    return pivot

def quickSort(nums, lo, hi):
    """
    Recursively sorts the higher- and lower-valued halves of the sub/array.
    
    Parameters
      > "nums" - The given sub/array.
      > "lo" - The index of the first element in the sub/array to be sorted.
      > "hi" - The index of the last element in the sub/array to be sorted.
    
    Returns
        NONE
    """
    if lo < hi:
        p = partition(nums, lo, hi)
        # After the call to the partition() function, the element at 
        #   position p will be at the correct position in the array.
        quickSort(nums, lo, p-1)
        quickSort(nums, p+1, hi)

def main():
    nums = []
    quickSort(nums, 0, len(nums)-1)
    print(nums)

if __name__ == "__main__":
    main()
