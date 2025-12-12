"""
Numbers 0 through 99 in order

Dial starts at 50

Rotation:
    * L - left  (toward lower numbers)
    * R - right (toward higher numbers)
Distance: value which indicates how many clicks the dial should be rotated in
that direction

Examples
- Start at 11. R8 --> Now at 19
- 19 + L19 --> 0
- 0 + L1 --> 99
- 5 + L10 --> 95
- 95 + R5 --> 0

Answer: the number of times the dial is left pointing at 0 after any rotation in the sequence
"""

INPUT_FILE = './full_input.txt'
dial_val = 50
ans = 0

with open(INPUT_FILE) as f:
    for rotation in f:
        rotation = rotation.strip()
        dir, val = rotation[0], rotation[1:]
        val = int(val)

        if dir == 'R':
            dial_val += val
        else:
            dial_val -= val

        dial_val %= 100
        if dial_val == 0:
            ans += 1
    
print(f'Answer: {ans}')
