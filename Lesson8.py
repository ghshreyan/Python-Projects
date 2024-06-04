class Database:
    def __init__(self, name, host, port, db_name, password):
        self.name = name
        self.host = host
        self.port = port
        self.db_name = db_name
        self.password = password


db = Database('Test', 'db_test.aws.com', 5432, 'test_db', 'XXXXXXX')

# print(db.name, db.port, db.host, db.db_name, db.password)
# print(db.name, db.port, db.host, db.db_name, db.password, db.url)
print(db)


class Person:
    # this is a function that sets the inputs required by the class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.age_squared = age*age

    # def __str__(self):
    #     return 'Dummy'

    def __str__(self):
        return 'Name: ' + self.name + ' Age:' + str(self.age)



p1 = Person('Hisham', 20)
p2 = Person('Shreyan', 50)
p3 = Person('Sergio', 90)

print(p1)
print(p2)
print(p3)



