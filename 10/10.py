from aocd import submit
from aocd import get
from aocd import data

# If set to True, use test data from the test_data.txt file
USE_TEST_DATA=False

brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
completion_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def get_input():
    if USE_TEST_DATA:
        with open(f"{get.get_day_and_year()[0]}/test_data.txt") as f:
            puzzle_data = f.read().splitlines()
    else:
        puzzle_data = data.splitlines()
    return puzzle_data

def part1(puzzle_input):
    total_points = 0
    for line in puzzle_input:
        expecting = []
        for char in line:
            if char in brackets:
                # Open chunk
                expecting.append(brackets[char])
            else:
                expect_char = expecting.pop()
                if char != expect_char:
                    # Unexpected close of chunk
                    #print(f"Error: Expected {expect_char} but found {char} instead")
                    total_points+=points[char]
    return total_points

def part2(puzzle_input):
    completion_strings = []

    for line in puzzle_input:
        syntax_error=False
        expecting = []
        for char in line:
            if char in brackets:
                # Open chunk
                expecting.append(brackets[char])
            elif char != expecting.pop():
                # Unexpected close of chunk
                pass
                syntax_error=True
        if not syntax_error:
            # Incomplete line
            completion_strings.append(expecting)

    completion_scores = []
    for completion_string in completion_strings:
        completion_score = 0
        for char in completion_string[::-1]:
            completion_score*=5
            completion_score+=completion_points[char]
        completion_scores.append(completion_score)

    completion_scores.sort()
    return completion_scores[len(completion_scores)//2]

input_data = get_input()

## Part 1
my_answer=part1(input_data)
print(f"Part 1: {my_answer}")
#submit(my_answer)

## Part 2
my_answer=part2(input_data)
print(f"Part 2: {my_answer}")
#submit(my_answer)
