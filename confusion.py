for i in range(8):
    chunk = (input_48_bits >> (6 * (7 - i))) & 0x3F