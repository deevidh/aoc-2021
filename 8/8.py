from aocd import submit
from aocd import get
from aocd import data

# If set to True, use test data from the test_data.txt file
USE_TEST_DATA=False

def get_input():
    if USE_TEST_DATA:
        with open(f"{get.get_day_and_year()[0]}/test_data.txt") as f:
            puzzle_data = f.read().splitlines()
    else:
        puzzle_data = data.splitlines()
    return puzzle_data

def part1(digits):
    total2347 = 0
    for line in digits:
        pattern, output = line.split("|")
        outputs = output.split(" ")
        total2347 += sum(len(output) in [2,3,4,7] for output in outputs)
    return total2347

# Segments:
#
#  AAAA
# B    C
# B    C
#  DDDD
# E    F
# E    F
#  GGGG
def part2(input_data):
    decoded_outputs = []
    for line in input_data:
        pattern_string, output_string = line.split("|")
        patterns = [ "".join(sorted(pattern)) for pattern in pattern_string.strip().split(" ") ]
        outputs = [ "".join(sorted(output)) for output in output_string.strip().split(" ") ]
        digit = [None] * 10

        # Easy digits (unique numbers of segments)
        digit[1]=next(pattern for pattern in patterns if len(pattern) == 2)
        digit[4]=next(pattern for pattern in patterns if len(pattern) == 4)
        digit[7]=next(pattern for pattern in patterns if len(pattern) == 3)
        digit[8]=next(pattern for pattern in patterns if len(pattern) == 7)
        patterns.remove(digit[4])
        patterns.remove(digit[7])
        patterns.remove(digit[8])

        # digit 6 is only 6 segment pattern which doesn't contain digit 1
        digit[6]=next(pattern for pattern in patterns if len(pattern) == 6 and not all([character in pattern for character in digit[1]]))
        patterns.remove(digit[6])

        # digit 3 is only 5 segment pattern which contains digit 1
        digit[3]=next(pattern for pattern in patterns if len(pattern) == 5 and all([character in pattern for character in digit[1]]))
        patterns.remove(digit[3])

        # segment C is only segment not in digit 6
        segmentC=next(character for character in 'abcdefg' if character not in digit[6])

        # digit 2 is only remaining 5 segment digit that contains segment C
        digit[2]=next(pattern for pattern in patterns if len(pattern) == 5 and segmentC in pattern)
        patterns.remove(digit[2])

        # digit 5 is only remaining 5 segment digit
        digit[5]=next(pattern for pattern in patterns if len(pattern) == 5)
        patterns.remove(digit[5])

        # segment E is only segment in digit 6 and not in digit 5
        segmentE=next(character for character in digit[6] if character not in digit[5])

        # digit 0 is only 6 segment digit which contains segment E
        digit[0]=next(pattern for pattern in patterns if len(pattern) == 6 and segmentE in pattern)
        patterns.remove(digit[0])

        # digit 9 is only remaining 6 segment digit
        digit[9]=next(pattern for pattern in patterns if len(pattern) == 6)
        patterns.remove(digit[9])

        decoded_output = int("".join([ str(digit.index(output)) for output in outputs ]))
        decoded_outputs.append(decoded_output)

    return sum(decoded_outputs)

input_data = get_input()

## Part 1
my_answer=part1(input_data)
print(f"Part 1: {my_answer}")
#submit(my_answer)

## Part 2
my_answer=part2(input_data)
print(f"Part 2: {my_answer}")
#submit(my_answer)
