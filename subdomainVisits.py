""" Day 1 LeetCode exercices
"""

import collections


def subdomainVisits(cpdomains):
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
    ####################### LEETCODE SOLUTION

    # ans = collections.Counter()
    # for domain in cpdomains:
    #     count, domain = domain.split()
    #     count = int(count)
    #     frags = domain.split('.')
    #     for i in range(len(frags)):
    #         print(frags)
    #         print(i, count)
    #         print(ans)
    #         ans[".".join(frags[i:])] += count

    # return print(["{} {}".format(ct, dom) for dom, ct in ans.items()])

    ###################### FIRST APPROACH...



    ###################### REVIEW OF SAME APPROACH

    result = {}
    for i in cpdomains:
        visits, domain = i.split()
        visits = int(visits)
        subdomains = domain.split('.')
        for i in range(len(subdomains)):
            sub = '.'.join(subdomains[i:])
            print(sub)
            if sub in result:
                result[sub] += visits
            else:
                result[sub] = visits
    final_result = ["{} {}".format(value, key) for key, value in result.items()]
    
    return print(final_result)

if __name__ == '__main__':
    subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])