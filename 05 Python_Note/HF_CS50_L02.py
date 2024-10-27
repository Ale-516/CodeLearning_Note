# Le Jiang
# 2024/10/17
# topic: LOOP

# 01 WHILE LOOP
def P01_WHILE_LOOP():
    i = 3
    while i != 0:
        print ("meow")
        i = i - 1

    j = 0
    while j < 3:
        print("meow")
        j = j + 1
        # j += 1 equal to j = j + 1


# 02 FOR LOOP
def P02_FOR_LOOP(): 
    for i in [0, 1, 2]:
        # "[]" is used to convey a list
        print("meow")

    for _ in range(3):
        # import function to simplify our code
        # use "_" to express a vary, means that you DON'T CARE what the variable means, just for loop
        print("meow")

    print("meow\n" * 3, end="")
    # 默认情况下，print函数会自动将光标移动到下一行，所以需要对该函数进行一些修改。

    while True:
        n = int(input("what's n ?"))
        if n <= 0:
            continue 
            # means you continue staying in the loop
        else:
            break 
            # means jump out of the loop

    for _ in range(n):
        print("meow")

# 03 LIST
def P03_LIST():
    students = ["Hermione","Harry", "Ron"]

    for s in students:
        print(s)

    for i in range(len(students)):
        # function "len" can tell us the length of a str
        print(i+1, students[i])
        # print the names with number

# 04 DICT
def P04_DICT():
# this type of data allow you to associate one variable with another variable
# before the ";" is KEY, while after the ";" is VALUE   
    sh = {
        "Hermione"  :   "Gryffindor",
        "Harry"     :   "Gryffindor",
        "Ron"       :   "Gryffindor",
        "Draco"     :   "Slytherin",
        }
    print(sh["Hermione"])
    print(sh["Harry"])
    print(sh["Ron"])
    print(sh["Draco"])

    for s in sh:
        print(s)# only print the key, not the value associated with it
        print(s,sh[s],sep = ",")# can print both the key and the value
        # change the seperator from " " to ","
        # 当字典类被放入循环中去，被循环的只是键值

    shp = [
        {"name":"Hermione","house":"Gryffindor","patronus":"Otter"},
        {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
        {"name":"Ron","house":"Gryffindor","patronus":"Jack Russell terrier"},
        {"name":"Draco","house":"Slytherin","patronus":"None"}
    ]
    for s in shp:
        print(s["name"],s["house"],s["patronus"],sep = ",")
        # dict类只能通过键值调用

def P05_MARIO():
    size = 3
    # for each row
    for i in range(size):
        # for each column
        for j in range(size):
            print("#",end="")
        print()


#P01_WHILE_LOOP()

#P02_FOR_LOOP()

#P03_LIST()

#P04_DICT()

P05_MARIO()
