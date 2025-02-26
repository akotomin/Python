class Morph:
    def __init__(self, *words):
        self.words = list(words)

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, other):
        if isinstance(other, str):
            return other.lower() in (word.lower() for word in self.words)
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __contains__(self, item):
        return self.__eq__(item)

dict_words = [
    Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'),
    Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'),
    Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'),
    Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'),
    Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')
]

text = input()

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
cleaned_text = ''.join(char for char in text if char not in punctuation)
words = cleaned_text.lower().split()

count = 0
for word in words:
    for morph in dict_words:
        if word in morph:
            count += 1
            break

print(count)