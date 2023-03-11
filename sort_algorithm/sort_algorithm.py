import copy
import math
import time
import random
from typing import TypeVar, Callable


ELEMENT_COUNT = 10000

_T = TypeVar('_T')


def sort_decorator(func: Callable[[list[_T]], list[_T]]) -> Callable[[list[_T]], list[_T]]:
    def wrapper(data: list[_T]) -> list[_T]:
        if __name__ == "__main__":
            start = time.time()
            result = func(copy.deepcopy(data))
            end = time.time()
            print(f'{func.__name__}, 処理時間: {end - start}')
        else:
            result = func(copy.deepcopy(data))
        return result
    return wrapper


def _swap(data: list[_T], i: int, j: int) -> None:
    temp = data[i]
    data[i] = data[j]
    data[j] = temp


def _median3(x: _T, y: _T, z: _T) -> _T:
    return max(min(x, y), min(max(x, y), z))


def _partition(data: list[_T], first: int, last: int) -> int:
    pivot = _median3(data[first], data[first + (last - first) // 2], data[last])
    while True:
        while data[first] < pivot:
            first += 1
        while pivot < data[last]:
            last -= 1
        if first >= last:
            return last + 1
        _swap(data, first, last)
        first += 1
        last -= 1


@sort_decorator
def bubble_sort(data: list[_T]) -> list[_T]:
    """バブルソート

    Args:
        data (list[_T]): ソートするイテラブルオブジェクト

    Returns:
        list[_T]: ソートした新たなイテラブルオブジェクト
    """

    for i in range(len(data) - 1):
        for j in range(len(data) - 1, i, -1):
            if data[j] < data[j - 1]:
                _swap(data, j, j - 1)
    return data


@sort_decorator
def shaker_sort(data: list[_T]) -> list[_T]:
    """シェーカーソート

    Args:
        data (list[_T]): ソートするイテラブルオブジェクト

    Returns:
        list[_T]: ソートした新たなイテラブルオブジェクト
    """

    low = 0
    high = len(data) - 1
    while True:
        last = low
        for i in range(low, high):
            if data[i] > data[i + 1]:
                _swap(data, i, i + 1)
                last = i
        high = last
        if low == high:
            break
        last = high
        for i in range(high, low, -1):
            if data[i] < data[i - 1]:
                _swap(data, i, i - 1)
                last = i
        low = last
        if low == high:
            break
    return data


@sort_decorator
def comb_sort(data: list[_T]) -> list[_T]:
    """コムソート

    Args:
        data (list[_T]): ソートするイテラブルオブジェクト

    Returns:
        list[_T]: ソートした新たなイテラブルオブジェクト
    """

    h = len(data)
    is_swapped = False
    while h > 1 or is_swapped:
        if h > 1:
            h = int((h * 10) / 13)
        is_swapped = False
        for i in range(len(data) - h):
            if data[i] > data[i + h]:
                _swap(data, i, i + h)
                is_swapped = True
    return data


@sort_decorator
def gnome_sort(data: list[_T]) -> list[_T]:
    """ノームソート

    Args:
        data (list[_T]): ソートするイテラブルオブジェクト

    Returns:
        list[_T]: ソートした新たなイテラブルオブジェクト
    """

    i = 1
    while i < len(data):
        if data[i - 1] <= data[i]:
            i += 1
        else:
            _swap(data, i - 1, i)
            i -= 1
            if i == 0:
                i += 1
    return data


@sort_decorator
def selection_sort(data: list[_T]) -> list[_T]:
    """選択ソート

    Args:
        data (list[_T]): ソートするイテラブルオブジェクト

    Returns:
        list[_T]: ソートした新たなイテラブルオブジェクト
    """

    for i in range(len(data)):
        min = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min]:
                min = j
        _swap(data, i, min)
    return data


@sort_decorator
def insertion_sort(data: list[_T]) -> list[_T]:
    """挿入ソート

    Args:
        data (list[_T]): ソートするイテラブルオブジェクト

    Returns:
        list[_T]: ソートした新たなイテラブルオブジェクト
    """

    for i in range(1, len(data)):
        tmp = data[i]
        j = i - 1
        while j >= 0 and data[j] > tmp:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = tmp
    return data


@sort_decorator
def shell_sort(data: list[_T]) -> list[_T]:
    """シェルソート

    Args:
        data (list[_T]): ソートするイテラブルオブジェクト

    Returns:
        list[_T]: ソートした新たなイテラブルオブジェクト
    """

    h = len(data) // 2
    while h > 0:
        for i in range(h, len(data)):
            tmp = data[i]
            j = i
            while j >= h and data[j - h] > tmp:
                data[j] = data[j - h]
                j -= h
            data[j] = tmp
        h //= 2
    return data


@sort_decorator
def merge_sort(data: list[_T]) -> list[_T]:
    """マージソート

    Args:
        data (list[_T]): ソートするイテラブルオブジェクト

    Returns:
        list[_T]: ソートした新たなイテラブルオブジェクト
    """

    def _merge_sort(data: list[_T]) -> list[_T]:

        def _merge(left: list[_T], right: list[_T]) -> list[_T]:
            result = []
            i, j = 0, 0
            while (i < len(left)) and (j < len(right)):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            if i < len(left):
                result.extend(left[i:])
            if j < len(right):
                result.extend(right[j:])
            return result

        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = _merge_sort(data[:mid])
        right = _merge_sort(data[mid:])
        return _merge(left, right)

    return _merge_sort(data)


@sort_decorator
def heap_sort(data: list[_T]) -> list[_T]:
    """ヒープソート

    Args:
        data (list[_T]): ソートするイテラブルオブジェクト

    Returns:
        list[_T]: ソートした新たなイテラブルオブジェクト
    """

    def _upheap(data: list[_T], n: int) -> None:
        while n > 0:
            m = int((n + 1) / 2 - 1)
            if data[m] < data[n]:
                _swap(data, m, n)
            else:
                break
            n = m

    def _downheap(data: list[_T], n: int) -> None:
        m = 0
        tmp = 0
        while True:
            left = (m + 1) * 2 - 1
            right = (m + 1) * 2
            if left >= n:
                break
            if data[left] > data[tmp]:
                tmp = left
            if right < n and data[right] > data[tmp]:
                tmp = right
            if tmp == m:
                break
            _swap(data, tmp, m)
            m = tmp

    i = 0
    while i < len(data):
        _upheap(data, i)
        i += 1
    while i > 0:
        i -= 1
        _swap(data, 0, i)
        _downheap(data, i)
    return data


@sort_decorator
def quick_sort(data: list[_T]) -> list[_T]:
    """クイックソート

    Args:
        data (list[_T]): ソートするイテラブルオブジェクト

    Returns:
        list[_T]: ソートした新たなイテラブルオブジェクト
    """

    def _quick_sort(data: list[_T], first: int, last: int) -> list[_T]:
        while first < last:
            p = _partition(data, first, last)
            if (p - first) < (last - p):
                _quick_sort(data, first, p - 1)
                first = p
            else:
                _quick_sort(data, p, last)
                last = p - 1
        return data

    return _quick_sort(data, 0, len(data) - 1)


@sort_decorator
def intro_sort(data: list[_T]) -> list[_T]:
    """イントロソート

    Args:
        data (list[_T]): ソートするイテラブルオブジェクト

    Returns:
        list[_T]: ソートした新たなイテラブルオブジェクト
    """

    def _introsort(data: list[_T], first: int, last: int, max_depth: int):
        if last <= first:
            return
        elif max_depth == 0:
            heap_sort(data[first:last])
        else:
            pivot_index = _partition(data, first, last)
            _introsort(data, first, pivot_index - 1, max_depth - 1)
            _introsort(data, pivot_index + 1, last, max_depth - 1)
        return data

    n = len(data)
    max_depth = math.floor(2 * math.log2(n))
    _introsort(data, 0, n - 1, max_depth)


@sort_decorator
def odd_even_sort(data: list[_T]) -> list[_T]:
    """奇偶転置ソート

    Args:
        data (list[_T]): ソートするイテラブルオブジェクト

    Returns:
        list[_T]: ソートした新たなイテラブルオブジェクト
    """

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
    return data


@sort_decorator
def python_sort(data: list[_T]) -> list[_T]:
    """Pythonに組み込まれたソートメソッド

    Args:
        data (list[_T]): ソートするイテラブルオブジェクト

    Returns:
        list[_T]: ソートした新たなイテラブルオブジェクト
    """

    data.sort()
    return data

if __name__ == '__main__':
    data = random.sample(range(ELEMENT_COUNT), ELEMENT_COUNT)
    bubble_sort(data)
    shaker_sort(data)
    comb_sort(data)
    gnome_sort(data)
    selection_sort(data)
    insertion_sort(data)
    shell_sort(data)
    merge_sort(data)
    heap_sort(data)
    quick_sort(data)
    intro_sort(data)
    odd_even_sort(data)
    python_sort(data)
