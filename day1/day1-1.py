def rotate(curr_dial_pos: int, rot_dir: str, rot_val: int) -> int:
    new_dial_pos = curr_dial_pos
    match rot_dir:
        case 'L':
            new_dial_pos -= rot_val
        case 'R':
            new_dial_pos += rot_val
        case _:
            raise ValueError(f"Invalid rotation direction {rot_dir}")

    new_dial_pos %= 100
    return new_dial_pos


def sol(input_file: str) -> int:
    curr_dial_pos = 50
    ans = 0
    with open(input_file) as f:
        for rotation in f:
            rotation = rotation.strip()
            rot_dir, rot_val = rotation[0], rotation[1:]
            rot_val = int(rot_val)
            curr_dial_pos = rotate(curr_dial_pos, rot_dir, rot_val)
            if curr_dial_pos == 0:
                ans += 1
    return ans
    
sample_ans = sol('./sample.txt')
assert sample_ans == 3, f"Expected 3, got {sample_ans}"

ans = sol('./full.txt')
print(f'Answer: {ans}')
