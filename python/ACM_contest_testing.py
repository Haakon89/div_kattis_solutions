#scoring: number of completed tasks and sum of time at solved problems + 20sec for each wrong attempt
completed_tasks=0
time_used=0
letters_completed=""
letters_failed=""
test=["1"]
while test[0]!="-1":
    test=input().split(" ")
    if test[0]=="-1":
        break
    if test[2]=="right":
        letters_completed+=test[1]
        completed_tasks+=1
        time_used+=int(test[0])
        if test[1] in letters_failed:
            time_used+=20*letters_failed.count(test[1])
    else:
        letters_failed+=test[1]
print(f"{completed_tasks} {time_used}")