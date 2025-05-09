
# input = int(input("Ingresa un número entero: ")) Esta linea espera un valor entero, si se ingresa cualquier otro tipo, se genera un ValueError
# ValueError: invalid literal for int() with base 10: ''
print()
while True:
    try:
        valueA = int(input("Ingresa un numero entero A: "))
        print("Bien! 🤓")
        valueB = int(input("Ahora ingresa otro numero entero B: "))
        valueC = valueA/valueB
        print("El resultado de A/B es: " + str(valueC) + " 🤓")
        break
    except ValueError:
        print("Ups! ...Intenta de nuevo 😨")
        print()
    except ZeroDivisionError:
        print("No es posible dividir entre cero! 🤯")
        print()
    finally:
        print("Finalmente... 👀")
        print()

"""
AssertionError:	Raised when the assert statement fails.
AttributeError:	Raised on the attribute assignment or reference fails.
EOFError:	Raised when the input() function hits the end-of-file condition.
FloatingPointError:	Raised when a floating point operation fails.
GeneratorExit:	Raised when a generator's close() method is called.
ImportError:	Raised when the imported module is not found.
IndexError:	Raised when the index of a sequence is out of range.
KeyError:	Raised when a key is not found in a dictionary.
KeyboardInterrupt:	Raised when the user hits the interrupt key (Ctrl+c or delete).
MemoryError:	Raised when an operation runs out of memory.
NameError:	Raised when a variable is not found in the local or global scope.
NotImplementedError:	Raised by abstract methods.
OSError:	Raised when a system operation causes a system-related error.
OverflowError:	Raised when the result of an arithmetic operation is too large to be represented.
ReferenceError:	Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError:	Raised when an error does not fall under any other category.
StopIteration:	Raised by the next() function to indicate that there is no further item to be returned by the iterator.
SyntaxError:	Raised by the parser when a syntax error is encountered.
IndentationError:	Raised when there is an incorrect indentation.
TabError:	Raised when the indentation consists of inconsistent tabs and spaces.
SystemError:	Raised when the interpreter detects internal error.
SystemExit:	Raised by the sys.exit() function.
TypeError:	Raised when a function or operation is applied to an object of an incorrect type.
UnboundLocalError:	Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeError:	Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError:	Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError:	Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError:	Raised when a Unicode-related error occurs during translation.
ValueError:	Raised when a function gets an argument of correct type but improper value.
ZeroDivisionError:	Raised when the second operand of a division or module operation is zero.
"""

