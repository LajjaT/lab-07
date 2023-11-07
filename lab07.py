#Part 1
import re

def validate_variable(value):

    shouldMatch = r'[a-zA-Z][a-zA-Z0-9_]*$'

    if re.match(shouldMatch, value):
        return True
    else:
        return False

#Part 2
def validate_domain(value):
    shouldMatchThis = r'[a-z][a-z0-9_]*(\.[a-z][a-z0-9_]*)*\.(com|ca|org)$'
    
    if re.match(shouldMatchThis, value):
        return True
    else:
        return False

#Part 3
def validate_phone(value):
    shouldMatchThisExpression = r'^\d{3}-\d{3}-\d{4}$|\d{3}-\d{4}$|^\(\d{3}\)\d{3}-\d{4}$'
    
    if re.match(shouldMatchThisExpression, value):
        return True
    else:
        return False