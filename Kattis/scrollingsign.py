n = int(input())
while n:
    k, w = list(map(int,input().split()))
    previous_word = input()
    w -= 1
    count = k
    while w:
        current_word = input()
        first_letter = current_word[0]
        for index in range(k):
            if first_letter == previous_word[index] and previous_word[index:] == current_word[:(k-index)]:
                break
            count += 1
        w -= 1
        previous_word = current_word
    print(count)
    n-=1