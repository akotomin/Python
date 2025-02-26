# эти строчки не менять
stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]

# здесь продолжайте программу
import re


class StringText:
    def __init__(self, words):
        self.words = words

    def __len__(self):
        return len(self.words)

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __str__(self):
        return " ".join(self.words)


lst_text = [StringText(re.findall(r'\b\w+\b', line)) for line in stich]
lst_text_sorted = sorted(lst_text, reverse=True, key=len)
lst_text_sorted = [str(st) for st in lst_text_sorted]