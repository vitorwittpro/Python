glossary = {
    'string': 'A String is a bunch of characters. Anything between two quotes is considered a string in python.',
    'integer': 'Integers are numbers with no decimal point.',
    'float': 'Floats are numbers with a decimal point.',
    'list': 'A collection of items in a particular order.', 
}

for term, meaning in glossary.items():
    print(f"{term.title()}\n  -{meaning.title()}")