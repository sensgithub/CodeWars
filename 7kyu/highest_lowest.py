# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.
def high_and_low(numbers):
    numbers = numbers.split()
    numbers = [int(i) for i in numbers]
    return str(max(numbers))+" "+str(min(numbers))