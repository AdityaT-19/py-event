"""
Two Sum II problem
# Suggested code may be subject to a license. Learn more: ~LicenseLog:872597672.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:2210877406.
The problem is given a sorted array of integers numbers that is already sorted in non-decreasing order, 
# Suggested code may be subject to a license. Learn more: ~LicenseLog:313185567.
find two numbers such that they add up to a specific target number.

In this problem, each input would have exactly one solution.

You may not use the same element twice.
"""

# Suggested code may be subject to a license. Learn more: ~LicenseLog:3210500123.
def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [numbers[l], numbers[r]]
        elif s < target:
            l += 1
        else:
            r -= 1
    
    return "No Solution"

auto = input("Do you want to run the predefined test cases? (Y/n) : ")

if not auto or auto == 'Y' or auto == 'y':
    testCases = [
        [[2, 7, 11, 15], 9],
        [[2, 3, 4], 6],
        [[1, 2, 3, 4], 5],
        [[1 ,3, 5, 6], 5]]

    for testCase in testCases:
        print(f"For array : {testCase[0]} and target {testCase[1]}")
        print(twoSum(testCase[0], testCase[1]))
        print()
    
else:
    ip = input("Enter the array : ")
    arr = list(map(int, ip.split()))
    ip = input("Enter the target : ")
    target = int(ip)
    print(twoSum(arr, target))

