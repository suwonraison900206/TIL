import datetime



class DatetimeDecorator:

        def __init__(self, f):

                self.func = f



        def __call__(self, *args, **kwargs):

                print(datetime.datetime.now())

                self.func(*args, **kwargs)

                print(datetime.datetime.now())



class MainClass:

        @DatetimeDecorator

        def main_function_1():

                print("MAIN FUNCTION 1 START")



        @DatetimeDecorator

        def main_function_2():

                print("MAIN FUNCTION 2 START")



        @DatetimeDecorator

        def main_function_3():

                print("MAIN FUNCTION 3 START")





my = MainClass()

my.main_function_1()

my.main_function_2()

my.main_function_3()
