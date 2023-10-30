# Word Time Stamps Approximation - Code-A

This code aims to handle and approximate time stamps for words in a given text based on a list of tuples which contains word time stamps.

## Overview

The given code primarily does the following:

1. Takes a list of tuples, where each tuple contains a word, its start time, and its end time.
2. Processes a string, `s`, and assigns time stamps to each word in `s` based on the given tuples.
3. Approximates time stamps for words in `s` that do not have a corresponding time stamp in the given tuples.

## How it Works

### Main Functions

- `find_word_in_tuples(word, tuples_list)`: This function iterates over `tuples_list` and yields the start and end time for each occurrence of `word`.
- `get_next_occurrence(word)`: Uses the generator pattern to fetch the next occurrence of `word` from `tuples_list`.
- `fetch_data_for_string(s)`: Processes the string `s`, splits it into words, and assigns time stamps to each word using `get_next_occurrence`. If a word does not have a time stamp, it assigns `None` values.
- `adjust_time_with_pointers(data)`: Uses two pointers to identify sequences of words without time stamps and approximates their time stamps based on surrounding words with known time stamps.

### Corner Cases Handled

1. **Multiple Occurrences of the Same Word**: If a word appears multiple times in the `tuples_list`, the code ensures that each occurrence of the word in the string `s` is mapped to the correct time stamp from `tuples_list`.
  
2. **Words Without Time Stamps**: Words in the string `s` that do not have a corresponding time stamp in `tuples_list` are assigned `None` values initially. The `adjust_time_with_pointers` function then approximates time stamps for these words based on the surrounding words with known time stamps.

3. **Initial Words Without Time Stamps**: If the first few words in `s` do not have time stamps in `tuples_list`, the code ensures that they are given appropriate time stamps. This is achieved by setting the start time of the first word to `0.0` and incrementing the end time by `0.1`.

## Usage







# Word Timestamp Approximation - Code - B

This solution processes a list of word timestamps and matches them with the corresponding words in a given string.

## 🚀 Key Features

- **Flexible Input:** Works with a list of tuples where each tuple contains a word, its start time, and its end time.
- **Generators:** Efficiently yields the timestamps for a particular word using Python's generator functionality.
- **Robust Handling:** In cases where a word from the string does not have a timestamp in the list, the solution estimates it using the average difference of end times from the available data.

## 🔍 Implementation Details

1. **Data Storage:** 
    - The list `tuples_list` stores tuples of (word, start time, end time).
    - A dictionary `generators` caches generators for each word, optimizing repeated requests.

2. **String Parsing:** The string is tokenized into words using the regular expression `r'[ ,.-]'`.

3. **Fetching Data:** For each word in the string, the solution retrieves its corresponding start and end times. If not found, it estimates the times.

4. **Mean Difference Calculation:** Calculates the mean difference of end times for consecutive words, which is then used for estimation in cases where the timestamp is missing.

## 🛠️ Corner Cases Handled

- **Missing Timestamps:** If a word in the string doesn't have a corresponding timestamp, it estimates the start and end times based on the average end time difference of other words.
- **Consecutive Missing Timestamps:** If multiple consecutive words do not have timestamps, they are handled sequentially using the previously computed or estimated timestamp.
- **Words At Start:** For the first word of the string, if its timestamp is missing, it assumes a start time of 0.0 and estimates the end time.

## ⚠️ Drawbacks

- **Estimation Accuracy:** The solution estimates missing timestamps based on the mean end time difference. This may not always be accurate.
- **Tokenization Limitations:** The current regex may not handle all punctuation marks or special characters optimally.
- **Assumption on Missing Data:** If the first Occurence of the timestamp is missing, it assumes a start automatically parses in the data of future occurences which results in incorrect data


After defining the list of tuples (`tuples_list`) and the target string (`s`), you can fetch the time stamps for each word in `s` as follows:

```python
data = fetch_data_for_string(s)
adjusted_data = adjust_time_with_pointers(data)
