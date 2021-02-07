#Daniel Brestoiu
#Symbolic Expression Calculator

import re
import sys
from sympy import simplify

FUNCTION_DICT = {"add": "+", "multiply": "*", "subtract": "-", "divide": "/"}
#REGEX_PATTERN = "(\([0-9A-Za-z]+\ [0-9]+\ [0-9]+\))"
REGEX_PATTERN = "(\([0-9A-Za-z]+\ [0-9\ ]+\ +[0-9]+\))"


def parse_input():
    args = sys.argv
    return args[1]

def is_int(string:str) -> bool:
    """"is_int attempts to convert a string to an int and reports its results."""
    try:
        int(string)
        return True
    except:
        return False


def regex_splitter(input_string: str) -> str:
    """ Regex Splitter attempts to split the input string into useful components based on 
    the regex that has been defined.
    Returns input as grouped per defined regex.
    """
    #grouping_list: list = re.compile(REGEX_PATTERN).split(input_string)
    compiled_regex = re.compile(REGEX_PATTERN)
    mo = compiled_regex.findall(input_string)
    
    #print("Current found matches are:" + str(mo))
    
    result = evaluator_indefinite(mo)
    
    #print("Dictionary of evaluations" + str(result))
    
    new_string = input_string

    for match in mo:
        new_string = new_string.replace(str(match), str(result[match]))
        #print("Current string modified with new value: " + new_string)

    return new_string

def evaluator_indefinite(match_group: list) -> dict:

    return_dict = {}
    
    for match in match_group:
        #print("Evaluator match is: "+match)

        stripped_match = match[1:-1]
        split_match = stripped_match.split()

        #print("Print evaluator split match is" + str(split_match))

        operator = FUNCTION_DICT[split_match[0]]
        current_result = split_match[1]
        for x in range(len(split_match)-2):
            new_num = split_match[x+2]
            current_result = evaluator(operator, current_result, new_num)
        
        return_dict[match] = current_result

    return return_dict



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
        #he is int, give back plz.
    else:
        try:
            modified_input: str = input_string.strip()

            evaluatable_pairs: str = regex_splitter(modified_input)

            while not (is_int(evaluatable_pairs)):
                evaluatable_pairs = regex_splitter(evaluatable_pairs)

            return (evaluatable_pairs)

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
    
    assert input_parser("(add (multiply 4 5) (multiply 10 10) (add 1 2 3 4 5 6 7 (add 4 4) 9) (multiply 4 5))") == '185'

    assert input_parser('(subtract 2 1)') == '1'
    assert input_parser("(divide 55 5)") == '11'

def main(input: str) -> None:
    """ Main function"""
    print(input_parser(input))


if __name__ == "__main__":
    #tests()
    main(parse_input())