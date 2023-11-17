import json
from makeNoisy import split_word
from makeWord import combine_word
from recoverWord import recover_word, convert_num
from language_identifier import contains_english, contains_only_korean
from exclude_special import exclude_special_characters

x = "안녕,"

print(split_word(x))