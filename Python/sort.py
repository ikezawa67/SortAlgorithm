import time
from typing import TypeVar, Callable, Sequence


ELEMENT_COUNT = 10000

_T = TypeVar('_T')


def sort_decorator(func: Callable[[Sequence[_T]], None]) -> Callable[[Sequence[_T]], None]:
    def wrapper(data: Sequence[_T]) -> Sequence[_T]:
        start = time.time()
        func(data)
        end = time.time()
        print(f'{func.__name__}, 処理時間: {end - start}')
        print(', '.join([str(d) for d in data]))
    return wrapper


def _swap(data: Sequence[_T], i: int, j: int) -> None:
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp


@sort_decorator
def bubble_sort(data: Sequence[_T]) -> None:
    for i in range(len(data) - 1):
        for j in range(len(data) - 1, i, -1):
            if data[j] < data[j - 1]:
                _swap(data, j, j - 1)


@sort_decorator
def shaker_sort(data: Sequence[_T]) -> None:
    head = 0
    tail = len(data) - 1
    while True:
        swap_index = head
        for i in range(head, tail):
            if data[i] > data[i + 1]:
                _swap(data, i, i + 1)
                swap_index = i
        tail = swap_index
        if head == tail:
            break
        swap_index = tail
        for i in range(tail, head, -1):
            if data[i] < data[i - 1]:
                _swap(data, i, i - 1)
                swap_index = i
        head = swap_index
        if head == tail:
            break


@sort_decorator
def comb_sort(data: Sequence[_T]) -> None:
    h = int(len(data) * 10 / 13)
    while True:
        swaps = 0
        i = 0
        while i + h < len(data):
            if data[i] > data[i + h]:
                _swap(data, i, i + h)
                swaps += 1
            i += 1
        if h == 1:
            if swaps == 0:
                break
        else:
            h = int(h * 10 / 13)


@sort_decorator
def gnome_sort(data: Sequence[_T]) -> None:
    i = 0
    while i < len(data) - 1:
        if data[i] > data[i + 1]:
            _swap(data, i, i + 1)
            if 0 < i:
                i -= 1
        else:
            i += 1


@sort_decorator
def selection_sort(data: Sequence[_T]) -> None:
    for i in range(len(data)):
        min = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min]:
                min = j
        _swap(data, i, min)


@sort_decorator
def insertion_sort(data: Sequence[_T]) -> None:
    for i in range(1, len(data)):
        if data[i - 1] > data[i]:
            j = i
            tmp = data[i]
            while True:
                data[j] = data[j - 1]
                j -= 1
                if not (0 < j and data[j-1] > tmp):
                    break
            data[j] = tmp


@sort_decorator
def shell_sort(data: Sequence[_T]) -> None:
    h = 1
    while True:
        if h < len(data) / 9:
            break
        h = h * 3 + 1
    while 0 < h:
        for i in range(h, len(data)):
            tmp = data[i]
            if data[i - h] > tmp:
                j = i
                while True:
                    data[j] = data[j - h]
                    j -= h
                    if not (h <= j and data[j - h] > tmp):
                        break
                data[j] = tmp
        h = int(h / 3)


@sort_decorator
def merge_sort(data: Sequence[_T]) -> None:

    def _merge(data0: Sequence[_T], data1: Sequence[_T], left: int, mid: int, right: int) -> None:
        i = left
        j = mid
        k = 0
        while i < mid and j < right:
            if data0[i] < data0[j]:
                data1[k] = data0[i]
                k += 1
                i += 1
            else:
                data1[k] = data0[j]
                k += 1
                j += 1
        if i == mid:
            while j < right:
                data1[k] = data0[j]
                k += 1
                j += 1
        else:
            while i < mid:
                data1[k] = data0[i]
                k += 1
                i += 1
        for l in range(k):
            data0[left + l] = data1[l]

    def _merge_sort(data0: Sequence[_T], data1: Sequence[_T], left: int, right: int) -> None:
        if not (left == right or left == right - 1):
            mid = int((left + right) / 2)
            _merge_sort(data0, data1, left, mid)
            _merge_sort(data0, data1, mid, right)
            _merge(data0, data1, left, mid, right)

    _merge_sort(data, [None] * len(data), 0, len(data))


@sort_decorator
def heap_sort(data: Sequence[_T]) -> None:

    def _upheap(data: Sequence[_T], n: int) -> None:
        while n > 0:
            m = int((n + 1) / 2 - 1)
            if data[m] < data[n]:
                _swap(data, m, n)
            else:
                break
            n = m

    def _downheap(data: Sequence[_T], n: int) -> None:
        m = 0
        tmp = 0
        while True:
            left = (m + 1) * 2 - 1
            right = (m + 1) * 2
            if n <= left:
                break
            if data[left] > data[tmp]:
                tmp = left
            if right < n and data[right] > data[tmp]:
                tmp = right
            if tmp == m:
                break
            _swap(data, tmp, m)
            m = tmp

    i = 1
    while i < len(data):
        _upheap(data, i)
        i += 1
    while i > 0:
        i -= 1
        _swap(data, 0, i)
        _downheap(data, i)
    return data


@sort_decorator
def quick_sort(data: Sequence[_T]) -> None:

    def _partition(data: Sequence[_T], min_index: int, max_index: int) -> int:
        pivot = min_index - 1
        for i in range(min_index, max_index):
            if data[i] < data[max_index]:
                pivot += 1
                _swap(data, pivot, i)
        pivot += 1
        _swap(data, pivot, max_index)
        return pivot

    def _quick_sort(data: Sequence[_T], min_index: int, max_index: int) -> None:
        if not min_index >= max_index:
            pivot_index = _partition(data, min_index, max_index)
            _quick_sort(data, min_index, pivot_index - 1)
            _quick_sort(data, pivot_index + 1, max_index)

    _quick_sort(data, 0, len(data) - 1)


@sort_decorator
def odd_even_sort(data: Sequence[_T]) -> None:
    while True:
        changed = False
        for i in range(0, len(data) - 1, 2):
            if data[i] > data[i + 1]:
                _swap(data, i, i + 1)
                changed = True
        for i in range(1, len(data) - 1, 2):
            if data[i] > data[i + 1]:
                _swap(data, i, i + 1)
                changed = True
        if not changed:
            break
