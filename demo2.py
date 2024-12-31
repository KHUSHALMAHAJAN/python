value = 4

def switch_case_example(value):
    match value:
        case 1:
            print("Case 1: Value is 1")
        case 2:
            print("Case 2: Value is 2")
        case 3:
            print("Case 3: Value is 3")
        case _:
            print("Default case: Value not found")

# Example usage
value = 2
switch_case_example(value)
