#get input
i = open("input.txt", "r")

#set variables
x = 0
y = 0

#parse inputs.  String first, then number.  String determines direction, number determines distance.
for line in i:
    values = line.split()
    if values[0] == "forward":
        x += int(values[1])
    if values[0] == "down":
        y += int(values[1])
    if values[0] == "up":
        y -= int(values[1])
    #loop through inputs and add values to x and y

#output final value:  (x * y = output)
print(x * y)

#success!
