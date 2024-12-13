#Zachary Shippey
#Solo Project
#CIS 314
#Morse Code Translator/ Geography Quiz 

import tkinter as tk
from tkinter import messagebox

# Morse Code Dictionary to convert between Morse and English
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

# Function to convert English text to Morse code
def english_to_morse(message):
    morse_message = ''
    for letter in message.upper():  # Loop through each letter in the message
        if letter in MORSE_CODE_DICT:  # Check if the letter exists in Morse dictionary
            morse_message += MORSE_CODE_DICT[letter] + ' '  # Add the Morse code for the letter
        elif letter == ' ':  # If it's a space, just add a space in the Morse message
            morse_message += ' '
    return morse_message  # Return the final Morse code

# Function to convert Morse code to English text
def morse_to_english(morse_code):
    morse_code += ' '  # Add a space at the end to make sure the last Morse code is processed
    decipher = ''  # To accumulate the decoded message
    citext = ''  # Temporarily store Morse code for a single character
    for letter in morse_code:
        if letter != ' ':  # If the letter isn't a space, add it to the character's Morse code
            citext += letter
        else:
            if citext:  # If we have Morse code for a character, decode it
                if citext in MORSE_CODE_DICT.values():
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]  # Decode it
                citext = ''  # Reset citext for the next character
            else:  # If we encounter a space, it's a space between words
                decipher += ' '
    return decipher  # Return the decoded English message

# Function to check if the user's answer matches the correct answer
def check_answer(question, correct_answer, answer):
    try:
        if '.' in answer or '-' in answer:  # If answer is in Morse code, decode it
            decoded_answer = morse_to_english(answer.strip())  # Decode Morse to English
        else:
            decoded_answer = answer.strip().lower()  # For English input, just strip and lower case it
        return decoded_answer == correct_answer.lower()  # Check if the answers match
    except ValueError:
        return False  # If an invalid Morse code is entered, return False

# Main class to handle the quiz GUI logic
class GeographyQuizApp:
    def __init__(self, root):
        self.root = root  # Set the root window
        self.root.title("Geography Quiz")  # Set the title of the window

        self.root.geometry("500x500")  # Set the window size

        # Initialize variables
        self.score = 0  # Initialize score to 0
        self.current_question = 0  # Start with the first question
        self.mode = None  # Mode (English or Morse) will be set later

        # Questions and answers for the quiz
        self.questions = [
            ("What is the capital of France?", "Paris"),
            ("Which continent is Egypt located in?", "Africa"),
            ("Which ocean is the largest?", "Pacific"),
            ("Which country is the Great Barrier Reef located in?", "Australia"),
            ("What is the longest river in the world?", "Nile"),
            ("What is the smallest country in the world?", "Vatican City"),
            ("Which country is home to the city of Machu Picchu?", "Peru"),
            ("Which country has the most population?", "China"),
            ("What is the highest mountain in the world?", "Mount Everest"),
            ("Which country is known as the Land of the Rising Sun?", "Japan")
        ]

        # Start the quiz interface with Yes/No for starting
        self.start_quiz()  # Ask if the user wants to start the quiz

    # Function to ask if the user wants to take the quiz
    def start_quiz(self):
        self.question_label = tk.Label(self.root, text="Would you like to take the Geography quiz?", font=("Helvetica", 14))
        self.question_label.pack(pady=20)  # Display the question

        # Yes/No buttons for quiz initiation
        self.yes_button = tk.Button(self.root, text="Yes", command=self.prompt_quiz, font=("Helvetica", 12))
        self.no_button = tk.Button(self.root, text="No", command=self.quit_quiz, font=("Helvetica", 12))
        self.yes_button.pack(pady=10)  # Pack Yes button
        self.no_button.pack(pady=10)  # Pack No button

    # Proceed to the quiz question after user chooses "Yes"
    def prompt_quiz(self):
        self.yes_button.pack_forget()  # Hide Yes button
        self.no_button.pack_forget()  # Hide No button

        self.question_label.config(text="Would you like to answer in Morse or English?")  # Change the question text

        # Buttons for mode selection (Morse or English)
        self.morse_button = tk.Button(self.root, text="Morse Code", command=self.select_morse, font=("Helvetica", 12))
        self.english_button = tk.Button(self.root, text="English", command=self.select_english, font=("Helvetica", 12))
        self.morse_button.pack(pady=10)  # Pack Morse Code button
        self.english_button.pack(pady=10)  # Pack English button

    # Exit the quiz
    def quit_quiz(self):
        self.root.quit()  # Close the window

    # Set mode to Morse and start the quiz
    def select_morse(self):
        self.mode = 'morse'  # Set mode to Morse
        self.show_question_page()  # Show the question page

    # Set mode to English and start the quiz
    def select_english(self):
        self.mode = 'english'  # Set mode to English
        self.show_question_page()  # Show the question page

    # Show the first question after mode selection
    def show_question_page(self):
        self.morse_button.pack_forget()  # Hide Morse button
        self.english_button.pack_forget()  # Hide English button

        self.display_question()  # Display the first question

    # Display the current question and input field
    def display_question(self):
        question, _ = self.questions[self.current_question]  # Get the current question
        self.question_label = tk.Label(self.root, text=question, font=("Helvetica", 14))  # Show question
        self.question_label.pack(pady=20)

        self.answer_label = tk.Label(self.root, text="Your answer:", font=("Helvetica", 12))  # Label for answer input
        self.answer_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.root, font=("Helvetica", 12))  # Entry box for the answer
        self.answer_entry.pack(pady=10)

        self.answer_button = tk.Button(self.root, text="Submit Answer", command=self.submit_answer, font=("Helvetica", 12))  # Submit button
        self.answer_button.pack(pady=10)

    # Submit the answer and check correctness
    def submit_answer(self):
        answer = self.answer_entry.get()  # Get the entered answer
        correct_answer = self.questions[self.current_question][1]  # Get the correct answer

        if check_answer(self.questions[self.current_question][0], correct_answer, answer):  # Check if the answer is correct
            self.score += 1  # Increment score for correct answer
            messagebox.showinfo("Correct!", "Your answer is correct!")  # Show info box for correct answer
        else:
            messagebox.showinfo("Incorrect", f"Your answer is incorrect! The correct answer is {correct_answer}.")  # Show info box for incorrect answer
        
        self.answer_entry.delete(0, tk.END)  # Clear the input box
        
        # Translate the answer to the opposite format (Morse to English or English to Morse)
        if self.mode == 'morse':
            translated_answer = morse_to_english(answer)  # Convert Morse to English
            self.translation_label = tk.Label(self.root, text=f"Your answer in English: {translated_answer}", font=("Helvetica", 12))
            self.translation_label.pack(pady=10)  # Show translated answer
        else:
            translated_answer = english_to_morse(answer)  # Convert English to Morse
            self.translation_label = tk.Label(self.root, text=f"Your answer in Morse: {translated_answer}", font=("Helvetica", 12))
            self.translation_label.pack(pady=10)  # Show translated answer
        
        # Proceed to the next question after a short delay
        self.root.after(2000, self.next_question)

    # Go to the next question
    def next_question(self):
        self.current_question += 1  # Move to the next question
        if self.current_question < len(self.questions):  # If there are more questions, show the next one
            self.clear_page()
            self.display_question()
        else:  # If all questions are answered, end the quiz
            self.end_quiz()

    # End the quiz and show the final score
    def end_quiz(self):
        messagebox.showinfo("Quiz Over", f"You scored {self.score} out of {len(self.questions)}!")  # Show score
        self.root.quit()  # Close the window

    # Clear the page of previous widgets before showing the next question
    def clear_page(self):
        for widget in self.root.winfo_children():  # Loop through all widgets on the window
            widget.destroy()  # Destroy them to prepare for the next question

# Main function to run the GUI
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = GeographyQuizApp(root)  # Initialize the app with the root window
    root.mainloop()  # Run the app