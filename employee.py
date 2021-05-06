class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + "." + last + '@email.com'

    def email(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

