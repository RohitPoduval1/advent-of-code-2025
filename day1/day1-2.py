def rotate(curr_dial_pos: int, rot_dir: str, rot_val: int) -> [int, int]:
    """Rotate the given dial position based on the direction and value.
    Args:
        rot_val: Assumed to be between 0 and 99. `rotate()` will not factor
        in multiple rotations due to rot_val being greater than 100.

    Returns:
        2-tuple of...
            1. the new dial position after the rotation
            2. How many times 0 was passed. Note that landing on 0 does not
            count as passing 0
    """
    num_passes_0 = 0
    if (
        (rot_dir == 'L' and curr_dial_pos - rot_val < 0 and curr_dial_pos != 0) or
        (rot_dir == 'R' and curr_dial_pos + rot_val > 100)
    ):
        num_passes_0 = 1

    new_dial_pos = curr_dial_pos
    match rot_dir:
        case 'L':
            new_dial_pos -= rot_val
        case 'R':
            new_dial_pos += rot_val
        case _:
            raise ValueError(f"Invalid rotation direction {rot_dir}")

    new_dial_pos %= 100
    return new_dial_pos, num_passes_0


def sol(input_file: str) -> int:
    curr_dial_pos = 50
    ans = 0
    with open(input_file) as f:
        for rotation in f:
            rotation = rotation.strip()
            rot_dir, rot_val = rotation[0], rotation[1:]
            rot_val = int(rot_val)

            # Rotating more than 100 in any direction will lead to passing 0
            if rot_val > 100:
                num_rotations = rot_val // 100
                ans += num_rotations
                rot_val %= 100

            curr_dial_pos, num_passes_0 = rotate(curr_dial_pos, rot_dir, rot_val)
            ans += num_passes_0
            if curr_dial_pos == 0:
                ans += 1

    return ans
    

sample_sol = sol('sample.txt')
assert sample_sol == 6, f"Expected 6, got {sample_sol}"

sample2_sol = sol('sample2.txt')
assert sample2_sol == 8, f"Expected 8, got {sample2_sol}"

ans = sol('full.txt')
print(f'Answer: {ans}')
