def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    delimiter = ','
    
    if numbers.startswith('//'):
        parts = numbers.split('\n', 1)
        delimiter = parts[0][2:]
        numbers = parts[1]
    
    numbers = numbers.replace('\n', delimiter)
    num_list = numbers.split(delimiter)
    
    total = 0
    for num in num_list:
        n = int(num)
        if n <= 1000:
            total += n
    
    return total

