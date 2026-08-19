class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        rows = {}

        # Store reserved seats using bitmask
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = 0

            rows[row] |= 1 << (seat - 1)

        ans = 0

        # Check rows having reserved seats
        for seats in rows.values():

            # Can place 2 groups:
            # 2,3,4,5 and 6,7,8,9
            if (seats & 0b0111111110) == 0:
                ans += 2

            # Can place at least 1 group
            elif (
                (seats & 0b0000011110) == 0 or  # 2,3,4,5
                (seats & 0b0001111000) == 0 or  # 4,5,6,7
                (seats & 0b0111100000) == 0    # 6,7,8,9
            ):
                ans += 1

        # Rows with no reservations can fit 2 groups
        ans += (n - len(rows)) * 2

        return ans