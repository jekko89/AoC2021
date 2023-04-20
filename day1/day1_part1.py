i = open("input.txt", "r")

previous = 0
count = -1
fail = 0
nums = []

for x in i:
    nums.append(int(x))

for y in nums:
    if y > previous:
        print("pass")
        print(str(y) + " > " + str(previous))
        count += 1
    else:
        print("fail")
        print(str(y) + " > " + str(previous))
        fail += 1
    previous = y

print("count is " + str(count))
