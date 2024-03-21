
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


# def add_binary(a,b):
#     sum = a+b
#     binary = []
#     while (sum/2) > 0:
#         remainder = sum%2
#         binary.append(remainder)
#         sum //=2
#     binary = ''.join(map(str, binary[::-1]))
#     return binary

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
    b = 1
    nums = []
    add_nums = []
    while b <= value:
        if (b ** p) < value:
            print(f'{b}:{b ** p}')
            nums.append(b ** p)
        b +=1
# now need to know if length of array longer than p
    if len(nums) >= p:
        print(f'nums is long enough')
        i = 0
        n = 0
        while i < len(nums) and n < (len(nums))-1:
            for num in nums:
                print(f'num = {num}, nums num = {nums[n]}, added together = {num + nums[n]}')
                # print(f'nums num = {nums[n]}')
                # print(f'added tog')
                print(f'n = {n}')
            n += 1
        i += 1
        
    
    return nums


  


# print(narcissistic(7))
print(narcissistic(371))
# print(narcissistic(122))
# print(narcissistic(4887))