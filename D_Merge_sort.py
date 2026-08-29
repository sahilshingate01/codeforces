import sys
input = sys.stdin.readline

def mergesort(arr):
    n = len(arr)
    temp = [0] * n
    width = 1
    while width < n:
        for low in range(0, n, 2 * width):
            mid = min(low + width - 1, n - 1)
            high = min(low + 2 * width - 1, n - 1)
            if mid >= high:
                continue
            # merge arr[low..mid] and arr[mid+1..high]
            i, j, k = low, mid + 1, low
            while i <= mid and j <= high:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]; i += 1
                else:
                    temp[k] = arr[j]; j += 1
                k += 1
            while i <= mid:
                temp[k] = arr[i]; i += 1; k += 1
            while j <= high:
                temp[k] = arr[j]; j += 1; k += 1
            arr[low:high+1] = temp[low:high+1]
        width *= 2

n = int(input())
arr = list(map(int, input().split()))
mergesort(arr)
sys.stdout.write(' '.join(map(str, arr)) + '\n')