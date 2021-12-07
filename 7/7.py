from aocd import submit
from aocd import get
from aocd import data

# If set to True, use test data from the test_data.txt file
USE_TEST_DATA=False

def get_input():
    if USE_TEST_DATA:
        with open(f"{get.get_day_and_year()[0]}/test_data.txt") as f:
            puzzle_data = f.read()
    else:
        puzzle_data = data
    return [ int(item) for item in puzzle_data.split(",") ]

def part1(crab_positions):
    total_fuels = []
    for x in range(min(crab_positions),max(crab_positions)):
        crab_fuels = [ abs(position-x) for position in crab_positions ]
        total_fuels.append(sum(crab_fuels))
    return min(total_fuels)

def part2(crab_positions):
    total_fuels = []
    for x in range(min(crab_positions),max(crab_positions)):
        crab_distances = [ abs(position-x) for position in crab_positions ]
        crab_fuels = [ int(((crab_distance*crab_distance)+crab_distance)/2) for crab_distance in crab_distances ]
        total_fuels.append(sum(crab_fuels))
    return min(total_fuels)

input_data = get_input()

## Part 1
my_answer=part1(input_data)
print(f"Part 1: {my_answer}")
#submit(my_answer)

## Part 2
my_answer=part2(input_data)
print(f"Part 2: {my_answer}")
#submit(my_answer)
