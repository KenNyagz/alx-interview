#!/usr/bin/python3
'''
determines if a given data set represents a valid UTF-8 encoding
'''


def validUTF8(data):
    '''determines if a given data set represents a valid UTF-8 encoding'''
    n_bytes = 0  # No of bytes in current UTF-8 chararcter

    mask1 = 1 << 7  # Masks to check the leading bits
    mask2 = 1 << 6

    for num in data:
        byte = num & 0XFF  # extract the 8 least significant bits of the int

        if n_bytes == 0:
            if (byte & mask1) == 0:  # Count no of leading 1s to get no bytes
                continue  # Single-byte character ASCII
            elif (byte & (mask1 | mask2)) == mask1:
                # Invalid byte (must start with 10xxxxxx if it's a contn byte)
                return False
            else:
                # Determine no of leading 1s in this utf-8 character
                leading_ones = 0
                while (byte & mask1) != 0:
                    leading_ones += 1
                    byte <<= 1

                if leading_ones == 1 or leading_ones > 4:
                    return False  # Invalid leading byte pattern

                n_bytes = leading_ones - 1  # No of continuation bytes exptd
        else:
            # Continuation bytes must start with 10
            if not (byte & mask1 and not (byte & mask2)):
                return False

            n_bytes -= 1

    return n_bytes == 0
