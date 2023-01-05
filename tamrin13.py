Hour = int(input())
Rate = 20
if Hour < 30 :
    result = Hour * Rate
    print(result)
elif Hour >= 30 :
    result = (Hour - 30) * (15) + 500
    print(result)
print ('Well done zahra Bravo !')