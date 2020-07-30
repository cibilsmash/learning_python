# printing out put


print("Hello All")

# variables and Data type

name = "cibil"

age = 24

for_float = 24.7

print("for variable and Data type output")

print(name)

print(age)

print(for_float)


print(str(name))


#complex in numbers

x = 1j

print(type(x))

#casting

to_float = float(1)

print(to_float)

#strings

coll = "karunya"

print(coll)

print(coll[3])

print(coll[0:4])

print(len(coll))

print(coll.upper())

print(coll.lower())

print(coll.upper().isupper())

print(coll.replace("karunya", "psg"))


type = " university"

print(coll + type)

for_next_line = "for\nnext\nline"

print(for_next_line)


# for boolean

a = 5

b = 5

if a == b:
    print("same")
else:
    print("not equal")



#operators

q = 1

w = 3

print(q + w * q / w % q)


# List

the_list = ["apple", "orange","mango"]


print(the_list[1])

for x in the_list:
    print(x)



if "apple" in the_list:
    print("yes")
else:
    print("no")

the_list.append("banana")

print(the_list)

#insert , remove, pop, clear()

the_list2 = ["1","2","3"]

the_list.extend(the_list2)

print(the_list)

# tuples same like list but unchangeable


#dictionaries///// this have keys and values


the_dictionary = {

    "name" : "cibil",
    "age" : "23",
}

print(the_dictionary)

for details in the_dictionary:

    print(the_dictionary[details])

the_dictionary["color"] = "black"

print(the_dictionary)

copied_dictionary = the_dictionary.copy()

print(copied_dictionary)


#nested Dictionary

nested_dictionary = {

    "user1":{
        "name":"cibil",
        "age":"23"
    },
    "user2":{
        "name":"arul",
        "age":"25"

    }


}

print(nested_dictionary["user1"])


#if else

v = 50

m = 40

if v < m or m < v:
    print("hello")

if v < m:
    print("is low")
else:
    print("v is high")

if v < m:
    print("it is low")

elif v > m:
    print("it is high")

else:
    print("error")

d = 1

while d < 10:

    print(d)

    d += 1

for x in the_list:
    if x == "orange":
       break

    print(x)

#functions

def first_function(num1,num2):

    return (num1 + num2)

print(first_function(3,6))

#lambda

def lam_funcyion(n):

    return lambda a : a * n
hj = lam_funcyion(3)

print(hj(6))


class person:

    def __init__(self,name, age):

        self.name = name

        self.age = age

    def view(self):

        print(self.name, self.age)



person1 = person("cibil", "23")

person1.view()





