# AoC - Day 9

[https://adventofcode.com/2021/day/9](https://adventofcode.com/2021/day/9)

My solution to this challenge used a fairly direct approach with lots of conditional checks to establish a point's relation to it's neighbours and the edges of the map.  To calculate basin sizes I used some recursion, and stored data in a set to ensure that duplicate points were excluded.

TIL:

- You can't initialise a set with `varname = {}` :facepalm:
