class SomeClass:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}'

    def __add__(self, other):
        return self.age + other


def main():
    some_class = SomeClass('Denis', 24)
    print(some_class, some_class + 1)


if __name__ == '__main__':
    main()
