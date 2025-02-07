elements = (1, 3, 4, 5, 3, 2, 4, 4, 1)
repeated_items = {item for item in elements if elements.count(item) > 1}
print(f"Repeated items: {tuple(repeated_items)}")
