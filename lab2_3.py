'''
This is the second lab of EE363.

Purpose:
The purpose of this function is to verify if the parity bit in a binary string matches the specified parity type.

Procedure:
1. Extract the parity bit from the binary string.
2. Check the parity type and compare it with the parity bit.
3. Return True if they match; otherwise, return False.

Author: Nathnael Minuta
Student ID: 15778991
Date: 01/28/2025
'''

def verify_parity(data: str, parity_type: str) -> str:
    # Extract the parity bit (last bit of the string)
    parity_bit = int(data[-1])
    # Determine the expected parity based on the parity type
    expected_parity = 1 if parity_type == "even" else 0
    # Compare the parity bit with the expected parity
    return parity_bit == expected_parity
print(verify_parity("11011", "even")) # Output: True
print(verify_parity("11010", "odd")) # Output: True
print(verify_parity("11011", "odd")) # Output: False
