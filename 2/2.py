from aocd import data
from aocd import submit
from aocd import get

# If set to True, use test data from the test_data.txt file
USE_TEST_DATA=False

def get_input():
    if USE_TEST_DATA:
        with open(f"{get.get_day_and_year()[0]}/test_data.txt") as f:
            data_lines = f.read().splitlines()
    else:
        data_lines = data.splitlines()
    strings = [ line.split(" ") for line in data_lines ]
    return [(direction, int(distance)) for [direction, distance] in strings]

def part1(course):
    distance = 0
    depth = 0
    for direction, amount in course:
        if direction == "forward":
            distance+=amount
        if direction == "up":
            depth-=amount
        if direction == "down":
            depth+=amount
    return distance * depth

def part2(course):
    aim = 0
    distance = 0
    depth = 0
    for direction, amount in course:
        if direction == "forward":
            distance+=amount
            depth+=amount*aim
        if direction == "up":
            aim-=amount
        if direction == "down":
            aim+=amount
    return distance * depth

input_data = get_input()

## Part 1
my_answer=part1(input_data)
print(f"Part 1: {my_answer}")
#submit(my_answer)

## Part 2
my_answer=part2(input_data)
print(f"Part 2: {my_answer}")
#submit(my_answer)
