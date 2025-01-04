def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')  # Or handle it in a more appropriate way

result = my_function(10, 0)
print(result)