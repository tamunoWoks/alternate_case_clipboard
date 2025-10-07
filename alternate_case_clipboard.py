import pyperclip

text = pyperclip.paste()       # Get text from clipboard
alt_text = ''                  # Store alternating text
make_uppercase = False         # Toggle for switching case

for character in text:
    if character.isalpha():    # Only alternate letters
        if make_uppercase:
            alt_text += character.upper()
        else:
            alt_text += character.lower()
        make_uppercase = not make_uppercase
    else:
        alt_text += character  # Leave punctuation/spaces unchanged

pyperclip.copy(alt_text)       # Copy new text to clipboard
print(alt_text)                # Show it on screen
