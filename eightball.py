from random import randrange

class Eightball(object):
    def __init__(self):
        self.name = "Eightball"
        self.initial_state = "1"
        self.answers = {
            "1":"Yes.",
            "2":"No.",
            "3":"It Will Pass.",
            "4":"Count On It.",
            "5":"Maybe.",
            "6":"You're Hot.",
            "7":"Ask Again.",
            "8":"No Doubt.",
            "9":"Absolutely.",
            "10":"Go For It.",
            "11":"Wait For It.",
            "12":"Not Now.",
            "13":"Cannot Tell Now.",
            "14":"Very Likely.",
            "15":"It Is Ok.",
            "16":"Don't Count On It.",
            "17":"Lay It Down! Lay It Down!",
            "18":"Don't Ask Me. I'm Just A Ball!",
            "19":"Highly Unlikely.",
            "20":"Eh. Sure Why Not?"
        }
    def roll(self):
        roll = randrange(1,22)
        ans = "[BLANK]"
        for answer in self.answers:
            if str(roll) == answer:
                ans = self.answers[answer]
        return ans