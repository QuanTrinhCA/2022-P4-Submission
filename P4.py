timetable = list()
for line in range(int(input())):
    timetable.append(int(input()))

for element in range((timetable.__len__() / 2) - 1):
    difference = timetable[element] - timetable[0]
    currenttime = int()
    counter = 1
    while currenttime <= timetable[(timetable.__len__() - 1)]:
        currenttime = timetable[0] + (difference * counter)
        counter += 1


    


print(str(currenttime))