def add(numbers: str) -> int:
    if numbers.startswith('//'):
        delimiter, numbers = numbers[2:].split('\n', 1)
    else:
        delimiter = ','
    
    num_list = numbers.replace('\n', delimiter).split(delimiter)
    return sum(int(num) for num in num_list if num.isdigit() and int(num) <= 1000)







    

