from functools import wraps

from errors import *


def error_handler(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        try:
            function(*args, ** kwargs)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print('Looks like you forgot to enter some data')
        except IndexError as e:
            print(e)
        except TypeError:
            print('Wow. Please change entered data and try again')
        except EmptySearchString as e:
            print(e)
        except ContactExists as e:
            print(e)
        except WrongBirthday as e:
            print(e)
        except WrongEmail as e:
            print(e)
        except WrongPhone as e:
            print(e)
        except Exception:
            print('Something bad has happened. Try anothing else :(')

    return wrapper
