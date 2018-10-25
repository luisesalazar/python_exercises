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

try:
    # w= person['weight']
    # size= 12
    #indice= "Masa " + 12

    div= 100/0
except KeyError as err:
    print ("weight key does not exist")
    print (err)
except TypeError as err:
    print ("There is an error of data type")
    print (err)
#general error
except Exception as err:
    print ("An error ocurred")
    print (err)