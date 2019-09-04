import re

def convert_to_snake_case(input):
    if type(input) == list:
        return [convert_to_snake_case(elem) for elem in input]
    elif type(input) == dict:
        return_solution = {}
        for key in input.keys():
            if '_' in key:
                return_solution[key] = input[key]
            # Kebab case
            elif '-' in key:
                return_solution[key.replace('-', '_')] = input[key]
            # Camel case
            else:
                new_key = re.sub('([A-Z]|[0-9]+)', '_\\1', key).lower()
                if new_key[0] == '_':
                    new_key = new_key[1:]
                return_solution[new_key] = input[key]
        for key, value in return_solution.items():
                print("Recursing here")
                return_solution[key] = convert_to_snake_case(value)          
        return return_solution
    return input