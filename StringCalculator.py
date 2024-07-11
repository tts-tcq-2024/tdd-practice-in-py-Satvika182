def add(numbers: str) -> int:
    if numbers == "":
        return 0
    
    # Split numbers by comma and convert them to integers, ignoring numbers greater than 1000
    num_list = numbers.split(',')
    total_sum = 0
    for num in num_list:
        num_int = int(num)
        if num_int <= 1000:
            total_sum += num_int
        
    return total_sum

    

