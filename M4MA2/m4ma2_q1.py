class User():
    '''class that defines a user'''
    def __init__(self, first, last, dept='Unassigned', pnum='n/a'):
        self.first_name = first
        self.last_name = last
        self.fullname = first + ' ' + last
        self.email = first + '.' + last + '@usergroup.com'
        self.department = dept
        self.phone= pnum

    def describe_user(self):
        '''prints a user's information'''
        print('Name: ', self.fullname)
        print('Department: ', self.department)
        print('Email: ', self.email)
        print('Phone: ', self.phone)

    def greet_user(self):
        '''prints a greeting to a user'''
        print('Greetings, ', self.firstname, '!')

class Restaurant():
    '''A class that defines a restaurant'''
    def __init__(self, rname, ctype):
        self.restaurant_name = rname
        self.cuisine_type = ctype

    def describe_restaurant(self):
        '''Prints a description of the restaurant name and cuisine.'''
        print('Restaurant Name: ', self.restaurant_name)
        print('Cuisine Type: ', self.cuisine_type)
    
    def open_restaurant(self):
        '''Prints message that the restaurant is open'''
        print(self.restaurant_name, ' is open.')

#Part 1
restaurant = Restaurant('Rest Au Rant', 'foods')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

#Part 2
wendys = Restaurant("Wendy's", 'Hamburgers')
tacobell = Restaurant("Taco Bell", 'Mexican')
dq = Restaurant("Dairy Queen", "Desserts")

wendys.describe_restaurant()
tacobell.describe_restaurant()
dq.describe_restaurant()
    

    
