# OOP (Object-Oriented Programming) allows us to structure code using classes and objects.
# It helps to organize logic, promote code reuse, and represent real-world entities.

# 1. BASIC CLASS STRUCTURE
# --------------------------------------------------------------------------------------------------------
    # Define a class with attributes (variables) and methods (functions).

    class Animal:
        def __init__(self, name, species):
            # Instance attributes
            self.name = name
            self.species = species

        def make_sound(self):
            print(f"{self.name} makes a generic sound.")

    # Create an object (instance)
    dog = Animal("Buddy", "Dog")
    dog.make_sound()


# 2. INHERITANCE
# --------------------------------------------------------------------------------------------------------
# One class (child) can inherit from another (parent), reusing or extending its functionality.

    class Dog(Animal):
        def __init__(self, name, breed):
            # Call parent constructor using super()
            super().__init__(name, species="Dog")
            self.breed = breed

        # Override parent method
        def make_sound(self):
            print(f"{self.name} barks!")

    dog = Dog("Max", "Golden Retriever")
    dog.make_sound()  # Uses overridden method
    print("Breed:", dog.breed)


# 3. ENCAPSULATION
# --------------------------------------------------------------------------------------------------------
    # Controlling access to class attributes and hiding internal details.

    class BankAccount:
        def __init__(self, owner, balance):
            self.owner = owner          # Public attribute
            self._balance = balance     # Protected (convention: should not be accessed directly)
            self.__pin = 1234           # Private (name-mangled, cannot be accessed directly)

        def deposit(self, amount):
            self._balance += amount
            print(f"Deposited {amount}, new balance: {self._balance}")

        def withdraw(self, amount, pin):
            if pin == self.__pin:
                if amount <= self._balance:
                    self._balance -= amount
                    print(f"Withdrew {amount}, new balance: {self._balance}")
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid PIN.")

    account = BankAccount("Jose", 1000)
    account.deposit(200)
    account.withdraw(500, 1234)
    account.withdraw(500, 4321)
    print(account.__pin)  # This will raise an error — private attribute


# 4. CLASS METHODS AND STATIC METHODS
# --------------------------------------------------------------------------------------------------------
    # - Class methods: operate on the class itself, not instances.
    # - Static methods: utility functions related to the class but don’t need access to instance/class data.

    class Person:
        population = 0  # Class attribute (shared by all instances)

        def __init__(self, name):
            self.name = name
            Person.population += 1

        @classmethod
        def get_population(cls):
            # Works with class itself
            return cls.population

        @staticmethod
        def greet():
            # Does not access class or instance attributes
            print("Hello! This is a static method.")

    p1 = Person("Jose")
    p2 = Person("Aitana")
    print("Population:", Person.get_population())
    Person.greet()


# 5. SPECIAL (MAGIC) METHODS
# --------------------------------------------------------------------------------------------------------
    # Magic methods start and end with double underscores (__)
    # They customize object behavior (printing, comparison, addition, etc.)

    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            # Called when using print()
            return f"Vector({self.x}, {self.y})"

        def __add__(self, other):
            # Called when using +
            return Vector(self.x + other.x, self.y + other.y)

        def __eq__(self, other):
            # Called when using ==
            return self.x == other.x and self.y == other.y

    v1 = Vector(2, 3)
    v2 = Vector(4, 1)
    v3 = v1 + v2
    print(v3)                # Uses __str__
    print("v1 == v2:", v1 == v2)