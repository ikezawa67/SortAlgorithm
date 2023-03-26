class Sort
{
    private static (T, T) Swap<T>(T element0, T element1)
    {
        return (element1, element0);
    }

    public static void BubbleSort<T>(IList<T> data) where T : IComparable<T>
    {
        for (int i = 0; i < data.Count; i++)
        {
            for (int j = 0; j < data.Count; j++)
            {
                if (data[i].CompareTo(data[j]) < 0)
                {
                    (data[i], data[j]) = Swap(data[i], data[j]);
                }
            }
        }
    }

    public static void ShakerSort<T>(IList<T> data) where T : IComparable<T>
    {
        int head = 0;
        int tail = data.Count - 1;
        while (true)
        {
            int swapIndex = head;
            for (int i = head; i < tail; i++)
            {
                if (0 < data[i].CompareTo(data[i + 1]))
                {
                    (data[i], data[i + 1]) = Swap(data[i], data[i + 1]);
                    swapIndex = i;
                }
            }
            tail = swapIndex;
            if (head == tail)
            {
                break;
            }
            swapIndex = tail;
            for (int i = tail; head < i; i--)
            {
                if (data[i].CompareTo(data[i - 1]) < 0)
                {
                    (data[i], data[i - 1]) = Swap(data[i], data[i - 1]);
                    swapIndex = i;
                }
            }
            head = swapIndex;
            if (head == tail)
            {
                break;
            }
        }
    }

    public static void CombSort<T>(IList<T> data) where T : IComparable<T>
    {
        int h = data.Count * 10 / 13;
        while (true)
        {
            int swaps = 0;
            for (int i = 0; i + h < data.Count; i++)
            {
                if (0 < data[i].CompareTo(data[i + h]))
                {
                    (data[i], data[i + h]) = Swap(data[i], data[i + h]);
                    swaps++;
                }
            }
            if (h == 1)
            {
                if (swaps == 0)
                {
                    break;
                }
            }
            else
            {
                h = h * 10 / 13;
            }
        }
    }

    public static void GnomeSort<T>(IList<T> data) where T : IComparable<T>
    {
        int i = 0;
        while (i < data.Count - 1)
        {
            if (0 < data[i].CompareTo(data[i + 1]))
            {
                (data[i], data[i + 1]) = Swap(data[i], data[i + 1]);
                if (0 < i)
                {
                    i--;
                }
            }
            else
            {
                i++;
            }
        }
    }

    public static void SelectionSort<T>(IList<T> data) where T : IComparable<T>
    {
        for (int i = 0; i < data.Count; i++)
        {
            int min = i;
            for (int j = i + 1; j < data.Count; j++)
            {
                if (data[j].CompareTo(data[min]) < 0)
                {
                    min = j;
                }
            }
            (data[i], data[min]) = Swap(data[i], data[min]);
        }
    }

    public static void InsertionSort<T>(IList<T> data) where T : IComparable<T>
    {
        for (int i = 1; i < data.Count; i++)
        {
            if (0 < data[i - 1].CompareTo(data[i]))
            {
                int j = i;
                T tmp = data[i];
                do
                {
                    data[j] = data[j - 1];
                    j--;
                } while (0 < j && 0 < data[j - 1].CompareTo(tmp));
                data[j] = tmp;
            }
        }
    }

    public static void ShellSort<T>(IList<T> data) where T : IComparable<T>
    {
        int h = 1;
        for (int hTmp = 1; hTmp < data.Count / 9; hTmp = hTmp * 3 + 1)
        {
            h = hTmp;
        }
        while (0 < h)
        {
            for (int i = h; i < data.Count; i++)
            {
                T tmp = data[i];
                if (0 < data[i - h].CompareTo(tmp))
                {
                    int j = i;
                    do
                    {
                        data[j] = data[j - h];
                        j -= h;
                    } while (h <= j && 0 < data[j - h].CompareTo(tmp));
                    data[j] = tmp;
                }
            }
            h /= 3;
        }
    }
    private static void Merge<T>(IList<T> data0, IList<T> data1, int left, int mid, int right) where T : IComparable<T>
    {
        int i = left;
        int j = mid;
        int k = 0;
        while (i < mid && j < right)
        {
            if (data0[i].CompareTo(data0[j]) < 0)
            {
                data1[k++] = data0[i++];
            }
            else
            {
                data1[k++] = data0[j++];
            }
        }
        if (i == mid)
        {
            while (j < right)
            {
                data1[k++] = data0[j++];
            }
        }
        else
        {
            while (i < mid)
            {
                data1[k++] = data0[i++];
            }
        }
        for (int l = 0; l < k; l++)
        {
            data0[left + l] = data1[l];
        }
    }

    private static void MergeSort<T>(IList<T> data0, IList<T> data1, int left, int right) where T : IComparable<T>
    {
        int mid;
        if (!(left == right || left == right - 1))
        {
            mid = (left + right) / 2;
            MergeSort(data0, data1, left, mid);
            MergeSort(data0, data1, mid, right);
            Merge(data0, data1, left, mid, right);
        }
    }

    public static void MergeSort<T>(IList<T> data) where T : IComparable<T>
    {
        MergeSort(data, new T[data.Count], 0, data.Count);
    }

    private static void Upheapt<T>(IList<T> data, int n) where T : IComparable<T>
    {
        while (n > 0)
        {
            int m = (n + 1) / 2 - 1;
            if (data[m].CompareTo(data[n]) < 0)
            {
                (data[m], data[n]) = Swap(data[m], data[n]);
            }
            else
            {
                break;
            }
            n = m;
        }
    }

    private static void Downheap<T>(IList<T> data, int n) where T : IComparable<T>
    {
        int m = 0;
        int tmp = 0;
        while (true)
        {
            int left = (m + 1) * 2 - 1;
            int right = (m + 1) * 2;
            if (n <= left)
            {
                break;
            }
            if (0 < data[left].CompareTo(data[tmp]))
            {
                tmp = left;
            }
            if (right < n && 0 < data[right].CompareTo(data[tmp]))
            {
                tmp = right;
            }
            if (tmp == m)
            {
                break;
            }
            (data[tmp], data[m]) = Swap(data[tmp], data[m]);
            m = tmp;
        }
    }

    public static void HeapSort<T>(IList<T> data) where T : IComparable<T>
    {
        int i = 0;
        while (++i < data.Count)
        {
            Upheapt(data, i);
        }
        while (0 < --i)
        {
            (data[0], data[i]) = Swap(data[0], data[i]);
            Downheap(data, i);
        }
    }

    private static int Partition<T>(IList<T> data, int minIndex, int maxIndex) where T : IComparable<T>
    {
        var pivot = minIndex - 1;
        for (var i = minIndex; i < maxIndex; i++)
        {
            if (data[i].CompareTo(data[maxIndex]) < 0)
            {
                pivot++;
                (data[pivot], data[i]) = Swap(data[pivot], data[i]);
            }
        }
        pivot++;
        (data[pivot], data[maxIndex]) = Swap(data[pivot], data[maxIndex]);
        return pivot;
    }

    private static void QuickSort<T>(IList<T> data, int minIndex, int maxIndex) where T : IComparable<T>
    {
        if (!(minIndex >= maxIndex))
        {
            var pivotIndex = Partition(data, minIndex, maxIndex);
            QuickSort(data, minIndex, pivotIndex - 1);
            QuickSort(data, pivotIndex + 1, maxIndex);
        }
    }

    public static void QuickSort<T>(IList<T> data) where T : IComparable<T>
    {
        QuickSort(data, 0, data.Count - 1);
    }

    public static void OddEvenSort<T>(IList<T> data) where T : IComparable<T>
    {
        bool changed;
        do
        {
            changed = false;
            for (int i = 0; i < data.Count - 1; i += 2)
            {
                if (0 < data[i].CompareTo(data[i + 1]))
                {
                    (data[i], data[i + 1]) = Swap(data[i], data[i + 1]);
                    changed = true;
                }
            }
            for (int i = 1; i < data.Count - 1; i += 2)
            {
                if (0 < data[i].CompareTo(data[i + 1]))
                {
                    (data[i], data[i + 1]) = Swap(data[i], data[i + 1]);
                    changed = true;
                }
            }
        } while (changed);
    }

}