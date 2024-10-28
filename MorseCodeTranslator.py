#Zachary Shippey
#Solo Project
#CIS 314
#Morse Code Translator test

# Here is the Morse Code Dictionary. Stores the alphabet and morse counterparts
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
    '(': '-.--.', ')': '-.--.-'
}

# This is the function to translate Simple English to Morse code
def english_to_morse(message):
    morse_message = ''
    for letter in message.upper():
        if letter != ' ':
            morse_message += MORSE_CODE_DICT.get(letter, '') + ' '
        else:
            morse_message += ' '  # Applies the Space between the words
    return morse_message

# This is the function to translate Morse code to English
def morse_to_english(morse_code):
    morse_code += ' '  # Add extra space to ensure last code is processed
    decipher = '' #this variable accumulates the translated English from the morse
    citext = ''  #temporarily stores the morse for each character until space indicates end of character code
    for letter in morse_code:
        if letter != ' ':
            citext += letter  # Collect morse code for a single character
        else:
            if citext:  # If morse code collected, decode it
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
            else:
                decipher += ' '  # Add space between words
    return decipher

# Here we will test to see if the codes translate
message = "Maximus Decimus Meridius" #Main Character of Gladiator
morse_code = english_to_morse(message)
print("English to Morse: ", morse_code)

decoded_message = morse_to_english(morse_code)
print("Morse to English: ", decoded_message)




#Topics included in project consist of:
# The custom method that defines the morse code dictionary
# Data Structure which is the dictionary
#Looping and Sorting
#Variables and Usage

#Lessons/Difficulties:
#managing spaces between words and characters 
#Handeling characters not suported by the dictionary
#Easily read function names
#only allowing characters that are valid for translation
#The translation from morse back to english
# identify where one character ends and another begins


#Post project report
'''The goal was to be able to translate from english to morse and vice versa.
It was successful as I was able to get it to translate but I orignally wanted
to create a user input so that the user can type whatever they wanted and it would translate.
In that portion, I still need to figure out how to include a text prompt , but I was able to at least
translate the given message in the Code.
'''