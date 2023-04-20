i = open("input.txt", "r")

previous = 0
count = -1
triplet_sums = []
nums = []

for x in i:
    nums.append(int(x))

for y in range(0,len(nums)-2):
    total = 0
    try:
        total = nums[y] + nums[y+1] + nums[y+2]
        triplet_sums.append(int(total))
    except IndexError:
        print("end reached")

for z in triplet_sums:
    if z > previous:
        count+=1
    previous = z

print("count is " + str(count))
