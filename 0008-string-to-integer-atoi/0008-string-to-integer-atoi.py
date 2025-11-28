class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Step 1: Remove leading whitespaces
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Check sign
        sign = 1
        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        # Step 3: Read digits
        num_str = ""
        for char in s:
            if char.isdigit():
                num_str += char
            else:
                break

        # Step 4: If no digits found
        if not num_str:
            return 0

        # Step 5: Convert to integer
        num = sign * int(num_str)

        # Step 6: Clamp to 32-bit signed integer range
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
        