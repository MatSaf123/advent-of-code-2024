def is_ordered(values: list[int]):
    """Checks if values present in the list are ordered in ascending manner"""
    return all(values[i] <= values[i+1] for i in range(len(values) - 1))


safe_reports_count = 0
with open("input.txt", "r") as f:
    for row in f:
        nums = row.strip().split(" ")

        # Cast to integers
        nums = [int(num) for num in nums]

        # Check for duplicates - those rows can be skipped already
        if len(list(set(nums))) != len(nums):
            continue

        # Check if list is ordered either in asc or desc manner
        if not is_ordered(nums):
            # Reverse the list, now desc becomes asc
            nums.reverse()

            # Check again
            if not is_ordered(nums):
                # Not ordered, skip
                continue

        # Go through numbers and check if value increases maximally up by 3
        # on each loop iteration
        last = None
        valid = True
        for num in nums:
            if last is not None:
                num_larger_than_last = last < num
                diff = num - last

                if not (
                    num_larger_than_last and
                    diff <= 3
                ):
                    valid = False
                    break

            if not valid:
                break
            last = num

        if valid:
            safe_reports_count += 1

# Print the result
print(safe_reports_count)
