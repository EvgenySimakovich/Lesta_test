# Алгоритм быстрой сортировки - среднее время сортировки составляет O(n*log(n)) в среднем и лучшем случае
# при выбора опорного элемента.

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i < pivot]
        return quicksort(less) + [pivot] + quicksort(greater)