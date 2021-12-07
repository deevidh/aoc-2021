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

def next_day(fish_freq):
    # Count fish mommas/babies & decrease all ages
    fish_babies = fish_freq.pop(0)
    # Reset fish mommas to 6 days
    fish_freq[6]+=fish_babies
    # Add new babies (8 days)
    fish_freq.append(fish_babies)
    return fish_freq

def part1(fishies, days):
    fish_freq = []
    for i in range(0,9):
        fish_freq.append(fishies.count(i))
    for i in range(1,days+1):
        fish_freq = next_day(fish_freq)
    return sum(fish_freq)

input_data = get_input()

## Part 1
my_answer=part1(input_data, 80)
print(f"Part 1: {my_answer}")
#submit(my_answer)

## Part 2
my_answer=part1(input_data, 256)
print(f"Part 2: {my_answer}")
#submit(my_answer)
