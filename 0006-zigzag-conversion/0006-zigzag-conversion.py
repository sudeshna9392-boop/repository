class Solution:
    def convert(seclasslf, s: str, numRows: int) -> str:
        # Edge case: if only one row or shorter string
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of strings, one for each row
        rows = [''] * numRows
        index, step = 0, 1

        for char in s:
            rows[index] += char

            # Reverse direction when reaching top or bottom
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step

        # Combine all rows
        return ''.join(rows)         