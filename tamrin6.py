Hours = input()
Rate = 8
try :
    Hour = int(Hours)
except :
    Hour = -1
    print('Error, please enter number input')

if Hour < 30 :
    result = Hour * Rate
    print(result)
if Hour > 30 :
    result = (Hour - 30) * (15) + 400
    print(result)
