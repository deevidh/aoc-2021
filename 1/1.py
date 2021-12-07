from aocd import data
from aocd import submit
from aocd import get

# If set to True, use test data from the test_data.txt file"
USE_TEST_DATA=False

def get_input():
    if USE_TEST_DATA:
        with open(f"{get.get_day_and_year()[0]}/test_data.txt") as f:
            data_lines = f.read().splitlines()
    else:
        data_lines = data.splitlines()
    return [ int(line) for line in data_lines ]

def calculate_depths(depths):
    increases = 0
    for i in range(len(depths)-1):
        if depths[i] < depths[i+1]:
            increases+=1
    return increases

def calculate_depths_window(depths, n):
    increases = 0
    for i in range(len(depths)-(n-1)):
        if sum(depths[i:i+n]) < sum(depths[i+1:i+n+1]):
            increases+=1
    return increases

depths = get_input()

## Part 1
my_answer=calculate_depths(depths)
print(f"Part 1: {my_answer}")
#submit(my_answer)

## Part 2
my_answer=calculate_depths_window(depths, 3)
print(f"Part 2: {my_answer}")
#submit(my_answer)
