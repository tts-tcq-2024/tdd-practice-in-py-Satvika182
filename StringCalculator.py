def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    delimiter = ','
    if numbers.startswith('//'):
        delimiter, numbers = re.split('\n', numbers[2:], 1)
    
    num_list = re.split(f'[{re.escape(delimiter)}\n]', numbers)
    return sum(int(num) for num in num_list if int(num) <= 1000)
