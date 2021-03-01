import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# -------------------------------------------------------------------------

# ******** Function Solution Provided By the Professor ********

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:
#     #TODO-3: What happens if the user enters a number/symbol/space?
#     #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#     #e.g. start_text = "meet me at 3"
#     #end_text = "•••• •• •• 3"
#     if char in alphabet:
#       position = alphabet.index(char)
#       new_position = position + shift_amount
#       end_text += alphabet[new_position]
#     else:
#       end_text += char
#   print(f"Here's the {cipher_direction}d result: {end_text}")

# -------------------------------------------------------------------------

def caesar(cipher_text, shift_amount, user_direction):
  plain_text = ""
  for letter in cipher_text:
    if letter not in alphabet:       # Checking if letter is out of alphabet list.
      plain_text += letter           # If Yes, appending it to the plain text. 
    else:
      position = alphabet.index(letter)
      if user_direction == 'encode':
        new_position = position + shift_amount
      elif user_direction == 'decode':
        new_position = position - shift_amount
      plain_text += alphabet[new_position]
  print(f"The {user_direction}d text is {plain_text}")
  

#For restarting the cipher program

restart_code = True

while restart_code:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

#What if the user enters a shift that is greater than the number of letters in the alphabet?
#Below line helps the code to run even if the user enters a shift number greater than 26. 

  shift = shift % 26   #Store the remainder as a shift value in the function

  caesar(cipher_text = text, shift_amount = shift, user_direction = direction)

# Asking user if he wants to rerun the code or not.
  want_rerun = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if want_rerun != "yes":  # If want_return value is anything except yes, code will stop.
    restart_code = False