word = input()
n = int(input())
center_letter = word[0]
possible_letters = set(word)
res = []
for _ in range(n):
    current_word = input()
    word_set = set([letter for letter in current_word])
    if center_letter in word_set and len(current_word)>3 and word_set.issubset(possible_letters):
        res.append(current_word)
        # print(current_word)
    
print()
for elem in res:
    print(elem)