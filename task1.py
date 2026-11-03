
def sort_by_parity(lst):
    even_numbers = [x for x in lst if x % 2 == 0]
    odd_numbers = [x for x in lst if x % 2 != 0]
    even_number=bucket_sort(even_numbers, max(even_numbers) if even_numbers else 0)
    odd_number=bucket_sort(odd_numbers, max(odd_numbers) if odd_numbers else 0)
    return even_number + odd_number

def bucket_sort(lst, max):
    buckets = [0] * (max + 1)
    for item in lst:
        buckets[item] += 1

    lst[:] = []
    for num, count in enumerate(buckets):
        lst.extend(count * [num])
    return lst 

print(sort_by_parity([5, 2, 9, 4, 1]))