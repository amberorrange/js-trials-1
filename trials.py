"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)
    


def get_all_evens(nums):
    pass  # TODO: replace this line with your code
    even_nums = []
    for num in nums:
        if num % 2 ==0:
            even_nums.append(num)

    return even_nums



def get_odd_indices(items):
    odd_indices = []
    for i, item in enumerate(items):
        if i % 2 == 0:
            odd_indices.append(i)

    return odd_indices    
    


def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f'{i}. {item}')
        i += 1


def get_range(start, stop):
    nums = []
   
    while start < stop:
        nums.append(start)
        start += 1
    return nums



def censor_vowels(word):
    chars = []

    for letter in word:
        if 'aeiou' in letter:
            chars.append('*')
        else:
            chars.append(letter)
    
    return ''.join(chars)


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
