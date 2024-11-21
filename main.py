import speech_recognition as sr  # Updated import for clarity
import pyttsx3
import webbrowser


# Initialize recognizer
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
ttsx = pyttsx3.init()

# Function to speak text
def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

# Main function
if __name__ == "__main__":
    speak("Initializing Henry...")  # Welcome message
    while True:  # Keep listening indefinitely
        try:
            # Get audio input from the microphone
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)  # Adjusts to ambient noise
                audio = recognizer.listen(source)  # Listen to audio from the microphone

            # Try recognizing the speech using Google Web Speech API
            command = recognizer.recognize_google(audio)  # Google recognition
            print(f"Command received: {command}")

            # Check if the command matches some predefined instructions
            command = command.lower()  # Convert to lowercase for easier matching

            if 'open youtube' in command:
                speak("Opening YouTube...")
                webbrowser.open('https://www.youtube.com')  # Opens YouTube
            elif 'open google' in command:
                speak("Opening Google...")
                webbrowser.open('https://www.google.com')  # Opens Google
            elif 'search' in command:
                search_query = command.replace("search", "")  # Remove 'search' from command
                speak(f"Searching for {search_query}...")
                webbrowser.open(f'https://www.google.com/search?q={search_query}')  # Google search
            elif 'stop' in command or 'exit' in command:
                speak("Goodbye!")
                break  # Exit the loop and stop the assistant
            else:
                speak("Sorry, I didn't catch that.")  # In case the command is not recognized
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
