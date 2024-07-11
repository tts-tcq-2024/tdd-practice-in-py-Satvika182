def add(numbers: str) -> int:
    return sum(
        map(
            int,
            filter(
                lambda x: x.isdigit() and int(x) <= 1000,
                numbers[2:].split('\n', 1)[-1].replace('\n', numbers[2:].split('\n', 1)[0]).split(numbers[2:].split('\n', 1)[0])
            )
        )
    ) if numbers.startswith('//') else sum(map(int, filter(lambda x: x.isdigit() and int(x) <= 1000, numbers.replace('\n', ",").split(","))))








    

