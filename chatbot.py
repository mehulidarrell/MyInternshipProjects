import tkinter as tk
from tkinter import scrolledtext, Entry, Button, END
import random

class SimpleChatbotGUI:
    def __init__(self):
        # Initialize Tkinter window
        self.root = tk.Tk()
        self.root.title("Bee")

        # Create scrolled text widget for displaying the conversation
        self.chat_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=15)
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Create entry widget for user input
        self.user_input_entry = Entry(self.root, width=30)
        self.user_input_entry.grid(row=1, column=0, padx=10, pady=10)

        # Create 'Send' button to send user input
        self.send_button = Button(self.root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        # Create 'Exit' button to close the application
        self.exit_button = Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Lists for greetings, questions, and answers
        self.greetings = ["hi", "hey", "hello"]
        self.questions = ["how are you?", "what's up?"]
        self.answers = ["I'm good 😊", "I'm fine 🙂", "I'm ill 🤒", "I'm happy 😌", "I'm great 😎"]
        self.identity_questions = ["what is your name?", "who are you?", "your identity?"]
        self.identity_answers=["My name is Bee.", "I'm Bee,", "My name is Bee. I'm your virtual assistant."]
        
    def send_message(self):
        # Get user input from the entry widget
        user_input = self.user_input_entry.get()

        # Display user input in the chat display
        self.display_message("User", user_input)

        # Process user input and get chatbot's response
        bot_response = self.process_user_input(user_input)

        # Display chatbot's response in the chat display
        self.display_message("Bot", bot_response)

        # Clear the user input entry
        self.user_input_entry.delete(0, END)
        
    def process_user_input(self, user_input):
    # Check for greetings, questions, and identity-related questions, provide answers accordingly
        if any(word in user_input.lower() for word in self.greetings):
            return self.list_Ai()
        elif any(word in user_input.lower() for word in self.questions):
            return self.list_Bi() + " BTW how about you?"
        elif any(word in user_input.lower() for word in self.identity_questions):
            return self.list_Ci()
        else:
            return self.list_Q(user_input)



    def list_Ai(self):
        # Generate response for greetings
        X1 = random.choice(self.greetings).capitalize()
        X2 = random.choice(self.questions)
        return f"{X1}! {X2}"

    def list_Bi(self):
        # Generate response for questions
        X3 = random.choice(self.answers)
        return f"{X3}"

    def list_Ci(self):
        # Generate response for identity-related questions
        X4 = random.choice(self.identity_answers)
        return f"{X4} Nice to meet you."

    def list_Q(self, ext):
        # Generate response for other user queries
        return f"Sorry i don't know about what you are saying"

    def display_message(self, sender, message):
        # Display the message in the chat display
        self.chat_display.insert(tk.END, f"{sender}: {message}\n")
        self.chat_display.yview(tk.END)

    def run(self):
        # Run the Tkinter main loop
        self.root.mainloop()

if __name__ == "__main__":
    chatbot_app = SimpleChatbotGUI()
    chatbot_app.run()
