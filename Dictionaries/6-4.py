# Programming glossary with control loops.

glossary = {
    'variable':'A unique declared location that is used to store values.',
    'dictionary':'A list of key/value pairs. Use a the key to access the value'
    ' which can be of any type.',
    'loop':'A type of program flow control. Keeps executing as long as '
    'conditions permit.',
    'function':'An encapsulation of code that can take arguments that performs'
    ' a task and usually returns a value.',
    'integer':'Whole numbers. 2,147,483,647 max positive value. Can be negative'
    '.',
    'method':'This is a function that takes a class instance as the first '
    'parameter.',
    'set()':'A method that returns a collection of unique values.',
    'index':'A position in a list or array. Starts at 0.',
    'bug':'An unintended feature in a program. May prevent the program from '
    'executing, but will always produce unpredicted behavior.',
    'key-value pair':'In a dictionary content is stored in key-value pairs, '
    'separated by ":"',
    }

for term, entry in glossary.items():
    print(term.title() + ": " + entry + "\n")
