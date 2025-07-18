import time
import json
import csv
import string


def measure_time(func):
    def wrapper(*args, **kwargs):
        print("the function to note time is starting \n")
        start_time = time.time()
        result = func(*args, **kwargs)
        total_time = time.time() - start_time
        print(f"total time it took for the function {func.__name__} to run was {total_time}s \n")
        return result
    return wrapper

file_path_text1 = "/home/relinxx/Documents/python-practice/story.txt"

with open(file_path_text1,"w+") as textFile1:
    story = "The cat loves to sit on mat . The dog ran in the park " \
    "cat or dog are pets. Many people loves pets"
    textFile1.write(story)

with open("/home/relinxx/Documents/python-practice/words.txt","w") as textFile2:
    words_to_find = ["apple", "banana", "cat", "dog", "happy", "sad"]
    for word in words_to_find:
        textFile2.write(word + "\n")

with open(file_path_text1,"r") as readFile1:
    file_stuff = readFile1.read()

    cleaned_text = file_stuff.translate(str.maketrans('', '', string.punctuation)).lower()
    words = cleaned_text.split()
    print(words)

countDict = {word: words.count(word) for word in set(words) if word in words_to_find}
print("Word counts:", countDict)

long_words = [word for word in words if len(word) > 3]
print("Long words:", long_words)



filtered_word = lambda word: word.startswith(letter)
letter = input("enter the first letter of the word you wanna find \n")
list_of_filtered_words = list(filter(filtered_word, words))
print(list_of_filtered_words)

lower_word_list = list(map(lambda word: word.lower(), words))
print(lower_word_list)

def total_words(word_count):
    if len(word_count) == 0:
        return 0
    
    return 1 + total_words(word_count[1:])

print(total_words(words))


def longest_word_finder(words, longest_word):
    if not words:
        return longest_word
    
    if len(longest_word) < len(words[0]):
        longest_word = words[0]

    return longest_word_finder(words[1:],longest_word)

print(f"longest word is {longest_word_finder(words,"")} \n")

JsonFilePath = "/home/relinxx/Documents/python-practice/words.json"
with open(JsonFilePath,"w") as JsonFile:
    json.dump(countDict,JsonFile,indent=4)

with open(JsonFilePath, "r") as JsonFile:
    showcaseDict = json.load(JsonFile)
    print(showcaseDict)

csvFilePath = "/home/relinxx/Documents/python-practice/file.csv" 
with open(csvFilePath,"w", newline='') as CsvFile:
    phoneBook = [{"Name": "rehan", "address": "Rawalpindi", "phoneNo": "03355685701"}, 
                 {"Name": "taha", "address": "Peshawar", "phoneNo": "03355849993"},
                 {"Name": "yousaf", "address": "Islamabad", "phoneNo": "03353883922"}]

    writer = csv.writer(CsvFile)
    writer.writerow(phoneBook[0].keys())
    for dic in phoneBook:
        writer.writerow(dic.values())
    


@measure_time
def simulate_process(custom_time):
    time.sleep(custom_time)
    print(f"function has ended, expected time was {custom_time}s \n")



simulate_process(3)


def force_uppercase(func):
    def wrapper(*args):
        result = func(*args)
        uppercasedResult = result.upper()
        
        return uppercasedResult
    return wrapper

@force_uppercase
def get_name(name):
    return name
    
    
print(get_name("rehan"))

