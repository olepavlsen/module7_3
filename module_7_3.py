def lower(param):
    pass


class WordsFinder:
    def __init__(self, *file_names):
        self.all_words = dict()
        self.file_names = [*file_names]

    def get_all_words(self):
        for i in range(len(self.file_names)):
            with open(self.file_names[i], encoding='utf-8') as file:
                list_of_words = file.read().lower()
            self.all_words[self.file_names[i]] = self.clean(list_of_words).split()
        return self.all_words

    def clean(self, list_of_words):
        self.list_of_words = list_of_words
        punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in range(len(punc)):
            if punc[i] in self.list_of_words:
                self.list_of_words = self.list_of_words.replace(punc[i], "")
        return self.list_of_words

    def find(self, word):
        found = dict()
        word = word.lower()
        for name, words in self.get_all_words().items():
            self.name = name
            self.words = words
            found[self.name] = self.words.index(word) + 1
        return found

    def count(self, word):
        counted = dict()
        word = word.lower()
        for name, words in self.get_all_words().items():
            self.name = name
            self.words = words
            counted[self.name] = self.words.count(word)
        return counted



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
#
# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))
