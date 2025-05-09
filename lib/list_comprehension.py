#!/usr/bin/env python3

def return_evens(num_list):
    return [even_num for even_num in num_list if even_num % 2  == 0]

def make_exclamation(sentence_list):
    return [sentence+"!" for sentence in sentence_list]