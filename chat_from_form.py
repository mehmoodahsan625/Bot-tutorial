import random
from flask import Flask, request,render_template, redirect

app = Flask(__name__)

print("Bot: what is your name?")
# user_name = input()

user_name = "ahsan"

name = "t_bot"
weather = "cloudy"
mood = "happy"

# bot_template = name + " : {0}"
# user_template = user_name + " : {0}"

responses = {
    "what's your name?":[
    "they call me {0}".format(name),
    "i usually go by {0}".format(name),
    "my name is {0}".format(name)],
    "what's today's weather?":[
    "the weather is {0}".format(weather),
    "it's {0} today".format(weather),
    "let me check, it's {0} today".format(weather) ],
    "are you a robot?": [ 
    "What do you think?", 
    "Maybe yes, maybe no!", 
    "Yes, I am a robot with human feelings.", ],
    "how are you?": [ 
    "I am feeling {0}".format(mood), 
    "{0}! How about you?".format(mood), 
    "I am {0}! How about yourself?".format(mood), ],
    "": [ 
    "how are you?", 
    "What do you mean by saying nothing?", 
    "Sometimes saying nothing tells a lot", ],
    "default": [
    "this is a default message"] }

def respond(message):
    if message in responses: 
        bot_message = random.choice(responses[message])
    else: 
        bot_message = random.choice(responses["default"])
    return bot_message

def related(x_text): 
    if "name" in x_text: 
        y_text = "what's your name?"
    elif "weather" in x_text: 
        y_text = "what's today's weather?"
    elif "robot" in x_text: 
        y_text = "are you a robot?"
    elif "how are" in x_text: 
        y_text = "how are you?"
    else: 
        y_text = ""
    return y_text

def send_message(message): 
    # print(user_template.format(message)) 
    response = respond(message) 
    return response, message
    # print(bot_template.format(response))

@app.route("/", methods=["GET", "POST"])
@app.route("/main", methods=["GET", "POST"])
def main():
    if request.method == "POST":
         
        my_input = request.form["inputdata"]
        if my_input == "exit" or my_input == "stop":
            print("chat done")
            return  "success!!"
        else:
            # my_input = input() 
            my_input = my_input.lower() 
            related_text = related(my_input) 
            response = send_message(related_text) 
            print(response[0])
            return render_template("chat_from_form.html", data = response[0], message = response[1])
    else:
        return render_template("chat_from_form.html", data = "")

if __name__ == "__main__":
    app.run(debug=True)