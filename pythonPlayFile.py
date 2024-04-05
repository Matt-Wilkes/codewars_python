import re
from itertools import combinations
import math
import string
from functools import reduce
import numpy as np

# append next word onto the end of current word until there are no words left

def spacey(array):
    newArray = []
    text=''
    for item in array:
        text = text+item
        newArray.append(text)
    print(newArray)

# spacey(['kevin', 'has','no','space'])
# spacey(['this','cheese','has','no','holes'])

# returns:
# ['kevin', 'kevinhas', 'kevinhasno', 'kevinhasnospace']
# ['this', 'thischeese', 'thischeesehas', 'thischeesehasno', 'thischeesehasnoholes']
    

# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"
    


def reverse_words(text):
    new_array =[]
    text = text[::-1]
    array = []
    new_array.append(text.split(' '))
    for word in new_array:
        array.append(word[::-1])
    return ' '.join(array[0])
  
# print(reverse_words('The quick brown fox jumps over the lazy dog.'))
# print(reverse_words('apple'))
# print(reverse_words('a b c d'))
# print(reverse_words('double  spaced  words'))

# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

# The binary number returned should be a string.

# Examples:(Input1, Input2 --> Output (explanation)))

# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)


def add_binary(a,b):
    sum = a+b
    binary = []
    while (sum/2) > 0:
        remainder = sum%2
        binary.append(remainder)
        sum //=2
    binary = ''.join(map(str, binary[::-1]))
    return binary

# refactored 
def add_binary_2(a,b):
    return bin(a+b)[2:] #[2:] is a slicing function and has sliced the first two characters

# add_binary(1,1) #10
# add_binary(0,1) #1
# add_binary(1,0) #1
# add_binary(2,2) #100
# add_binary(51,12) #111111

# print(add_binary_2(1,1)) #10
# print(add_binary_2(0,1))#1
# print(add_binary_2(1,0)) #1
# print(add_binary_2(2,2)) #100
# print(add_binary_2(51,12)) #111111

def narcissistic(value):
    p = len(str(value))
    numbers = list(str(value))
    nums = []
    for i in numbers:
        nums.append(int(i) ** p)
    if sum(nums) == value:
        narc_num = True
    else:
        narc_num = False
    return narc_num

# print(narcissistic(7))
# print(narcissistic(371))
# print(narcissistic(122))
# print(narcissistic(4887))
# print(narcissistic(17333509997782249308725103962772))

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false

def is_isogram(string):
    letters = []
    isogram = True
    letters = [i.lower() for i in string]
    # for i in string:
    #     letters.append(i.lower())
        # print(f'{i} = {letters.count(i)}')
    for l in letters:
        count = letters.count(l)
        if count <= 1:
            isogram = True
        else:
            isogram = False
            break
    return isogram

# refactored: sets the string to lower case, then uses set function to remove duplicate characters, compares length and if length is different then word is not an isogram.
def is_isogram(string):
    return len(string) == len(set(string.lower()))

# print(is_isogram("Dermatoglyphics"))
# print(is_isogram("isogram")) 
# print(is_isogram("aba"))# False, "same chars may not be adjacent" 
# print(is_isogram("moOse"))# False, "same chars may not be same case"
# print(is_isogram("isIsogram"))#False 
# print(is_isogram(""))# True an empty string is a valid isogram" 

# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

def domain_name(url):
    url_front = re.search("http://www.|https://|http://|www.",url, flags=re.IGNORECASE)
    if url_front:
        front = url[url_front.end():]
    else:
        front = url
    front = re.split('[.]',front)
    return(front[0])
        
    # print(url["http://":"."])

# refactored
def domain_name2(url):
    # split by //, then split by www., then ..
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

# print(domain_name("http://google.com"))
# print(domain_name("http://google.co.jp"))
# print(domain_name("https://123.net"))
# print(domain_name("https://hyphen-site.org"))
# print(domain_name("http://codewars.com"))
# print(domain_name("www.xakep.ru"))
# print(domain_name("https://youtube.com"))
# print(domain_name("http://www.codewars.com/kata/"))
# print(domain_name("icann.org"))

# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    split = text.split(' ')
    pig_latin = []
    for w in split:
        k = w[1:len(w)]+w[0]
        if re.match(r'[a-z]', k, flags=re.IGNORECASE):
            k = k+'ay'
            pig_latin.append(k)
        else:
            pig_latin.append(k)
    return ' '.join(pig_latin)


# refactored 

def pig_it2(text):
    split = text.split(' ')
    pig_latin = []
    for w in split:
        w = w[1:]+w[0]
        if w.isalpha():
            w+='ay'
            # pig_latin.append(w)
        pig_latin.append(w)
    return ' '.join(pig_latin)

def pig_it3(text):
    lst = text.split()

    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

# Examples
# print(pig_it2('Pig latin is cool')) # igPay atinlay siay oolcay
# print(pig_it2('Hello world !'))     # elloHay orldway !


# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, 
# they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.
def rot13(message):
    alpha_lower = (string.ascii_lowercase)
    alpha_upper = (string.ascii_uppercase)
    #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ, if z = 51
    rot13 = []
    for i in message:
        if i.isalpha():
            if i.isupper():
                id = alpha_upper.rfind(i)+13
                if id >= len(alpha_upper):
                    id = (id - len(alpha_upper))
                rot13.append(alpha_upper[id])
            elif i.islower():
                id = alpha_lower.rfind(i)+13
                if id >= len(alpha_lower):
                    id = (id - len(alpha_lower))
                rot13.append(alpha_lower[id])
        else:
            rot13.append(i)
    return(''.join(rot13))
            
        # print(i)

    # return message
    

# print(rot13('test'))#, 'grfg', 'Returned solution incorrect for fixed string = test')
# print(rot13('Test'))#, 'Grfg', 'Returned solution incorrect for fixed string = Test')
# print(rot13('aA bB zZ 1234 *!?%'))#, 'nN oO mM 1234 *!?%', 'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%')
# print(rot13('abcdefghijklmnopqrstuvwxyz'))

# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

def find_it(seq):
    numbers = {}
    for n in seq:
        if n not in numbers:
            numbers[n] = 1
        else:
            numbers[n] +=1
    for n in numbers:
        if numbers[n] % 2 != 0:
            return n

# refactored 1
        def find_it1(seq):
            for i in seq:
                if seq.count(i)%2!=0:
                    return i
        
# refactored 2
        def find_it2(seq):
            return [x for x in seq if seq.count(x) % 2][0]

# print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])) #should return 5 (because it appears 3 times)")
# print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))# should return -1 (because it appears 1 time)")
# print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5])) #should return 5 (because it appears 3 times)")
# print(find_it([10])) # should return 10 (because it appears 1 time)")
# print(find_it([10, 10, 10])) #should return 10 (because it appears 3 times)")
# print(find_it([1,1,1,1,1,1,10,1,1,1,1])) #should return 10 (because it appears 1 time)")
# print(find_it([5,4,3,2,1,5,4,3,2,10,10])) #should return 1 (because it appears 1 time)")

# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

def generate_hashtag(s):
    if s:
        hashtag = '#'+''.join(s.title().split())
        if len(hashtag) <= 140:
            return hashtag
        else:
            hashtag = False
    else:
        hashtag = False
    return hashtag

# print(generate_hashtag('Codewars'))# '#Codewars', 'Should handle a single word.'
# print(generate_hashtag('Codewars      '))#, '#Codewars', 'Should handle trailing whitespace.'
# print(generate_hashtag('      Codewars'))#, '#Codewars', 'Should handle leading whitespace.'
# print(generate_hashtag('Codewars Is Nice'))#, '#CodewarsIsNice', 'Should remove spaces.'
# print(generate_hashtag('codewars is nice'))#, '#CodewarsIsNice', 'Should capitalize first letters of words.'
# print(generate_hashtag('CoDeWaRs is niCe'))#, '#CodewarsIsNice', 'Only the first letter of each word should be capitalized in the final hashtag, all other letters must be lower case.'
# print(generate_hashtag('c i n'))# '#CIN', 'A single letter is considered to be a word of length 1, so should capitalize first letters of words of length 1.'
# print(generate_hashtag('codewars  is  nice'))#, '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.'
# print(generate_hashtag(''))#, False, 'Expected an empty string to return False'
# print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))#, False, 'Should return False if the final string is longer than 140 chars.'

# def get_pins(observed):
    
#     # combinations depends on number of button presses i.e '0' = 0 or 8, 08 = 08, 80, 09, 05, 07, etc
    
#     keypad = [['1','2','3'],['4','5','6'],['7','8','9'],['','0','']]
#     digits = [n for n in observed]
#     pressed = []
#     combinations = {}
#     for n in digits:
#         combinations[n]=[]
#         combinations[n].append(n)
#         for k in keypad:
#             if n in k:            
#                 row = keypad.index(k)
#                 column = k.index(n)
#         if column < 2:
#             right = keypad[row][column+1]
#             combinations[n].append(right)
#         if column > 0:
#             left = keypad[row][column-1]
#             combinations[n].append(left)
#         if row > 0:
#             above = keypad[row-1][column]
#             combinations[n].append(above)
#         if row < 3:
#             below = keypad[row+1][column]
#             combinations[n].append(below)

#     print(combinations)
#     return digits


# print(get_pins('1357'))
# print(get_pins('0'))
# print(get_pins('1'))
# print(get_pins('2'))
# print(get_pins('5'))

# [
#         ('8', ['5','7','8','9','0']),
#         ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
#         ('369', [
#             "339","366","399","658","636","258","268","669","668","266","369","398",
#             "256","296","259","368","638","396","238","356","659","639","666","359",
#             "336","299","338","696","269","358","656","698","699","298","236","239"
#         ])
#     ]

def get_combo():
    pressed = []
    combinations = [
        ['1', '2', '4'], 
        ['3', '2', '6'], 
        ['5', '6', '4', '2', '8'], 
        ['7', '8', '4', '']]
    
    
    # print(len(combinations))
    for coms in combinations:
        i = 1
        n = 0
        while i < len(combinations):
            for num in coms:
                while n < len(combinations[i]):
                    print(f'num = {num}')
                # while n < len(combinations)
                    print(f'coms = {combinations[i][n]}')
                    n += 1
                i += 1
            
            
    # i += 1
    print(pressed)
# print(get_combo())

# Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

# If a string contains all repeating characters, it should return an empty string ("");

# † Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character.

def first_non_repeating_letter(s):
    duplicates = []
    if len(s) > 0:
        for l in s:
            l = l.lower()
            if s.lower().count(l) > 1:
                duplicates.append(l)
        if len(duplicates) != len(s):
            for k in s:
                if k.lower() not in duplicates:
                    return k
                else:
                    pass
        else:
            return ""
    else:
        return ""

# print(first_non_repeating_letter('a'))#, 'a')
# print(first_non_repeating_letter('stress'))#, 't')
# # print(first_non_repeating_letter('moonmen'))#, 'e')

# #     # @test.it('Should handle empty strings')
# #     # def _():
# print(first_non_repeating_letter(''))#, '')

# # #     # @test.it('Should handle strings without unique characters') 
# # #     # def _():
# print(first_non_repeating_letter('abba'))#, '')
# print(first_non_repeating_letter('aa'))#, '')

# # #     # @test.it('Should handle exotic characters')
# # #     # def _():
# print(first_non_repeating_letter('~><#~><'))#, '#')
# print(first_non_repeating_letter('hello world, eh?'))#, 'w')

# #     # @test.it('Should handle letter case correctly')
# #     # def _():
# print(first_non_repeating_letter('sTreSS'))#, 'T')
# print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))#, ',')
# print(first_non_repeating_letter('GWvk7J7bG7VJMVbMbBkbOOB7Wv'))

# My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.

# I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.

# Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

# Example:
# "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: 

# "100 180 90 56 65 74 68 86 99"
# When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers:

# 180 is before 90 since, having the same "weight" (9), it comes before as a string.

# All numbers in the list are positive numbers and the list can be empty.

# Notes
# it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers
# For C: The result is freed.

def order_weight(strng):
    weights = strng.split()
    new_weights = []
    for weight in weights:
        new_weights.append(weight.split())
        for w in weights:
            new_weights.append(w)
        # new_weights[weight] = reduce(lambda x, y: int(x)+int(y), weight)
        # sorted_weights = sorted(new_weights.items(), key = lambda x:x[1])
        # weight_d = dict(sorted_weights)
    # print(weight_d)
    return new_weights

# print(order_weight("103 123 4444 99 2000"))#, "2000 103 123 4444 99")
# print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))#, "11 11 2000 10003 22 123 1234000 44444444 9999")
# print(order_weight(""))#, "")

# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

def make_readable(seconds):
    hh = 00
    mm = 00
        
    if seconds >= 3600:
        ss = seconds % (100 * 3600)
        hh = ss // 3600
        # print(hh)
        ss %= 3600
        mm = ss // 60
        ss %= 60
        print(mm)
    elif seconds >= 60 and seconds < 3600:
        ss = seconds % 3600
        mm = ss // 60
        # print(f'{hh}:{mm}:{ss}')
    else:
        ss = seconds
        # print(f'{hh}:{mm}:{ss}')
        

    return "%02d:%02d:%02d" % (hh, mm, ss)
# print(f'{hh},{mm}')
        
        

# print(make_readable(0))#, "00:00:00")
# print(make_readable(59))#, "00:00:59")
# print(make_readable(60))#, "00:01:00")
# # print(make_readable(3599))#, "00:59:59")
# # print(make_readable(3600))#, "01:00:00")
# # print(make_readable(86399))#, "23:59:59")
# print(make_readable(86400))#, "24:00:00")
# print(make_readable(359999))#, "99:59:59")
# print(make_readable(22545))#, "06:15:45")

# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# Note: The function accepts an integer and returns an integer.

# Happy Coding!

def square_digits(num):
    digi = str(num)
    squared = []
    for i in digi:
        squared.append(str((int(i) ** 2)))
    return int(''.join(squared))

# refactored 

def square_digits2(num):
    digi = ''
    for i in str(num):
        digi += str(int(i)**2)
    return int(digi)

def square_digits3(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

# print(square_digits2(9119))

# https://mathspp.com/blog/base-conversion-in-python

# import math
import math
def esthetic(num):
    base_nums = [2,3,4,5,6,7,8,9,10]
    results = []
    for b in base_nums:
        n = num
        digits = []
        while n:
            digits.append(n % b)
            n //= b
        i = 0
        if len(digits) > 1:
            for x,y in zip(digits[::],digits[1::]):
                if (x - y) == 1 or (y - x) == 1:
                    i = i + 1
                else: 
                    pass
                if i >= (len(digits)-1):
                    results.append(b)
        elif len(digits) == 1:
                i = i + 1
                results.append(b)
                
    return results

# creator solution:
def esthetic2(num):
	return [b for b in range(2,11) if xx(num,b)] or []

def xx(n,b):
	return n//b==0 or abs(n%b-n//b%b)==1 and xx(n//b,b)

# refactored solution using numpy // https://numpy.org/ - scientific computing package - see notes
#  np.base_repr to get base representation
# unpack results to new list using *map - evaluate straight away
# np.diff used to find the difference
# np.abs used on results of difference to get absolute values (i.e. 1)
# for loop - if n == 1 (absolute value)
# all returns true if all values are true in iterable (for loop)

def esthetic3(num):
  return [b for b in range(2, 11) if all(n == 1 for n in np.abs(np.diff([*map(int, np.base_repr(num, b))])))]


# print(esthetic3(10))
# print(esthetic3(441))

# You are going to be given a word. Your job will be to make sure that each character in that word has the exact same number of occurrences. You will return true if it is valid, or false if it is not.

# For this kata, capitals are considered the same as lowercase letters. Therefore: "A" == "a"

# The input is a string (with no spaces) containing [a-z],[A-Z],[0-9] and common symbols. The length will be 0 < length < 100.

# Examples
# "abcabc" is a valid word because "a" appears twice, "b" appears twice, and"c" appears twice.
# "abcabcd" is NOT a valid word because "a" appears twice, "b" appears twice, "c" appears twice, but "d" only appears once!
# "123abc!" is a valid word because all of the characters only appear once in the word.

def validate_word(word):

    letters = list(map(str.lower, word))
    l_count = set()
    for i in letters:
        l_count.add(letters.count(i))
    if len(l_count) > 1:
        return False
    else:
        return True

# refactored/best solution 

from collections import Counter

def validate_word(word):
    return len(set(Counter(word.lower()).values())) == 1

# https://docs.python.org/3/library/collections.html
# //https://www.hackerrank.com/challenges/collections-counter/problem
# collections.Counter()
# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values. 


# Write a function, isItLetter or is_it_letter or IsItLetter, which tells us if a given character is a letter or not.
def is_it_letter(s):
    return s.isalpha()

# You will be given a sphere with radius(r). Imagine that sphere gets cut with flat surface, in this case the figure that is made with this cut is circle. 
# You will also be given distance(h) between centres of sphere and circle.
# Your task is to return the area of the original sphere,area of circle and perimeter of circle, 
# all of them rounded to 3 decimal places and order must be same as in the description.

from math import pi, sqrt

def stereometry(r, h):
    circle_r = sqrt(r**2-h**2)
    sphere_a = round(4 * pi * (r**2),3)
    circle_a = round(pi * circle_r ** 2, 3)
    circle_c = round(sqrt(pi * circle_r ** 2 * pi)*2,3)
    return sphere_a, circle_a, circle_c


string1 = "283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767837449448255379774726847104047534646208046684259069491293313677028989152104752162056966024058038150193511253382430035587640247496473263914199272604269922796"
def numofn(string):
    # string = string.split()
    n = 0
    for i in string:
        if i == "4":
            n = n + 1
    return n
        
print(numofn(string1))