from typing import Literal

ALL_SORT_ORDERS = ['asc', 'desc']


def validate_list(
    values: list[int],
    order: Literal['asc'] | Literal['desc']
) -> bool:
    """Checks if list elements are ascending, if they increase max up by 3
            at a time, and if the elements are not the same"""

    last = None
    for v in values:
        if last is not None:
            val_larger_than_last = (
                last < v if order == 'asc' else last > v)
            difference_by_three_tops = (
                v - last <= 3 if order == 'asc' else last - v <= 3)

            if (
                val_larger_than_last is False or
                difference_by_three_tops is False
            ):
                return False
        last = v

    return True


safe_reports_count = 0
with open("input.txt", "r") as f:
    for row in f:
        nums = row.strip().split(" ")

        # Cast to integers
        nums = [int(num) for num in nums]

        # Run first validation check
        is_valid = any([validate_list(nums, so) for so in ALL_SORT_ORDERS])

        if not is_valid:
            # Try again but without the number at the issue index to see
            # if removing one element would make the list valid
            sublists = []
            for i in range(len(nums)):
                sublist = nums.copy()
                sublist.pop(i)
                sublists.append(sublist)

            if any([validate_list(s, o) for o in ALL_SORT_ORDERS for s in sublists]):
                safe_reports_count += 1
        else:
            safe_reports_count += 1

# Print the result
print(safe_reports_count)
