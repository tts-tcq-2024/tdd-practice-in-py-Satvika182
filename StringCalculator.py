def add(numbers: str) -> int:
    delimiter = ','
    numbers_part = numbers
    
    if numbers.startswith('//'):
        delimiter, numbers_part = numbers[2:].split('\n', 1)
        
    all_numbers = numbers_part.replace('\n', delimiter).split(delimiter)
    return sum(int(num) for num in all_numbers if num and int(num) <= 1000)
