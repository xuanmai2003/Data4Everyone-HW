
number = int(input('How many B bacterias are there?'))
time = int(input('How much time will we wait?'))
if time%2==0:
    a = number*2*(time/2)
else:
    a =  number*2*((time-1)/2)
print('After',time,'minutes, we would have',a,'bacterias')