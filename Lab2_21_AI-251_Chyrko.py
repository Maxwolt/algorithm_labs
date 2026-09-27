# --- 1.1 Ітеративне сортування злиттям ---
def merge_iterative(a, left, mid, right):
    comparisons = 0
    assignments = 0
    n1 = mid - left
    n2 = right - mid
    L = a[left:mid]
    R = a[mid:right]
    assignments += n1 + n2
    it1 = 0
    it2 = 0
    k = left
    assignments += 3

    while it1 < n1 and it2 < n2:
        comparisons += 1
        if L[it1] <= R[it2]:
            a[k] = L[it1]
            it1 += 1
        else:
            a[k] = R[it2]
            it2 += 1
        assignments += 2
        k += 1
        assignments += 1

    while it1 < n1:
        a[k] = L[it1]
        it1 += 1
        k += 1
        assignments += 3

    while it2 < n2:
        a[k] = R[it2]
        it2 += 1
        k += 1
        assignments += 3

    return comparisons, assignments

def merge_sort_iterative(a_orig):
    a = a_orig.copy()
    n = len(a)
    comparisons = 0
    assignments = 0
    i = 1
    print("--- Трасування Ітеративного Сортування Злиттям ---")
    print(f"Початковий масив: {a}")

    while i < n:
        j = 0
        while j < n - i:
            left = j
            mid = j + i
            right = min(j + 2 * i, n)
            print(f"Об'єднуємо підмасиви: a[{left}:{mid}] ({a[left:mid]}) і a[{mid}:{right}] ({a[mid:right]})")
            c, ass = merge_iterative(a, left, mid, right)
            comparisons += c
            assignments += ass
            print(f"Масив після об'єднання: {a}")
            j += 2 * i
        i *= 2
    return a, comparisons, assignments

# --- 1.2 Рекурсивне сортування злиттям ---
def merge_recursive(left, right):
    merged_arr = []
    comparisons = 0
    assignments = 0
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
        assignments += 2

    while i < len(left):
        merged_arr.append(left[i])
        i += 1
        assignments += 2

    while j < len(right):
        merged_arr.append(right[j])
        j += 1
        assignments += 2

    return merged_arr, comparisons, assignments

def merge_sort_recursive(arr):
    comparisons = 0
    assignments = 0
    recursive_calls = 1

    if len(arr) <= 1:
        return arr, comparisons, assignments, recursive_calls

    mid = len(arr) // 2
    assignments += 1

    print(f"Розділяємо масив: {arr} -> лівий: {arr[:mid]}, правий: {arr[mid:]}")

    left_half, c1, a1, r1 = merge_sort_recursive(arr[:mid])
    right_half, c2, a2, r2 = merge_sort_recursive(arr[mid:])

    merged_arr, c_merge, a_merge = merge_recursive(left_half, right_half)
    print(f"Зливаємо {left_half} та {right_half} -> Результат: {merged_arr}")

    comparisons += c1 + c2 + c_merge
    assignments += a1 + a2 + a_merge
    recursive_calls += r1 + r2

    return merged_arr, comparisons, assignments, recursive_calls

# --- 2. ШВИДКЕ СОРТУВАННЯ ЗА СХЕМОЮ ХОАРА ---

def partition(a, l, r):
    comparisons = 0
    assignments = 0
    pivot = a[l]
    assignments += 1
    i, j = l - 1, r + 1
    assignments += 2

    print(f"\n> Розділення a[{l}:{r+1}] {a[l:r+1]} | Pivot = {pivot}")

    while True:
        i += 1
        assignments += 1
        while a[i] < pivot:
            comparisons += 1
            i += 1
            assignments += 1
        comparisons += 1

        j -= 1
        assignments += 1
        while a[j] > pivot:
            comparisons += 1
            j -= 1
            assignments += 1
        comparisons += 1

        comparisons += 1
        if i >= j:
            print(f"  Поділ завершено: точка j = {j}")
            return j, comparisons, assignments

        a[i], a[j] = a[j], a[i]
        assignments += 3
        print(f"  Обмін a[{i}] ↔ a[{j}]: {a[l:r+1]}")

def quicksort(a, l, r):
    comparisons = 0
    assignments = 0
    recursive_calls = 1

    if l < r:
        q, c1, a1 = partition(a, l, r)
        comparisons += c1
        assignments += a1

        c2, a2, r2 = quicksort(a, l, q)
        c3, a3, r3 = quicksort(a, q + 1, r)

        comparisons += c2 + c3
        assignments += a2 + a3
        recursive_calls += r2 + r3

    return comparisons, assignments, recursive_calls

# --- БЛОК ТЕСТУВАННЯ ТА ВИВЕДЕННЯ РЕЗУЛЬТАТІВ ---
if __name__ == "__main__":

    my_array = [50, 57, 78, 34, 41, 68, 47, 61, 38]

    print("==========================================")
    print("1. ТЕСТУВАННЯ ІТЕРАТИВНОГО MERGE SORT")
    print("==========================================")
    sorted_arr, comps, assigs = merge_sort_iterative(my_array)
    print(f"\nФінальний відсортований масив: {sorted_arr}")
    print(f"Кількість порівнянь: {comps}")
    print(f"Кількість присвоювань: {assigs}")

    print("\n==========================================")
    print("2. ТЕСТУВАННЯ РЕКУРСИВНОГО MERGE SORT")
    print("==========================================")
    sorted_arr_rec, comps_rec, assigs_rec, calls_rec = merge_sort_recursive(my_array)
    print(f"\nФінальний відсортований масив: {sorted_arr_rec}")
    print(f"Загальна кількість порівнянь: {comps_rec}")
    print(f"Загальна кількість присвоювань: {assigs_rec}")
    print(f"Загальна кількість рекурсивних викликів: {calls_rec}")

    print("\n==========================================")
    print("3. ТЕСТУВАННЯ QUICK SORT (СХЕМА ХОАРА)")
    print("==========================================")
    quick_array = my_array.copy()
    comps_q, assigs_q, calls_q = quicksort(quick_array, 0, len(quick_array) - 1)
    print(f"\nФінальний відсортований масив: {quick_array}")
    print(f"Загальна кількість порівнянь: {comps_q}")
    print(f"Загальна кількість присвоювань: {assigs_q}")
    print(f"Загальна кількість рекурсивних викликів: {calls_q}")