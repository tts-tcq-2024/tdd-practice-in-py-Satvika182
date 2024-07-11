def add(numbers: str) -> int:
    delimiter = ','
    if numbers.startswith('//'):
        delimiter, numbers = numbers[2:].split('\n', 1)
    elif not numbers:
        return 0
    
    num_list = numbers.replace('\n', delimiter).split(delimiter)
    return sum(int(num) for num in num_list if num.isdigit() and int(num) <= 1000)




    

