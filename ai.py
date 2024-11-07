import webbrowser
import os

print("AI: Hello! I'm your simple AI chatbot.")
print("AI:Chosse any of them")
print("1. Open Google")
print("2. Open YouTube")
print("3. Open Codingal")
print("4. Open Visual studio code")
print("5. Open Wekipedia")
print("6. Open ChatGpt")
print("7. Open Stack Overflow")
print("8. Open fiverr")

while True:
    user_input = input("You: ").lower()

    # Exit condition
    if user_input == 'exit':
        print("AI: Goodbye! Have a nice day!")
        break

    # Open Google
    elif user_input == "1":
        print("AI: Opening Google for you...")
        webbrowser.open("https://www.google.com")

    # Open Visual Studio Code
    elif user_input == "4":
        print("AI: Opening Visual Studio Code...")
        os.system("code")  
    # Open Codingal
    elif user_input == "3":
        print("AI: Opening Codingal...")
        os.system("start https://www.codingal.com/bn-BD/student/dashboard/")
    # Open YouTube
    elif user_input == "2":
        print("AI: Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
    # Open Wekipide
    elif user_input == "5":
        print("AI: Opening Wikipedia...")
        webbrowser.open("https://www.wikipedia.org")
    # Open ChatGpt
    elif user_input == "6":
        print("AI: Opening ChatGpt...")
        webbrowser.open("https://chat.openai.com")
    # Open Stack Overflow
    elif user_input == "7":
        print("AI: Opening Stack Overflow...")
        webbrowser.open("https://stackoverflow.com")
    # Open Fiver
    elif user_input =="8":
        print("AI:  Opening Fiver...")
        webbrowser.open("https://www.fiverr.com/")
    # Additional simple responses
    elif "hello" in user_input:
        print("AI: Hi there! How can I help you today?")
    elif "how are you" in user_input:
        print("AI: I'm just a program, but thanks for asking! How about you?")
    else:
        print("AI: Sorry, I didn’t understand that. Could you ask something else?")
