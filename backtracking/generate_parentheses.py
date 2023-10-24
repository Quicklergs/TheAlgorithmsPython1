"""
author: Aayush Soni
Given n pairs of parentheses, write a function to generate all
combinations of well-formed parentheses.
Input: n = 2
Output: ["(())","()()"]
Leetcode link: https://leetcode.com/problems/generate-parentheses/description/
"""


def generateParenthesis(n: int) -> list[str]:
    """
    Generate valid combinations of balanced parentheses for a given n.

    :param n: An integer representing the number of pairs of parentheses.
    :return: A list of strings with valid combinations.

    This function uses a recursive approach to generate the combinations.

    Time Complexity: O(2^(2n)) - In the worst case, we have 2^(2n) combinations.
    Space Complexity: O(2n) - Space used for recursion, where 'n' is the number of pairs.

    Example 1:
    >>> generateParenthesis(3)
    ['((()))', '(()())', '(())()', '()(())', '()()()']

    Example 2:
    >>> generateParenthesis(1)
    ['()']
    """

    def backtrack(partial, open_count, close_count):
        if len(partial) == 2 * n:
            result.append(partial)
            return

        if open_count < n:
            backtrack(partial + "(", open_count + 1, close_count)

        if close_count < open_count:
            backtrack(partial + ")", open_count, close_count + 1)

    result = []
    backtrack("", 0, 0)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
