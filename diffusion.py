P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25,
]

input_32_bits = 0x12345678
acc = 0
for i in range(0, 32):
    acc |= ((input_32_bits >> (32 - P[i])) & 1) << (32 - (i + 1))

# remember the leading zeros are removed
print(bin(input_32_bits))
print(bin(acc))
