# OOP allows you to structure your code using objects that combine data (attributes) and behavior (methods).
# Key concepts:
# - Class: a blueprint for creating objects
# - Object: an instance of a class
# - Inheritance: a class can inherit attributes and methods from another class
# - Special methods: methods with double underscores (dunder) like __init__, __str__

# 1. Defining a Class and Creating Objects
# --------------------------------------------------------------------------------------------------------
        class Person:
            """Class representing a person"""

            def __init__(self, name, age):
                """
                Special method __init__ is the constructor.
                It initializes object attributes when the object is created.
                """
                self.name = name
                self.age = age

            def greet(self):
                """Instance method to greet"""
                print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    # Creating an object (instance) of Person
    person1 = Person("Jose", 27)
    person1.greet()  # Hello, my name is Alice and I am 30 years old.

# 2. Inheritance
# --------------------------------------------------------------------------------------------------------
    class Student(Person):
        """Student class inherits from Person"""

        def __init__(self, name, age, student_id):
            # Call the parent constructor
            super().__init__(name, age)
            self.student_id = student_id

        def study(self):
            """Student-specific method"""
            print(f"{self.name} is studying.")

    # Creating a Student object
    student1 = Student("Jose", 27, "S12345")
    student1.greet()  # Inherited method
    student1.study()  # Student-specific method

# 3. Special Methods (__str__, __repr__)
# --------------------------------------------------------------------------------------------------------
    class Book:
        """Book class with special methods"""

        def __init__(self, title, author):
            self.title = title
            self.author = author

        def __str__(self):
            """
            __str__ defines the informal string representation of the object,
            used by print() and str().
            """
            return f"'{self.title}' by {self.author}"

        def __repr__(self):
            """
            __repr__ defines the official representation, useful for debugging.
            """
            return f"Book(title='{self.title}', author='{self.author}')"

    book1 = Book("1997", "The Life of Pi")
    print(book1)       # Uses __str__: '1984' by George Orwell
    print(repr(book1)) # Uses __repr__: Book(title='1984', author='George Orwell')

# 4. Encapsulation and Private Attributes
# --------------------------------------------------------------------------------------------------------
    class BankAccount:
        """Example of encapsulation with private attributes"""

        def __init__(self, owner, balance):
            self.owner = owner
            self.__balance = balance  # Private attribute

        def deposit(self, amount):
            """Add money to the account"""
            self.__balance += amount

        def withdraw(self, amount):
            """Withdraw money safely"""
            if amount <= self.__balance:
                self.__balance -= amount
                return amount
            else:
                print("Insufficient funds")
                return 0

        def get_balance(self):
            """Access private attribute safely"""
            return self.__balance

    account = BankAccount("Jose", 1000)
    account.deposit(500)
    print(account.get_balance())  # 1500
    account.withdraw(2000)        # Insufficient funds

    print(account.owner) # Public, so you can access it directly
    print(account.__balance) # Private attribute, trying to access it directly will raise an error