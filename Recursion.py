def get_fib(position):
    if position == 0 or position == 1:
        return position
    else:
        sum =  get_fib(position - 1) + get_fib(position - 2)
        # print(sum)
        return sum

# Test cases
print (get_fib(9))
print (get_fib(11))
print (get_fib(0))
