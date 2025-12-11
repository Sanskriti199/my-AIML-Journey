info=[#list
    ("Alice", "math"),#tuple
    ("bob","science"),
    ("Alice","science"),
    ("charlie","math"),
    ("bob","maths"),
    ("Alice","English"),
    ("Charlie","English"),
]
unique_course=set()

for tup in info:
    unique_course.add(tup[1]) #course
print(unique_course)

#another method of writing it 
# for name,course in info:
# print(name,course)