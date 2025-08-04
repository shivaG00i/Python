# 19. Group Anagrams Together Input: ["bat", "tab", "cat"]
# → Output: [["bat", "tab"], ["cat"]]
#
# what is anagrams
#
# "listen" and "silent" ✅ (same letters, rearranged)

from collections import defaultdict

strArry = ["bat", "tab", "cat"]

def group_anagrams(words):
    anagram_dict = defaultdict(list)

    for word in words:
        key = tuple(sorted(word.lower()))
        # or  key = ''.join(sorted(word.lower()))
        anagram_dict.setdefault(key, []).append(word)
    return list(anagram_dict.values())

print(group_anagrams(strArry))
