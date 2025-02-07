number_to_word = ("Zero", "One", "Two", "Three", "Four", 
                  "Five", "Six", "Seven", "Eight", "Nine")

num = input("Enter a number: ")
num_words = tuple(number_to_word[int(digit)] for digit in num)

print("Number in words:", " ".join(num_words))
