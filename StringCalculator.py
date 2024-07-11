def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    delimiter = ','
    
    if numbers.startswith('//'):
        delimiter, numbers = numbers[2:].split('\n', 1)
    
    numbers = numbers.replace('\n', delimiter)
    num_list = numbers.split(delimiter)
    
    return sum(int(num) for num in num_list if int(num) <= 1000)
