""" Day 1 LeetCode exercices
"""

def sortArrayByParity(A):
    """
    Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
    You may return any answer array that satisfies this condition.

    Example 1:
    Input: [3,1,2,4]
    Output: [2,4,3,1]
    The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
    """
    # # FIRST APPROACH
    # #declarar variables una para pares y otra para impares.
    # pares = []
    # impares = []
    #    
    # #for recorrer la lista y separarlos
    # for i in A:
    #     if i % 2 == 0:
    #         pares.append(i)
    #     else:
    #         impares.append(i)
    #   
    # #juntar la lista y retornar el output que nos piden.
    # return print(pares + impares)
    return print(sorted(A, key = lambda x : x%2))

    # ordered_list = A.copy()

    # for i in A:
    #     if i%2==1:
    #         ordered_list.append(i)
    #         ordered_list.remove(i)
    # return print(ordered_list)

    # MORE CLEVER APROACH: Reduces memory usage and code
    # return print(sorted(A, key = lambda x : x % 2))


import collections


# def subdomainVisits(cpdomains):
"""
A website domain like "discuss.leetcode.com" consists of various subdomains. 
At the top level, we have "com", at the next level, we have "leetcode.com", and at the 
lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", 
we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this 
domain received), followed by a space, followed by the address. An example of a count-paired 
domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired 
domains, (in the same format as the input, and in any order), that explicitly counts the 
number of visits to each subdomain.

Example 1:
Input: 
["9001 discuss.leetcode.com"]
Output: 
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation: 
We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain 
"leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.
"""
    # ans = collections.Counter()
    # for domain in cpdomains:
    #     count, domain = domain.split()
    #     count = int(count)
    #     frags = domain.split('.')
    #     for i in range(len(frags)):
    #         ans[".".join(frags[i:])] += count

    # return print(["{} {}".format(ct, dom) for dom, ct in ans.items()])


def subdomainVisits(cpdomains):
        #recorrer el array. separar los strings: int del string.
    result = {}
    for i in cpdomains:
        temp = i.split()
        result[temp[1]] = int(temp[0])
    for i in result.keys():
        temp = i.split('.')
        print(temp)

    # print(resutl)
    # tuple_list = [value, key for key, value in result.items()]
    # print(tuple_list)

    # final_result = []
    # for i in tuple_list:
    #     tuple_string = ''.join(i)
    #     final_result.append(tuple_string)
    
    return print(list(result.items()))

if __name__ == '__main__':
    sortArrayByParity([3, 1, 2, 4])
    # subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])