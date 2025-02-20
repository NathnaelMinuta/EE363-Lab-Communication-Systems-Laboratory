'''
This is the second lab of EE363.

Purpose:
The purpose of this function is to determine the parity type and return a fixed output for "even" or "odd" types.

Procedure:
1. Accept `data` and `parity_type` as inputs.
2. Return '1' for "even" and '0' for "odd", ignoring `data` for now.
3. Maintain the function signature for future activities where `data` will be used.

Author: Nathnael Minuta
Student ID: 15778991
Date: 01/28/2025
'''

def calculate_parity(data: str, parity_type: str) -> str:
    if parity_type=="even":
        return '1'
    elif parity_type=="odd":
        return '0'
print(calculate_parity("1101", "even"))
print(calculate_parity("1101", "odd"))
