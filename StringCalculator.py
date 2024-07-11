def add(numbers: str) -> int:
    if numbers == "":
        return 0
    
    delimiter = ','
    if numbers.startswith('//'):
        delimiter, numbers = numbers[2:].split('\n', 1)
    
    # Replace newline characters with delimiter and split by delimiter
    numbers = numbers.replace('\n', delimiter)
    num_list = numbers.split(delimiter)
    
    total_sum = 0
    for num in num_list:
        num_int = int(num)
        if num_int <= 1000:
            total_sum += num_int
        
    return total_sum


    

