def add(numbers: str) -> int:
    if numbers == "":
        return 0
    
    # Split numbers by comma and convert them to integers
    num_list = numbers.split(',')
    total_sum = 0
    for num in num_list:
        total_sum += int(num)
        
    return total_sum
    

