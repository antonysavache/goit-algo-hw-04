import random
import timeit
import matplotlib.pyplot as plt
from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Реалізація сортування вставками
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr: List[int]) -> List[int]:
    """
    Реалізація сортування злиттям
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Допоміжна функція для злиття двох відсортованих масивів
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def timsort(arr: List[int]) -> List[int]:
    """
    Використання вбудованого сортування Python (Timsort)
    """
    return sorted(arr)

def generate_data(size: int, case: str = 'random') -> List[int]:
    """
    Генерація тестових даних різних типів
    """
    if case == 'sorted':
        return list(range(size))
    elif case == 'reversed':
        return list(range(size, 0, -1))
    else:  # random
        return [random.randint(0, 1000000) for _ in range(size)]

def measure_time(func, arr: List[int], number: int = 1) -> float:
    """
    Вимірювання часу виконання функції
    """
    return timeit.timeit(lambda: func(arr.copy()), number=number) / number

def compare_algorithms(sizes: List[int], case: str = 'random') -> dict:
    """
    Порівняння алгоритмів на різних розмірах масивів
    """
    results = {
        'insertion_sort': [],
        'merge_sort': [],
        'timsort': []
    }

    for size in sizes:
        data = generate_data(size, case)

        # Вимірювання часу для кожного алгоритму
        for algo_name, algo_func in [
            ('insertion_sort', insertion_sort),
            ('merge_sort', merge_sort),
            ('timsort', timsort)
        ]:
            time = measure_time(algo_func, data)
            results[algo_name].append(time)

        print(f"Розмір масиву: {size}, Тип даних: {case}")

    return results

def plot_results(sizes: List[int], results: dict, case: str):
    """
    Візуалізація результатів порівняння
    """
    plt.figure(figsize=(10, 6))

    for algo_name, times in results.items():
        plt.plot(sizes, times, marker='o', label=algo_name)

    plt.xlabel('Розмір масиву')
    plt.ylabel('Час виконання (секунди)')
    plt.title(f'Порівняння алгоритмів сортування ({case} case)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'sorting_comparison_{case}.png')
    plt.close()

def main():
    # Тестування на різних розмірах масивів
    sizes = [100, 500, 1000, 5000, 10000]
    cases = ['random', 'sorted', 'reversed']

    for case in cases:
        results = compare_algorithms(sizes, case)
        plot_results(sizes, results, case)

        print(f"\nРезультати для {case} випадку:")
        for algo_name, times in results.items():
            print(f"{algo_name}:")
            for size, time in zip(sizes, times):
                print(f"  Розмір {size}: {time:.6f} сек")

if __name__ == "__main__":
    main()

# Додаткове завдання: об'єднання k відсортованих списків
def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Об'єднання k відсортованих списків в один відсортований список
    """
    if not lists:
        return []

    # Використовуємо функцію merge з сортування злиттям
    def merge_two_lists(l1: List[int], l2: List[int]) -> List[int]:
        return merge(l1, l2)

    # Послідовно об'єднуємо списки
    result = lists[0]
    for i in range(1, len(lists)):
        result = merge_two_lists(result, lists[i])

    return result

# Тестування додаткового завдання
if __name__ == "__main__":
    test_lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged = merge_k_lists(test_lists)
    print("\nДодаткове завдання:")
    print("Вхідні списки:", test_lists)
    print("Відсортований список:", merged)