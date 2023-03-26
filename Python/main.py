import copy
import random
import sort

data = [random.randint(0, 500) for _ in range(25)]
sort.bubble_sort(copy.deepcopy(data))
sort.shaker_sort(copy.deepcopy(data))
sort.comb_sort(copy.deepcopy(data))
sort.gnome_sort(copy.deepcopy(data))
sort.selection_sort(copy.deepcopy(data))
sort.insertion_sort(copy.deepcopy(data))
sort.shell_sort(copy.deepcopy(data))
sort.merge_sort(copy.deepcopy(data))
sort.heap_sort(copy.deepcopy(data))
sort.quick_sort(copy.deepcopy(data))
sort.odd_even_sort(copy.deepcopy(data))
