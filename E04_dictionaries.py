person={
    "name": "luis",
    "last_name": "salazar",
    "age": "35",
    "favorite_movies": ['uno', 'dos', 'tres'],
    "favorites_books":[{
            "title":"primer libro",
            "author": "primer autor"
        },
        {
            "title":"segundo libro",
            "author": "segundo autor"
        }
    ]

}

print (person)
print (person['name'])
print (person['favorite_movies'])
print (person['favorites_books'])

print (person.keys())
print (person.values())

#remove a key
del person['age']
print (person)

#get default value if key does not exist
print (person.get("age", "Unknown"))

