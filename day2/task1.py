safe_reports_count = 0
with open("input.txt", "r") as f:
    for row in f:
        nums = row.strip().split(" ")

        # Handle 1 element list case
        if len(nums) == 1:
            safe_reports_count += 1  # I suppose this means a safe report?
            continue

        # Cast to integers
        nums = [int(num) for num in nums]

        # Check if element two is smaller than element one
        if nums[0] > nums[1]:
            # If the second number is smaller than the first one,
            # reverse the list. Now we can always check for the ASC scenario
            nums.reverse()

        # Go through numbers and check if value increases maximally up by 3
        # on each loop iteration
        last = None
        valid = True
        for num in nums:
            if last is not None:
                num_larger_than_last = last <= num
                diffrence_by_three_tops = num - last <= 3
                elements_not_equal = last != num

                if not (
                    num_larger_than_last and
                    diffrence_by_three_tops and
                    elements_not_equal
                ):
                    valid = False
                    break
            last = num

        if valid:
            safe_reports_count += 1

# Print the result
print(safe_reports_count)
