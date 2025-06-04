import requests
from commands import *
from speechengine import *
from pprint import pprint
from llm import generate_response


if __name__ == '__main__':
    greet_user()
    boolean = True
    while boolean:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'open discord' in query:
            open_discord()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif "send an email" in query:
            speak("To what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif "trending movies" in query:
            movies = get_trending_movies()
            speak(f"Some of the trending movies are: {movies}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*movies, sep='\n')

        elif 'news' in query:
            speak("I'm reading out the latest news headlines, sir")
            headlines = get_latest_news()
            speak(headlines)
            speak("For your convenience, I am printing it on the screen sir.")
            print(*headlines, sep='\n')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

        elif 'goodbye' in query:
            speak(f"Thank you for using me,Have a good day")
            boolean=False

        elif 'trivia' in query:
            query=requests.get("https://opentdb.com/api.php?amount=1").json();
            speak(query['results'][0]['question'])
            speak(f"The options are : {query['results'][0]['correct_answer']} , {query['results'][0]['incorrect_answers'][0]} ,{query['results'][0]['incorrect_answers'][1]} ,{query['results'][0]['incorrect_answers'][2]}")
            answer = take_user_input().lower()
            if query['results'][0]['correct_answer'] in answer:
                speak("Your answer is correct , Congratulations")
            else:
                speak(f"Your answer is wrong , the correct answer is {query['results'][0]['correct_answer']}, Better luck next time")

        elif 'repeat' in query:
            speak("Alright i shall repeat what you say ,make sure to say stop to stop me from repeating")
            while(True):
                query = take_user_input().lower()
                if 'stop' in query:
                    break
                speak(query)

        else:
            response = generate_response(query)
            speak(response)

            
