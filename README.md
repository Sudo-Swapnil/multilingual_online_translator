This project is a python program that is capable of translating a given one into any (or all) of the 13 supported languages. 

It first provides the user with word which most likely is the direct translation of the given word, followed by synonyms of the word. 

Finally, it provides the user with ample of sample sentences to show how the word is to be used in context. 

In the end, the program creates a file named same as the word whose translation is done. In this file, all the content displayed on the console is written for future reference for the user.


Technology and tools:
1. Python 3
2. bs4 -> BeautifulSoup
3. requests
4. sys

Supported Languages:
1.  Arabic
2.  German
3.  English
4.  Spanish
5.  French
6.  Hebrew
7.  Japanese
8.  Dutch
9.  Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish

For sample translations, refer files:
'hello(sample translation of word hello).txt' -> translation of 'hello' in all remaining 12 supported languages
'глаза (sample translation of word глаза to english).txt' -> translation of 'глаза' into english

Main programs:
1. multi_lingual_online_translator_CLI_inputs.py -> the inputs to this program must be passed through command line.
   Format: python <file_name.py> <input_langague> <target_language> <word_to_translate>
2. multi_lingual_online_translator_user_inputs.py -> Simply run this script and the program will ask for inputs during execution. to translate to all other languages, enter 'all' as the target language
