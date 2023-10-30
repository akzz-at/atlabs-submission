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

After defining the list of tuples (`tuples_list`) and the target string (`s`), you can fetch the time stamps for each word in `s` as follows:

```python
data = fetch_data_for_string(s)
adjusted_data = adjust_time_with_pointers(data)
