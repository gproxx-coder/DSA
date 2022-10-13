"""
This is the optimal solution to this problem. Here we use three pointers to achieve three-way partitioning.
Let me put it simply. We will use three pointers that are low, mid, and high.  Initially, we point the low and
mid-pointers to the start that is the first element of the input array, and the high pointer to the end that is the last
element of the input array.

So, basically this algorithm is based on the fact all the numbers from arr[0] to arr[low-1] will be 0s and all the
numbers from arr[high+1] to arr[n-1] will be 2s and arr[low] to arr[mid-1] will be 1s
arr[0] to arr[low-1] ----------0
arr[high+1] to arr[n-1]------2
arr[low] to arr[mid-1]--------1
That is all the numbers to the left of low will be 0 and all the numbers to the right of high will be 1.
How to achieve this? we will traverse the input array until mid<=high. We will check three conditions that is
when arr[mid]==0, arr[mid]==1, and arr[mid]==2. See the piece of code below:
"""

arr = [0, 2, 1, 0, 2, 0, 0, 1, 1, 1, 0, 2, 1, 2, 1, 2]


def counter_solution(arr):
    counter = {}
    for num in arr:
        counter[num] = counter.get(num, 0) + 1

    # new_list = []
    # for key in sorted(counter.keys()):
    #     new_list.extend([key] * counter[key])

    # If we make sure there will be only 0, 1 & 2 digits always presents then below would work
    new_list = [0] * counter[0] + [1] * counter[1] + [2] * counter[2]

    print(new_list)


# counter_solution(arr)


def dutchsort(arr, n):
    low = 0
    high = n - 1
    mid = 0
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low = low + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high = high - 1
    return arr

print(dutchsort(arr, len(arr)))