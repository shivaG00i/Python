# 22. Count Number of Words Starting with a
#     Vowel Input: ["apple", "banana", "orange"] → Output: 2


list1=["apple", "banana", "orange"]
vowels='aeiou'

count=0
for word in list1:
    if word[0].lower() in vowels:
        count=count+1
print(count)

'''
or 

def count_vowel_starts(words):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for word in words:
        if word and word[0].lower() in vowels:
            count += 1
    return count
    
    
words = ["apple", "banana", "orange"]
print(count_vowel_starts(words))  # Output: 2




'''