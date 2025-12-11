info=[#list
    ("Alice", "math"),#tuple
    ("bob","science"),
    ("Alice","science"),
    ("charlie","math"),
    ("bob","maths"),
    ("Alice","English"),
    ("Charlie","English"),
]

dict={}

for name,course in info:
    if(dict.get(name)==None):
        dict.update({name: set()})
        dict[name].add(course)

    else:
         dict[name].add(course)

print(dict)
