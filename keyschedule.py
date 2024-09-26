def key_schedule(des_key_64_bits: int) -> list[int]:
    """
    Takes a 64-bit DES key as input and returns a list of 16 round keys, each 48 bits long.
    """
    # Permuted Choice 1 (PC-1)
    permuted_key = permuted_choice_1(des_key_64_bits)
    
    # Split the key into two 28-bit halves
    left_half = ________          # 28-bit left half
    right_half = ________         # 28-bit right half
    
    round_keys = []     # will be returned in the end
    shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    for round_num in range(16):
        # Apply left shifts according to the shift schedule
        left_half = _________     # See example below
        right_half = _________
        
        # Combine the halves and apply Permuted Choice 2 (PC-2)
        combined_key = _________
        round_key = permuted_choice_2(combined_key)
        round_keys.append(round_key)
    
    return round_keys