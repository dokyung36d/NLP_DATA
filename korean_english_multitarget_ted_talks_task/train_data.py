import json
from makeNoisy import split_word
from makeWord import combine_word
from recoverWord import recover_word, convert_num
from language_identifier import contains_english, contains_only_korean
from exclude_special import exclude_special_characters

# Specify the path to your JSON file
json_file_path = 'korean_english_multitarget_ted_talks_task/train.json'

# Open the file in read mode
json_data = []
with open(json_file_path, 'r', encoding='UTF8') as f:
    for line in f:
        json_data.append(json.loads(line))


total_num=0

for i in range(len(json_data)):
    token_list = json_data[i]["korean"].split()

    if len(token_list) >= 4:
        data_list = []
        for j in range(3, len(token_list)):
            new_data = {"data" : token_list[j - 3 : j], "label" : token_list[j]}

            if contains_english(new_data['label']): #label단어가 영어인 경우
                for k in range(1, len(new_data["label"])):
                    last_token_list = token_list[j - 3 : j] + [new_data["label"][:k]]
                    data_list.append({"data" : last_token_list, "label" : token_list[j]})
                    total_num +=1
            else: #label 단어가 한국어인 경우
                split_korean = exclude_special_characters(new_data["label"])
                print(split_korean)
                if not contains_only_korean(split_korean):
                    continue
                split_korean = split_word(split_korean)[0]
                split_korean = convert_num(split_korean)
                for k in range(1, len(split_korean)):
                    last_token_list = token_list[j - 3 : j] + [combine_word(recover_word(split_korean[:k]))]
                    data_list.append({"data" : last_token_list, "label" : token_list[j]})    
                    total_num += 1
        
    for data in data_list:
        print(data)

print(total_num)