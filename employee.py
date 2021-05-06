class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + "." + last + '@email.com' 

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

