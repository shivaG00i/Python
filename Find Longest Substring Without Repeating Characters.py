# 18. Find Longest Substring Without Repeating Characters
# Input: "abcabcbb" → Output: "abc"

#sliding window problem


def longest_unique_substring(s):
    start = 0               # Start of the current window
    max_len = 0             # Maximum length found so far
    max_sub = ""            # Longest substring found
    seen = {}               # Dictionary to track last seen index of each character


    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1  # move the window start
        seen[char] = i  # store/update the last seen index

        # check max length and store substring
        if i - start + 1 > max_len:
            max_len = i - start + 1
            max_sub = s[start:i+1]

    return max_sub

Substring = "abcabcbb"

print(longest_unique_substring(Substring))
# s = "p w w k e w"

'''

def longest_unique_substring(s):
    start = 0
    max_len = 0
    max_sub = ""
    seen = {}

    for end in range(len(s)):
        char = s[end]

        if char in seen and seen[char] >= start:
            start = seen[char] + 1  # move start ahead of the last seen position

        seen[char] = end  # store/update the latest index of char
        window_len = end - start + 1

        if window_len > max_len:
            max_len = window_len
            max_sub = s[start:end+1]

    return max_sub



'''