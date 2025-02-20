'''
This is the second lab of EE363.

Purpose:
The purpose of this function is to append a parity bit ('1' or '0') to a binary string based on the specified parity type.

Procedure:
1. Define a function `append_parity` that accepts `data` and `parity_type`.
2. Depending on the `parity_type`:
   - Append '1' for "even".
   - Append '0' for "odd".
3. Return the modified string.

Author: Nathnael Minuta
Student ID: 15778991
Date: 01/28/2025
'''
def append_parity(data: str, parity_type: str) -> str:
    if parity_type=="even":
        return data+'1'
    elif parity_type=="odd":
        return data+'0'
print(append_parity("1101", "even"))
print(append_parity("1101", "odd"))
