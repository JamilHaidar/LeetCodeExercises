while True:
    r = 10
    l = 1
    guess = int(input())
    if guess == 0:break
    
    while True:
        response = input()
        if response == "too high":
            r = min(r,guess-1)
        elif response == "too low":
            l = max(l,guess+1)
        else:
            if l<=guess<=r:
                print("Stan may be honest")
            else:
                print("Stan is dishonest")
            break
        guess = int(input())