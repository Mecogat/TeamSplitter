def FN(nums):
    n = len(nums)
    result = [0, 0, 0, 0]
    min_diff = float('inf')

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                diff = abs(current_sum)

                if diff < min_diff:
                    min_diff = diff
                    result[0] = i
                    result[1] = j
                    result[2] = left
                    result[3] = right

                if current_sum < 0:
                    left += 1
                else:
                    right -= 1

    return result

