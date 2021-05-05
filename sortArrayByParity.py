
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

    # SECOND APPROACHGIT
    # ordered_list = A.copy()
    # for i in A:
    #     if i%2==1:
    #         ordered_list.append(i)
    #         ordered_list.remove(i)
    # return print(ordered_list)

    # MORE CLEVER APROACH: Reduces memory usage and code
    # return print(sorted(A, key = lambda x : x % 2))


if __name__ == '__main__':
    # sortArrayByParity([3, 1, 2, 4])