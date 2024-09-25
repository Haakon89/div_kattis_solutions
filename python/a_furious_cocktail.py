potions_and_speed=input().split(" ")
failure_test=0
for i in range(int(potions_and_speed[0])):
    potion_duration=input()
    if i==0:
        continue
    elif int(potion_duration)-int(potions_and_speed[1])<=0:
        print("NO")
        failure_test+=1
if failure_test==0:
    print("YES")
