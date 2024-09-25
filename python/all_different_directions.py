test_cases=int(input())
combined_longitued=0
combined_latitued=0
for i in range(test_cases):
    info=input().split(" ")
    start_position_longditued=float(info[0]) 
    start_position_latitued=float(info[1])
    facing_direction=float(info[3])
    for j in range(4, len(info)-len(info[4:])):
        if info[j] == "turn":
            facing_direction+=float(info[j+1])
        elif info[j] == "walk":
            if facing_direction==90.0 or facing_direction==-90.0:
                start_position_longditued-=float(info[j+1])
            elif facing_direction<0:
                start_position_latitued-=float(info[j+1])
            elif facing_direction>0:
                start_position_latitued+=float(info[j+1])
            else:
                start_position_longditued+=float(info[j+1])
    combined_longitued+=start_position_longditued
    combined_latitued+=start_position_latitued
print(f"{combined_latitued/test_cases} {combined_longitued/test_cases}")