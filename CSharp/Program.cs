class Program
{
    static Random random = new Random(new Random().Next());
    static System.Diagnostics.Stopwatch stopwatch = new System.Diagnostics.Stopwatch();

    static void Main()
    {
        byte[] data = new byte[25];
        random.NextBytes(data);

        stopwatch.Start();
        byte[] tmp = (byte[])data.Clone();
        Sort.BubbleSort(tmp);
        stopwatch.Stop();
        Console.WriteLine($"バブルソート 処理時間: {stopwatch.ElapsedMilliseconds}(ms)");
        Console.WriteLine(String.Join(", ", tmp));
        stopwatch.Reset();

        stopwatch.Start();
        tmp = (byte[])data.Clone();
        Sort.ShakerSort(tmp);
        stopwatch.Stop();
        Console.WriteLine($"シェーカーソート 処理時間: {stopwatch.ElapsedMilliseconds}(ms)");
        Console.WriteLine(String.Join(", ", tmp));
        stopwatch.Reset();

        stopwatch.Start();
        tmp = (byte[])data.Clone();
        Sort.CombSort(tmp);
        stopwatch.Stop();
        Console.WriteLine($"コムソート 処理時間: {stopwatch.ElapsedMilliseconds}(ms)");
        Console.WriteLine(String.Join(", ", tmp));
        stopwatch.Reset();

        stopwatch.Start();
        tmp = (byte[])data.Clone();
        Sort.GnomeSort(tmp);
        stopwatch.Stop();
        Console.WriteLine($"ノームソート 処理時間: {stopwatch.ElapsedMilliseconds}(ms)");
        Console.WriteLine(String.Join(", ", tmp));
        stopwatch.Reset();

        stopwatch.Start();
        tmp = (byte[])data.Clone();
        Sort.SelectionSort(tmp);
        stopwatch.Stop();
        Console.WriteLine($"選択ソート 処理時間: {stopwatch.ElapsedMilliseconds}(ms)");
        Console.WriteLine(String.Join(", ", tmp));
        stopwatch.Reset();

        stopwatch.Start();
        tmp = (byte[])data.Clone();
        Sort.InsertionSort(tmp);
        stopwatch.Stop();
        Console.WriteLine($"挿入ソート 処理時間: {stopwatch.ElapsedMilliseconds}(ms)");
        Console.WriteLine(String.Join(", ", tmp));
        stopwatch.Reset();

        stopwatch.Start();
        tmp = (byte[])data.Clone();
        Sort.ShellSort(tmp);
        stopwatch.Stop();
        Console.WriteLine($"シェルソート 処理時間: {stopwatch.ElapsedMilliseconds}(ms)");
        Console.WriteLine(String.Join(", ", tmp));
        stopwatch.Reset();

        stopwatch.Start();
        tmp = (byte[])data.Clone();
        Sort.MergeSort(tmp);
        stopwatch.Stop();
        Console.WriteLine($"マージソート 処理時間: {stopwatch.ElapsedMilliseconds}(ms)");
        Console.WriteLine(String.Join(", ", tmp));
        stopwatch.Reset();

        stopwatch.Start();
        tmp = (byte[])data.Clone();
        Sort.HeapSort(tmp);
        stopwatch.Stop();
        Console.WriteLine($"ヒープソート 処理時間: {stopwatch.ElapsedMilliseconds}(ms)");
        Console.WriteLine(String.Join(", ", tmp));
        stopwatch.Reset();

        stopwatch.Start();
        tmp = (byte[])data.Clone();
        Sort.QuickSort(tmp);
        stopwatch.Stop();
        Console.WriteLine($"クイックソート 処理時間: {stopwatch.ElapsedMilliseconds}(ms)");
        Console.WriteLine(String.Join(", ", tmp));
        stopwatch.Reset();

        stopwatch.Start();
        tmp = (byte[])data.Clone();
        Sort.OddEvenSort(tmp);
        stopwatch.Stop();
        Console.WriteLine($"奇偶転置ソート 処理時間: {stopwatch.ElapsedMilliseconds}(ms)");
        Console.WriteLine(String.Join(", ", tmp));
        stopwatch.Reset();
    }
}