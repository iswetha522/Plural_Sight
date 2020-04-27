# Python supports bitwise - operators :
# & - and
# | - or
# << - left shift
# >> - right shift


def _int32_to_bytes(i):
    """Convert an integer to four bytes in little - endian format"""
    # & : Bitwise - and
    # >> : Right - shift
    return bytes((i & 0xff,
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff))


print(_int32_to_bytes(6)) # b'\x06\x00\x00\x00'
print(_int32_to_bytes(108)) # b'l\x00\x00\x00'