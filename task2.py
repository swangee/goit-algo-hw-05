def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    ops = 0
    res = None

    while low <= high:
        ops += 1

        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            res = arr[mid]
            break

    if res is None:
        if len(arr) > mid:
            res = arr[mid]
        else:
            res = arr[mid+1]

    # якщо елемент не знайдений
    return ops, res

arr = [2.6, 3.2, 4.56, 10.1, 40.5]
x = 10
result = binary_search(arr, x)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
