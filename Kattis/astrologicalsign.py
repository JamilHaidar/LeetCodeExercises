months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
days =   [21   ,20   ,21   ,21   ,21   ,22   ,23   ,23   ,22   ,23   ,23   ,22]
signs = ['Capricorn','Aquarius','Pisces','Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius']
t = int(input())
while t:
    day,month = input().split()
    idx = months.index(month)
    if int(day)<days[idx]:
        print(signs[idx])
    else:
        print(signs[(idx+1)%12])
    t -= 1