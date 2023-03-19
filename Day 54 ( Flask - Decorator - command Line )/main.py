"""Terminal commands
pwd                                Where I am ( in linux or PowerShell - it doesn't work for CMD and need CD instead )
ls                                 list everything in the current directory
cd                                 to change directory
mkdir                              make the folder
touch or ni                        making a file
cd ..                              going 1 step back to parent folder
rm -rf (folder) or rmdir           delete a folder
ls - a                             list hidden files as well
start or open file.txt             open a file
git init                           initialize empty git repository
git status                         statis of files in git if there are on watch list
git add file.txt                   add file to repository
git commit -m "Initial Commit"     commit the files in repository -m gives it a message
git log                            history of commits
git diff file                      difference between current and previous version of file
git checkout file                  restore the previous version of the file
HuB connect
git remote add origin https...     add remote address for your repository
git push -u origin master          connect your local and remote repository and upload it to remote one



"""


# """NESTED FUNC, Decorators
## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(add, 2, 3)
print(result)


##Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()


outer_function()


## Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function


inner_function = outer_function()
inner_function()
## Simple Python Decorator Functions
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


# With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")


# Without the @ syntactic sugar
def say_greeting():
    print("How are you?")


decorated_function = delay_decorator(say_greeting)
decorated_function()
