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

def diffusion(input_32_bits, p_box):
    acc = 0
    for i in range(0, 32):
        acc |= ((input_32_bits >> (32 - p_box[i])) & 1) << (32 - (i + 1))

    return acc

"""
# remember the leading zeros are removed
print(bin(input_32_bits))
print(bin(acc))
"""

# old test code
# # formated to include the leading zeros
# print(format(input_32_bits, "#034b"))
# print(format(acc, "#034b"))
