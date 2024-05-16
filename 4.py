"""
Groupin anagrams problem
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Given an array of strings, group anagrams together.
Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["ate","eat","tea"], ["nat","tan"], ["bat"]]
"""

from collections import defaultdict


def groupAnagrams(strs):
    di = defaultdict(list)
    for s in strs :
        count = [0] * 26
        for c in s:
            count[ord(c)-ord('a')] += 1
        di[tuple(count)].append(s)
    return di.values()

auto = input("Do you want to run the predefined test cases? (Y/n) : ")

if not auto or auto == 'Y' or auto == 'y':
    testCases = [["eat", "tea", "tan", "ate", "nat", "bat"], ["anagram", "nagaram", "margana",], ["a"], [""]]
    for tc in testCases:
        print(f"Input: {tc}")
        print(f"Output: {groupAnagrams(tc)}")
else:
    ip = input("Enter a list of strings separated by commas : ")
    print(f"Output: {groupAnagrams(ip.split(','))}")
