from aocd import submit
from aocd import get
from aocd import data
from math import prod
import itertools

# If set to True, use test data from the test_data.txt file
USE_TEST_DATA=False

def get_input():
    if USE_TEST_DATA:
        with open(f"{get.get_day_and_year()[0]}/test_data.txt") as f:
            puzzle_data = f.read().splitlines()
    else:
        puzzle_data = data.splitlines()
    return puzzle_data

def get_lows(depths) -> list:
    num_rows=len(depths)
    row_length=len(depths[0])
    lows = []
    for y, x in itertools.product(range(num_rows), range(row_length)):
        if all([
            x==0 or depths[y][x] < depths[y][x-1],
            x==row_length-1 or depths[y][x] < depths[y][x+1],
            y==0 or depths[y][x] < depths[y-1][x],
            y==num_rows-1 or depths[y][x] < depths[y+1][x]
        ]):
            lows.append((x,y))
    return lows

def get_surrounding(depths, low) -> list:
    num_rows=len(depths)
    row_length=len(depths[0])
    surroundings = set()
    surroundings.add(low)
    x,y = low
    for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if i>=0 and i <row_length and j>=0 and j<num_rows:
            if depths[j][i] > depths[y][x] and int(depths[j][i])<9:
                surroundings.add((i,j))
                recursion=get_surrounding(depths, (i,j))
                surroundings.update(recursion)
    return surroundings

def part1(depths):
    risk_levels=[ int(depths[y][x])+1 for x,y in get_lows(depths) ]
    return sum(risk_levels)

def part2(depths):
    lows = get_lows(depths)
    sizes = [ len(get_surrounding(depths, low)) for low in lows ]
    sizes.sort(reverse=True)
    return prod(sizes[0:3])

input_data = get_input()

## Part 1
my_answer=part1(input_data)
print(f"Part 1: {my_answer}")
#submit(my_answer)

## Part 2
my_answer=part2(input_data)
print(f"Part 2: {my_answer}")
#submit(my_answer)
