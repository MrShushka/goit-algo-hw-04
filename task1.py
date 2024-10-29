import random
import timeit
import matplotlib.pyplot as plt

# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key 

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged



def generate_data(size):
    return [random.randint(1, size) for _ in range(size)]

def test_sorting_algorithms(sizes):
    insertion_times = []
    merge_times = []
    timsort_times = []

    for size in sizes:
        data = generate_data(size)

        insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=10)
        insertion_times.append(insertion_time)

        merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=10)
        merge_times.append(merge_time)

        timsort_time = timeit.timeit(lambda: sorted(data), number=10)  # sorted() використовує Timsort
        timsort_times.append(timsort_time)

    return insertion_times, merge_times, timsort_times

sizes = [100, 200, 400, 800, 1600, 3200, 6400]

insertion_times, merge_times, timsort_times = test_sorting_algorithms(sizes)

plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
plt.plot(sizes, merge_times, label='Merge Sort', marker='o')
plt.plot(sizes, timsort_times, label='Timsort (sorted)', marker='o')
plt.xlabel('Розмір масиву')
plt.ylabel('Час виконання (секунди)')
plt.title('Порівняння алгоритмів сортування')
plt.legend()
plt.grid()
plt.show()
