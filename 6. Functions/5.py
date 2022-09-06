def odd_nums_remover(numbers):
    evenNumbers = []
    for number in numbers:
        if number % 2 == 0:
            evenNumbers.append(number)
        else:
            continue
    return evenNumbers

nums = [1, 2, 3, 4, 5]

print(odd_nums_remover(nums))