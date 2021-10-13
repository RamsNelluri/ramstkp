## Import Regular Expression - Used to replace all special characters other than alphanumeric
import re

## Input
giventext = "This is Medium article presented by ramstkp in the month of October. On the day of writing it was cold, and autumn started early this in the october month. October month is relatively less cold compared to winter months"

## Replacing all other characters other than alphanumerics
giventext = re.sub('[^a-zA-Z0-9 \n]', '', giventext)

## Converting to lower and splitting the text to list by word (split by space)
text_to_list = giventext.lower().split()

## EMpty dictionary
result_dict = {}

## Process to find words
for word in text_to_list:
    if word in result_dict.keys():
        result_dict[word] += 1
    else:
        result_dict[word] = 1

## Sort and print words in descedning order based in appereance.
print(sorted(result_dict.items(),key = lambda x: x[1], reverse=True))
