text = input("Enter your text: ")
length = len(text)
if length % 2 != 0:
  text_index = length//2
  print(text[text_index])
elif length % 2 == 0:
  text_index = length//2 - 1
  print(text[text_index: text_index +2])