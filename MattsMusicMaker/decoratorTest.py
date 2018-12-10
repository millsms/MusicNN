
#Testing out decorators
def cough_dec(func):

    def func_wrapper():
        #code before function
        print("cough")
        func()
        #code after function
        print("weirdo")

    return func_wrapper()

@cough_dec
def question():
    print("Who are you")

question()
