import employee

if __name__ == '__main__':
    emp = employee.Employee('John', 'Smith')
    print(emp.fullname)
    emp.fullname = 'Jane Doe'
    print(emp.email)
    print(emp.fullname)


