#solved with a more intuitive approach, finds the value of the word if it exists in the almost_correct array, If not uses the mean of the start_time and end_time differences between consequetive 
#words, the added time which will be used to output as speech for a word is added to the start and end times of all the subsequent words, creating a smoother and more realtime solution

import ast
import re

def find_word_in_tuples(word, tuples_list):
    for tup in tuples_list:
        if tup[0].lower() == word.lower():
            yield tup[1], tup[2]

tuples_list = [('m', 0.0, 0.4), ('b', 0.4, 0.7), ('a', 0.7, 0.7), ('hardworking', 0.7, 1.4), ('middle', 1.4, 1.8), ('class', 1.8, 2.1), ('man', 2.1, 2.3), ('from', 2.3, 2.5), ('Delhi', 2.5, 2.8), ('trying', 2.8, 3.5), ('to', 3.5, 3.6), ('build', 3.6, 3.7), ('the', 3.7, 3.8), ('secure', 3.8, 4.2), ('future', 4.2, 4.4), ('for', 4.4, 4.8), ('his', 4.8, 5.0), ('family', 5.0, 5.4), ('Ravi', 5.4, 6.4), ('always', 6.4, 6.8), ('dreamt', 6.8, 7.1), ('of', 7.1, 7.2), ('a', 7.2, 7.3), ('comfortable', 7.3, 7.7), ('retirement', 7.7, 8.0), ('a', 8.0, 8.6), ('good', 8.6, 8.9), ('education', 8.9, 9.0), ('for', 9.0, 9.5), ('his', 9.5, 9.7), ('children', 9.7, 10.1), ('and', 10.1, 10.2), ('a', 10.2, 10.3), ('well-deserved', 10.3, 10.8), ('vacation', 10.8, 11.4), ('for', 11.4, 11.5), ('his', 11.5, 11.7), ('wife', 11.7, 11.9), ('but', 11.9, 13.0), ('his', 13.0, 13.3), ('modest', 13.3, 13.6), ('income', 13.6, 14.0), ('seem', 14.0, 14.2), ('to', 14.2, 14.3), ('be', 14.3, 14.4), ('a', 14.4, 14.4), ('hurdle', 14.4, 14.8), ('then', 14.8, 15.4), ('he', 15.4, 15.6), ('discovered', 15.6, 16.1), ('that', 16.1, 16.3), ('forms', 16.3, 16.7), ('a', 16.7, 17.0), ('trusted', 17.0, 17.4), ('name', 17.4, 17.5), ('in', 17.5, 17.8), ('mutual', 17.8, 18.2), ('fund', 18.2, 18.4), ('investments', 18.4, 19.0), ('in', 19.0, 19.1), ('India', 19.1, 19.5), ('they', 19.5, 20.4), ('introduced', 20.4, 20.9), ('into', 20.9, 21.1), ('the', 21.1, 21.2), ('concept', 21.2, 21.7), ('of', 21.7, 21.8), ('systematic', 21.8, 22.4), ('investment', 22.4, 22.7), ('plan', 22.7, 23.0), ('a', 23.0, 23.5), ('sip', 23.5, 23.8), ('a', 23.8, 24.2), ('simple', 24.2, 24.7), ('disciplined', 24.7, 25.3), ('and', 25.3, 25.5), ('affordable', 25.5, 25.7), ('way', 25.7, 26.2), ('to', 26.2, 26.2), ('invest', 26.2, 26.6), ('Ravi', 26.6, 27.8), ('started', 27.8, 28.2), ('with', 28.2, 28.3), ('a', 28.3, 28.4), ('small', 28.4, 28.7), ('amount', 28.7, 28.8), ('every', 28.8, 29.3), ('month', 29.3, 29.6), ('as', 29.6, 30.2), ('yours', 30.2, 30.4), ('past', 30.4, 30.8), ('Ravi', 30.8, 31.3), ('so', 31.3, 31.4), ('his', 31.4, 31.6), ('wealth', 31.6, 32.0), ('grow', 32.0, 32.2), ('steadily', 32.2, 32.5), ('he', 32.5, 33.2), ('was', 33.2, 33.4), ('surprised', 33.4, 33.9), ('field', 33.9, 34.3), ('and', 34.3, 34.5), ('relieve', 34.5, 34.8), ('his', 34.8, 35.4), ('dreams', 35.4, 35.8), ('were', 35.8, 35.9), ('no', 35.9, 36.0), ('longer', 36.0, 36.2), ('unattainable', 36.2, 37.1), ('the', 37.1, 37.6), ('turning', 37.6, 37.9), ('point', 37.9, 38.1), ('game', 38.1, 38.5), ('when', 38.5, 38.7), ('is', 38.7, 38.8), ('not', 38.8, 39.1), ('a', 39.1, 39.1), ('secured', 39.1, 39.6), ('admission', 39.6, 40.0), ('in', 40.0, 40.1), ('a', 40.1, 40.2), ('prestigious', 40.2, 40.4), ('University', 40.4, 41.4), ('the', 41.4, 42.2), ('funds', 42.2, 42.5), ('for', 42.5, 42.6), ('education', 42.6, 43.5), ('is', 43.5, 44.0), ('a', 44.0, 44.1), ('sip', 44.1, 44.5), ('investment', 44.5, 44.8), ('and', 44.8, 45.8), ('so', 45.8, 46.0), ('Ravi', 46.0, 46.5), ('story', 46.5, 47.0), ('is', 47.0, 47.0), ('a', 47.0, 47.1), ('Testament', 47.1, 47.3), ('to', 47.3, 47.7), ('the', 47.7, 47.8), ('benefits', 47.8, 48.3), ('of', 48.3, 48.3), ('a', 48.3, 48.5), ('sip', 48.5, 48.8), ('in', 48.8, 49.1), ('mutual', 49.1, 49.2), ('funds', 49.2, 49.8), ('Z', 49.8, 50.9), ('funds', 50.9, 51.4), ('not', 51.4, 51.6), ('only', 51.6, 51.8), ('help', 51.8, 52.1), ('rebuild', 52.1, 52.5), ('his', 52.5, 52.7), ('wealth', 52.7, 53.1), ('but', 53.1, 53.3), ('also', 53.3, 53.5), ('turned', 53.5, 53.9), ('his', 53.9, 54.1), ('dreams', 54.1, 54.4), ('into', 54.4, 54.7), ('reality', 54.7, 54.7), ('all', 54.7, 56.1), ('it', 56.1, 56.2), ('took', 56.2, 56.3), ('was', 56.3, 56.5), ('a', 56.5, 56.6), ('small', 56.6, 56.7), ('step', 56.7, 57.3), ('a', 57.3, 57.5), ('disciplined', 57.5, 58.0), ('approach', 58.0, 58.1), ('and', 58.1, 58.7)]

generators = {}

def get_next_occurrence(word):
    if word not in generators:
        generators[word] = find_word_in_tuples(word, tuples_list)
    return next(generators[word], (None, None))

s = "Meet Ravi. A hardworking middle-class man from Delhi, striving to build a secure future for his family. Ravi always dreamt of a comfortable retirement, a good education for his children and a well-deserved vacation for his wife. But, his modest income seemed to be a hurdle.Then, he discovered Z. Funds, a trusted name in mutual fund investments in India. They introduced him to the concept of Systematic Investment Plan, S.I.P., a simple, disciplined and affordable way to invest. Ravi started with a small amount every month. As years passed, Ravi saw his wealth grow steadily. He was surprised, thrilled and relieved. His dreams were no longer unattainable. The turning point came when his daughter secured admission in a prestigious university. The funds for her education? His S.I.P. investment. And so, Ravi's story is a testament to the benefits of S.I.P. in mutual funds. Z. Funds not only helped Ravi build his wealth but also turned his dreams into reality. All it took was a small step, a disciplined approach, and"

def fetch_data_for_string(s):
    words = re.split(r'[ ,.-]', s)
    result = []

    for word in words:
        if word:  # To prevent empty strings
            start_time, end_time = get_next_occurrence(word)
            if start_time is not None:
                result.append((word, start_time, end_time))
            else:
                result.append((word, None, None))

    return result

data = fetch_data_for_string(s)

# Calculate mean difference of end time for consecutive words where neither is None
end_time_diffs = [data[i+1][2] - data[i][2] for i in range(len(data)-1) if data[i][2] is not None and data[i+1][2] is not None]
mean_end_time_diff = round(sum(end_time_diffs) / len(end_time_diffs) if end_time_diffs else 0, 1)

# Handle cases where start and/or end times are None
count = 0
for i, (word, start_time, end_time) in enumerate(data):
    if start_time is None:
        count += 1
        if i == 0:
            start_time = 0.0
            end_time = round(start_time + mean_end_time_diff, 1)
        else:
            start_time = data[i-1][2]  # end time of previous word
            end_time = round(start_time + mean_end_time_diff, 1)
        data[i] = (word, start_time, end_time)
    else:
        count = 0  # reset the count

    if count > 2:  # if there are more than 2 consecutive None times, use mean_end_time_diff
        end_time = round(start_time + mean_end_time_diff, 1)
        data[i] = (word, start_time, end_time)

# print the results
# for word_data in data:
print(data)
