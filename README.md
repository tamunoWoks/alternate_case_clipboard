# Alternate Case Clipboard
Alternate Case Clipboard is a simple Python utility that takes the text currently on your clipboard, converts it to an *alternating uppercase and lowercase pattern*, and then automatically copies the result back to your clipboard, while preserving punctuation, spaces, and numbers.

For example: 
```txt
Input:   Python is awesome!
Output:  pYtHoN iS aWeSoMe!
```
### Features:
- Reads text directly from your clipboard
- Alternates case for letters only
- Keeps punctuation, numbers, and spaces unchanged
- Copies the transformed text back to your clipboard automatically
- Prints the result to your terminal

### How It Works:
1. The script fetches text from your system clipboard using the pyperclip module.
2. It iterates through each character in the text:
3. Letters alternate between lowercase and uppercase.
4. Non-letter characters (like punctuation, spaces, or numbers) remain unchanged.
5. The modified text is printed on screen and copied back to your clipboard for instant pasting.

#### Note:
For the boolean flag controlling whether the next letter should be uppercase or lowercase, the default value is `False`, meaning the first letter encountered will be lowercased. Change to `True` to start with uppercase.
