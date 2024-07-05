#Task 1
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]

sampleList = set(sampleList)
sampleSet.update(sampleList)

print("Task 1: ", sampleSet)

#Task 2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

intersection = set1.intersection((set2))

print("Task 2: ", intersection)

#Task 3
set1.difference_update(set2)
set1.update(set2)

print("Task 3: ", set1)