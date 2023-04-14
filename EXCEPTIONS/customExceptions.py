class MyException(Exception):
    pass


class NoExistError(MyException):
    
    def __init__(self, catch, message="does not exist"):
        self.catch = catch
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.catch} -> {self.message}'


class InputError(MyException):
    
    def __init__(self, message="The input is empty, try again!"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class AlreadyExistError(MyException):
        
    def __init__(self, catch, message="already exists"):
        self.catch = catch
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.catch} -> {self.message}'
    
