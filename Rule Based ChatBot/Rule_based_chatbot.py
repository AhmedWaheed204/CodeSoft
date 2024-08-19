import random
import re

class RuleBot:
    ## responses
    negative_res = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commends = ("quit", "pause", "exit", "goodbye", "bye", "later")

    random_question = (
        "why are you here?",
        "Are there many humans like you?",
        "what do you consume for sustenance?",
        "Is there Intelligent life on this planet?",
        "does Earth have a leader?",
    )

    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'about_intellipaat': r'.*\s*intellipaat.*',
        }

    def greet(self):
        self.name = input("what is your name?\n")
        will_help = input(f"Hi {self.name}, I am bot. Will you help me learn about your planet?\n")
        if will_help in self.negative_res:
            print("Have a nice Earth day!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commends:  # Corrected here
            if reply == command:
                print("Have a nice day!")
                return True
        return False

    def chat(self):
        reply = input(random.choice(self.random_question)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply)).lower()

    def match_reply(self, reply):
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.match(regex_pattern, reply)
            if found_match:
                if intent == 'describe_planet_intent':
                    return self.describe_planet_intent()
                elif intent == 'answer_why_intent':
                    return self.answer_why_intent()
                elif intent == 'about_intellipaat':
                    return self.about_intellipaat()
        return self.no_match_intent()

    def describe_planet_intent(self):
        responses = ("My planet is a utopia of diverse organisms.", "I heard the coffee is good.")
        return random.choice(responses)

    def answer_why_intent(self):
        responses = ("I come in peace.", "I am here to collect data on your planet and its inhabitants.", "I heard the coffee is good.")
        return random.choice(responses)

    def about_intellipaat(self):
        responses = ("Intellipaat is the world's largest professional educational company.", "Intellipaat will make you learn concepts like never before.", "Intellipaat is where your career and skills grow.")
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "Please tell me more.",
            "Tell me more!",
            "I see. Can you elaborate?",
            "Interesting. Can you tell me more?",
            "I see. How do you think?",
            "Why?",
            "How do you think I feel when you say that? Why?",
        )
        return random.choice(responses)

bot = RuleBot()
bot.greet()
