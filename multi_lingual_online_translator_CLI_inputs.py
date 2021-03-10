import sys
import requests
from bs4 import BeautifulSoup


class MachineTranslation:
    def __init__(self):
        self.args = sys.argv
        self.translated_words = []
        self.usage_examples = []
        self.url = None
        self.from_language = None
        self.target_lang = None
        self.lang_list = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew',
                          'Japanese', 'Dutch', 'Polish', 'Portuguese', 'Romanian',
                          'Russian', 'Turkish']
        self.word_to_translate = None
        self.all_lang = False
        self.isNonLatin = False
        self.file_writer = None
        self.isWord = True
        self.main()

    def main(self):
        self.word_to_translate = self.args[3].lower()
        to_create_file = self.word_to_translate + '.txt'
        self.file_writer = open(to_create_file, 'w', encoding='UTF-8')
        self.from_language = self.args[1].lower()
        self.target_lang = self.args[2].lower()
        if self.target_lang.title() not in self.lang_list and self.target_lang.lower() != 'all':
            print(f"Sorry, the program doesn't support {self.target_lang.lower()}")
            return
        if self.from_language.title() not in self.lang_list:
            print(f"Sorry, the program doesn't support {self.from_language.lower()}")
            return
        if self.target_lang != 'all':
            self.set_url()
            self.url = self.url + "/" + self.word_to_translate
            if self.target_lang == 'Arabic' or self.target_lang == 'Hebrew' or self.target_lang == 'Japanese' or \
                    self.target_lang == 'Spanish':
                self.isNonLatin = True
            self.print_results()
        elif self.target_lang == 'all':
            self.all_lang = True
            self.translate_to_all()
        self.file_writer.close()

    def translate_to_all(self):
        for language in self.lang_list:
            if language == self.from_language.title():
                continue
            if language == 'Arabic' or language == 'Hebrew' or language == 'Japanese' or language == 'Spanish':
                self.isNonLatin = True
            else:
                self.isNonLatin = False
            self.target_lang = language
            self.set_url()
            self.url = self.url + "/" + self.word_to_translate
            self.print_results()

    def set_url(self):
        self.url = "https://context.reverso.net/translation/" + str(self.from_language).lower() + "-" + str(self.target_lang).lower()

    def get_translation(self):
        if not self.isWord:
            return False
        user_agent = 'Mozilla/5.0'
        r = requests.get(self.url, headers={'User-Agent': user_agent})
        if int(r.status_code) == 404:
            print(f"Sorry, unable to find {self.word_to_translate}")
            self.isWord = False
            sys.exit(0)
        if r.ok:
            soup = BeautifulSoup(r.content, 'html.parser')
            raw_translated_words = soup.findAll('a', class_='translation')
            raw_usage_examples = soup.findAll('div', {"class": ['ltr', 'arabic', 'rtl']}) # class_='ltr'
            self.translated_words = []
            self.usage_examples = []
            for word in raw_translated_words:
                self.translated_words.append(word.text.strip())
            for sentence in raw_usage_examples:
                self.usage_examples.append(sentence.text.strip())
            return True
        else:
            print("Something wrong with your internet connection")
            return False

    def print_results(self):
        is_successful = self.get_translation()
        if is_successful and not self.all_lang:
            to_write = ""
            print()
            write_temp = f"{str(self.target_lang).title()} Translations:"
            to_write += write_temp + '\n'
            print(write_temp)
            for word in self.translated_words[1:6]:
                to_write += word + '\n'
                print(word)
            print()
            write_temp = f"{self.target_lang} Examples:"
            to_write += '\n' + write_temp + '\n'
            print(write_temp)
            if self.isNonLatin:
                for i in range(2, 16, 2):
                    write_temp = self.usage_examples[i+1]
                    to_write += write_temp + '\n'
                    print(write_temp)
                    write_temp = self.usage_examples[i+2]
                    to_write += write_temp + '\n\n'
                    print(write_temp)
                    print()
            else:
                for i in range(6, 16, 2):
                    write_temp = self.usage_examples[i]
                    to_write += write_temp + '\n'
                    print(write_temp)
                    write_temp = self.usage_examples[i+1]
                    to_write += write_temp + '\n\n'
                    print(write_temp)
                    print()
            self.file_writer.write(to_write)

        elif is_successful and self.all_lang:
            write_string = "\n"
            print()
            write_temp = f"{self.target_lang} Translations:"
            write_string += write_temp
            print(write_temp)
            for word in self.translated_words[1:6]:
                write_string += '\n' + word + '\n\n'
                print(word)
                break
            print()
            write_temp = f"{self.target_lang} Example:"
            write_string += write_temp + '\n'
            print(write_temp)
            if not self.isNonLatin:
                for i in range(13, 15, 2):
                    write_temp = self.usage_examples[i]
                    write_string += write_temp + '\n'
                    print(write_temp)
                    write_temp = self.usage_examples[i+1]
                    write_string += write_temp
                    print(write_temp)
                    print()
                    break
            else:
                for i in range(19, 21, 2):
                    write_temp = self.usage_examples[i+1]
                    write_string += write_temp + '\n'
                    print(write_temp)
                    write_temp = self.usage_examples[i+2]
                    write_string += write_temp
                    print(write_temp)
                    print()
                    break
            write_string += '\n\n'
            self.file_writer.write(write_string)


if __name__ == '__main__':
    machine_translation = MachineTranslation()
