from similarity_calculator import find_most_similar
from data_loader import data

class Bot:

    def __init__(self):
        self.event_stack = []
        self.settings = {
            "min_score": 0.2,
            "help_email": "fakeEmail@notArealEmail.com",
            "faq_page": "www.NotActuallyAnFAQ.com"
        }

        print ("Ask a query:")
        while(True):
            self.allow_question()

    def allow_question(self):
        # Check for event stack
        potential_event = None
        if(len(self.event_stack)):
            potential_event = self.event_stack.pop()
        if potential_event:
            text = input("Response: ")
            potential_event.handle_response(text, self)
        else:
            text = input("query: ")
            answer = self.pre_built_responses_or_none(text)
            if not answer:
                answer = find_most_similar(text)
                self.answer_question(answer, text)

    def answer_question(self, answer, text):
        if answer['score'] > self.settings['min_score']:
            # set off event asking if the response question is what they were looking for
            print ("\nBest-fit question: %s (Score: %s)\nreply: %s\n" % (answer['query'],
                                                                          answer['score'],
                                                                          answer['reply']))
        else:
            print ("Woops! I'm having trouble finding the answer to your question. " \
                  "Would you like to see the list of questions that I am able to answer?\n")
            # set off event for data dump
            self.event_stack.append(Event("data_dump", text))

    def pre_built_responses_or_none(self, text):
        # only return answer if exact match is found
        pre_built = [
            {
                "query": "Who made you?",
                "reply": "I was created by TS-North.\n"
            },
            {
                "query": "When were you born?",
                "reply": "I first opened my eyes in alpha stage February 9th, 2018.\n"
            },
            {
                "query": "What is your purpose?",
                "reply": "I assist user experience by providing an interactive FAQ chat.\n"
            },
            {
                "query": "Thanks",
                "reply": "Glad I could help!\n"
            },
            {
                "query": "Thank you",
                "reply": "Glad I could help!\n"
            }
        ]
        for each_question in pre_built:
            if each_question['query'].lower() in text.lower():
                print (each_question['reply'])
                return each_question


    def dump_data(self):
        question_stack = []
        for each_item in data:
            question_stack.append(data[each_item]['query'])
        return question_stack


class Event:

    def __init__(self, kind, text):
        self.kind = kind
        self.CONFIRMATIONS = ["yes", "sure", "okay", "that would be nice", "yep"]
        self.NEGATIONS = ["no", "don't", "dont", "nope"]
        self.original_text = text

    def handle_response(self, text, bot):
        if self.kind == "data_dump":
            self.data_dump(text, bot)

    def data_dump(self, text, bot):
        for each_confirmation in self.CONFIRMATIONS:
            for each_word in text.split(" "):
                if each_confirmation.lower() == each_word.lower():
                    data = bot.dump_data()
                    data = ["-" + s for s in data]
                    print ("%s%s%s" % ("\n", "\n".join(data), "\n"))
                    return 0
        for each_negation in self.NEGATIONS:
            for each_word in text.split(" "):
                if each_negation.lower() == each_word.lower():
                    print ("Feel free to ask another question or send an email to %s.\n" % bot.settings['help_email'])
                    bot.allow_question()
                    return 0
        # base case, no confirmation or negation found
        print ("I'm having trouble understanding what you are saying. At the time, my ability is quite limited, " \
              "please refer to %s or email %s if I was not able to answer your question. " \
              "For convenience, a google link has been generated below: \n%s\n" % (bot.settings['faq_page'],
                                                                                 bot.settings['help_email'],
                                                                                 "https://www.google.com/search?q=%s" %
                                                                                 ("+".join(self.original_text.split(" ")))))
        return 0


Bot()
