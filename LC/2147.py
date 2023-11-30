# corridor = "SSPPSPS"
corridor = "PPSPSP"
corridor = 'SPPSSSSPPS'
# corridor = 'S'
couches_passed = 0
ans = 1
plants = 0
for letter in corridor:
    if letter == 'S':
        couches_passed += 1
    else:
        if couches_passed==2: plants += 1
    if couches_passed==3: 
        ans = ans*(plants+1)%(10**9+7)
        couches_passed = 1
        plants = 0
if couches_passed==1:print(0)
print(ans)