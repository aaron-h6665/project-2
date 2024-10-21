def permute(data: int, table: list, bit_length: int) -> int:
    """
    General permutation function that applies the given permutation table to the data.
    
    Args:
        data: The input data to permute (int).
        table: The permutation table (list of bit positions).
        bit_length: The number of bits in the input (e.g., 48 for PC-2, 32 for P-box).
    
    Returns:
        The permuted data (int).
    """
    permuted_data = 0
    for i, pos in enumerate(table):
        permuted_data |= ((data >> (bit_length - pos)) & 1) << (len(table) - 1 - i)
    return permuted_data

pc1_table = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]

pc2_table = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
    ]

def key_schedule(des_key_64_bits: int) -> list[int]:
    """
    Takes a 64-bit DES key as input and returns a list of 16 round keys, each 48 bits long.
    """
    # Permuted Choice 1 (PC-1)
    permuted_key = permute(des_key_64_bits, pc1_table, 64)
    
    # Split the key into two 28-bit halves
    left_half = permuted_key >> 28          # 28-bit left half
    right_half = permuted_key & 0x0000000fffffff     # 28-bit right half
    
    round_keys = []     # will be returned in the end
    shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    for round_num in range(16):
        # Apply left shifts according to the shift schedule
        left_half = (left_half << shift_schedule[round_num] & 0xfffffff) | (left_half >> (28 - shift_schedule[round_num]))
        right_half = (right_half << shift_schedule[round_num] & 0xfffffff) | (right_half >> (28 - shift_schedule[round_num]))
        
        # Combine the halves and apply Permuted Choice 2 (PC-2)
        combined_key = (left_half << 28) | (right_half) 
        round_key = permute(combined_key, pc2_table, 56)
        round_keys.append(hex(round_key))
    
    return round_keys

if __name__ == "__main__":
    print(key_schedule(0x133457799bbcdff1))