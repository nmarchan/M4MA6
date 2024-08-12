'''This represents the "final" version of the program as it is supposed to exist after all the changes.'''
class User():
    '''class that defines a user'''
    def __init__(self, first, last, dept='Unassigned', pnum='n/a'):
        self.first_name = first
        self.last_name = last
        self.fullname = first + ' ' + last
        self.email = first + '.' + last + '@usergroup.com'
        self.department = dept
        self.phone= pnum
        self.login_attempts = 0

    def describe_user(self):
        '''prints a user's information'''
        print('Name: ', self.fullname)
        print('Department: ', self.department)
        print('Email: ', self.email)
        print('Phone: ', self.phone)

    def greet_user(self):
        '''prints a greeting to a user'''
        print('Greetings, ', self.firstname, '!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
    '''defines basic privileges for an administrative user'''
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        '''method for printing privileges'''
        print('privileges: ', self.privileges)    

class Admin(User):

    def __init__(self, first, last, dept='Unassigned', pnum='n/a'):
        super().__init__(first, last, dept='Unassigned', pnum='n/a')
        #privileges from class for #12
        self.priv = Privileges()

class Restaurant():
    '''A class that defines a restaurant'''
    def __init__(self, rname, ctype):
        self.restaurant_name = rname
        self.cuisine_type = ctype
        self.number_served = 0

    def describe_restaurant(self):
        '''Prints a description of the restaurant name and cuisine.'''
        print('Restaurant Name: ', self.restaurant_name)
        print('Cuisine Type: ', self.cuisine_type)
    
    def open_restaurant(self):
        '''Prints message that the restaurant is open'''
        print(self.restaurant_name, ' is open.')

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, customers=1):
        self.number_served += customers

class IceCreamStand(Restaurant):

    def __init__(self, rname, ctype):
        super().__init__(rname, ctype)
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Neopolitan']

    def show_flavors(self):
        print('Flavors: ', self.flavors)

#creates ice cream stand and shows its flavors
iscream = IceCreamStand('Iscream Uscream', 'ice cream')
iscream.show_flavors()

#Shows privileges
kj = Admin('Katherine', 'Janeway')
kj.priv.show_privileges()

ja = Admin('Jonathan', 'Archer')
ja.priv.show_privileges()
