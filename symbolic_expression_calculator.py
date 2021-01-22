
# Daniel Brestoiu
# Symbolic Expression Calculator


import re
from sympy import simplify

FUNCTION_DICT = {"add": "+", "multiply": "*"}
REGEX_PATTERN = "(\([0-9A-Za-z]+\ [0-9A-Za-z]+\ [0-9A-Za-z]+\))"
# NOTE: Regex
# Match group starting with (, followed by char or num indefinitely, followed by space, 
#                              followed by char or num indefinitely, followed by space,
#                              followed by char or num indefinitely, followed by )
# I use this to identify the portions of input that are currently evaluatable.

# NOTE: Extensibility
# All other math functions could be implemented trivially by adding to FUNCTION_DICT
# Arbitrary amount of arguments would require changing regex and evaluator() parameters. 


def is_int(string:str) -> bool:
    """"is_int attempts to convert a string to an int and reports its results."""
    try:
        int(string)
        return True
    except:
        return False


def regex_splitter(input_string: str) -> list:
    """ Regex Splitter attempts to split the input string into useful components based on 
    the regex that has been defined.
    Returns input as grouped per defined regex.
    """
    grouping_list: list = re.compile(REGEX_PATTERN).split(input_string)
    return grouping_list


def regex_component_evaluator(strings_list: list) -> str:
    """ Takes in a list containing strings, where some strings are valid (func num num).
    Returns input list with all (func num num) evaluated recomposed as a joined string."""

    full_string: str = ""
    compiled_regex = re.compile(REGEX_PATTERN)

    for string in strings_list:
        if compiled_regex.match(string):
            try:    
                #By matching pattern I know it is of the form (func num num) according to input specifications
                
                evaluatable_string: str = string[1:-1].split(" ")
                #This is to strip the () 
                #print(evaluatable_string)
                
                evaluated_expression: str = evaluator(FUNCTION_DICT[evaluatable_string[0]], evaluatable_string[1], evaluatable_string[2])
                full_string = full_string + evaluated_expression
            except:
                raise Exception("Invalid Input")
        else:
            #Not a string we're looking to evaluate.
            full_string = full_string + string

    return full_string


def evaluator(operator: str, value1: str, value2: str) -> str:
    """ 
    Evaluator takes a mathematical operator, value and value then applies the mathematical operation to the values.
    It returns the result of this operation.
    """

    evaluation_function: str = value1 + operator + value2
    #Because all three are strings, the + operator simply appends them together to be simplified. 

    result: str = str(simplify(evaluation_function))
    return result
    

def input_parser(input_string: str) -> str:
    """
    input_parser takes in a string input of the form (add ... ...) or (multiply ... ...)
    and returns the result of the calculation
    """ 
    if is_int(input_string):
        return input_string
        # he is int, give back plz.
    else:
        try:
            modified_input: str = input_string.strip()

            input_as_list: list = regex_splitter(modified_input)
            evaluated_input: str = regex_component_evaluator(input_as_list)

            return (input_parser(evaluated_input))

        except:
            raise Exception("Invalid Input")


def tests() -> None:
    """ Run test cases to verify functionality"""
    assert input_parser("123") == '123'
    assert input_parser("(add 12 12)") == '24'
    assert input_parser("(add 0 (add 3 4))") == '7'
    assert input_parser("(add 3 (add (add 3 3) 3))") == '12'
    assert input_parser("(multiply 3 (multiply (multiply 3 3) 3))") == '81'
    assert input_parser("(multiply 2 (multiply 3 4))") == '24'
    assert input_parser("(multiply 0 (multiply 3 4))") == '0'

    assert input_parser("(add 4 1)") == '5'
    assert input_parser("(multiply 4 1)") == '4'
    
    assert input_parser("(add 4 (add 1 8))") == '13'
    assert input_parser("(add (add 1 8) 4)") == '13'
    assert input_parser("(multiply (multiply 1 2) 12)") == '24'
    assert input_parser("(multiply 4 (multiply 8 12))") == '384'

    assert input_parser("(add (multiply 4 5) (multiply 10 10))") == '120'
    assert input_parser("(add (multiply (add 4 (add 3 (add 3 (add 3 (add 1 (multiply 4 5)))))) 5) (multiply 10 10))") == '270'
    

def main() -> None:
    """ Main function"""
    input_string = input()
    print(input_parser(input_string))


if __name__ == "__main__":
    #tests()
    main()