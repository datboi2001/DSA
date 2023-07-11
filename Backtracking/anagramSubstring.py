from collections import Counter

def sherlockAndAnagrams(s):
    """
    Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
    Constraint: 2 <= s <= 100
    """
    
    # Main idea: Count all substrings and sort them. If two substrings are anagrams, they will be the same after sorting.
    # At the end, we loop through the dictionary and count the number of pairs of anagrams.
    # Time complexity: O(n^2 * log(n)) because of sorting

    substr_count = {}
    for i in range(len(s)):
        for j in range(i, len(s)):
            cur = s[i:j + 1]
            cur = ''.join(sorted(cur))
            substr_count[cur] = substr_count.get(cur, 0) + 1
    # v * (v-1) //2 is the number of pairs of v elements
    return sum([(v * (v - 1) // 2) for v in substr_count.values()])

