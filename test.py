shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
round_num = 0
left_half = 0xe7402934

print(format(left_half, "#034b"))
print(format(((left_half << shift_schedule[round_num])), "#034b"))
print(format(((left_half << shift_schedule[round_num])) & 0xffffffff, "#034b"))