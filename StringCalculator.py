def add(numbers: str) -> int:
    delimiter = ','
    if numbers.startswith('//'):
        delimiter, numbers = numbers[2:].split('\n', 1)
    return sum(int(num) for num in numbers.replace('\n', delimiter).split(delimiter) if num.isdigit() and int(num) <= 1000)







    

