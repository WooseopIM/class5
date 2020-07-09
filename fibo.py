def fibonacci(num):
    global count_one, count_zero
    if num < 2:
        if num == 0:
            count_zero += 1
            return 0
        else:
            count_one += 1
            return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)


for i in range(10):
    count_zero = 0
    count_one = 0
    print(f"피보나치 {i}항의 수는 {fibonacci(i)}")
    print(f"fibonacci(0) 호출회수 : {count_zero}, fibonacci(1) 호출회수 : {count_one}")