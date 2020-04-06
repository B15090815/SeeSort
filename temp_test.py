from util import shuffle


def bubbleSort(data: list):
    N = len(data)
    flag = False
    k = 0
    for i in range(N):

        if flag:
            print(k)
            return data
        flag = True
        for j in range(N - i - 1):
            k += 1
            if data[j] > data[j + 1]:
                flag = False
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def inertSort(data: list):
    N = len(data)
    for i in range(1, N):
        for j in range(i):
            if data[i] < data[j]:
                data[j], data[i] = data[i], data[j]
    return data


def merge(a: list, l1: int, r1: int, l2: int, r2: int):
    temp = []
    i = l1
    j = l2

    while i <= r1 and j <= r2:
        if a[i] < a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1

    while i <= r1:
        temp.append(a[i])
        i += 1

    while j <= r2:
        temp.append(a[j])
        j += 1

    i = l1
    j = 0
    while j < len(temp):
        a[i] = temp[j]
        i += 1
        j += 1


def innerMergeSort(data: list, l: int, r: int):
    if l < r:
        mid = (r + l) >> 1
        innerMergeSort(data, l, mid)
        innerMergeSort(data, mid + 1, r)
        merge(data, l, mid, mid + 1, r)


def mergeSort(data: list):
    innerMergeSort(data, 0, len(data) - 1)
    return data


def swap(data: list, i: int, j: int):
    data[i], data[j] = data[j], data[i]


def adjustHeap(data: list, root: int, length: int):
    N = length
    k = root * 2 - 1
    while k < N:
        if k + 1 < N and data[k] < data[k + 1]:
            k += 1

        root -= 1
        if data[root] < data[k]:
            swap(data, root, k)
            root = k + 1
            k = root * 2 - 1
        else:
            break


def buildHeap(data: list):
    N = len(data)
    i = N >> 1

    while i > 0:
        adjustHeap(data, i, N)
        i -= 1


def heapSort(data: list):
    buildHeap(data)
    k = len(data) - 1
    while k > 0:
        swap(data, 0, k)
        adjustHeap(data, 1, k)
        k -= 1


def partion(data: list, left: int, right: int):
    k = data[left]
    i = left + 1
    j = right

    while True:
        while data[i] < k and i < right:
            i += 1

        while data[j] > k:
            j -= 1

        if i >= j:
            break

        swap(data, i, j)

    data[left] = data[j]
    data[j] = k
    return j

def InnerquickSort(data:list, p:int, r:int):
    if p < r:
        mid = partion(data, p, r)
        InnerquickSort(data, p, mid-1)
        InnerquickSort(data, mid+1, r)

def quickSort(data:list):
    InnerquickSort(data, 0, len(data)-1)


if __name__ == '__main__':
    # n = 20
    # data = list(range(1, n + 1))
    # data = shuffle(data)
    data = list(range(1, 21))
    # data = list(range(20, 0, -1))
    # buildHeap(data)
    print(data)
    # data = list(range(1, 21))
    # print(data)
    # data = bubbleSort(data)
    # data = inertSort(data)
    # data = mergeSort(data)

    quickSort(data)
    print(data)
