""" Day 2 LeetCode exercices
"""

# def destCity(paths=[[]]):
#     """=["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
#     """
#     result = ''
#     print(paths)
#     # print(destiny)
#     for i in paths:
#         print(i)
#         for j in i:
#             print(j)
#             result = j
#     return print(result)
# paths= [['a','s'],['e','u']]
       
nums = [1,54,3,6,9,4,5,98,3,8,6,87,32,6,7,43,8]
target = 9

def twoSum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the 
    two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may 
    not use the same element twice.

    You can return the answer in any order.
    
    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].

    """    
    for i in range(len(nums)):
        print(i, '= i -->', nums[i])
        for j in range(len(nums)):
            print(j, '= j -->', nums[j])
            guess = nums[i]+nums[j]
            print(str(target) + ' = ' + str(nums[i]+nums[j])+ ' ?' )
            if target == guess:
                result = [i, j]
                print('Objetivo: ' + str(target) + ' encontrado sumando ' + str(nums[i]) + '+' + str(nums[j]) + '. Los indices son: ' + str(result))            
                return result

    return "No pudimos encontrar el objetivo"
    

if __name__ == '__main__':
    twoSum(nums, target)