# Name: Jeb Barker
# Date: Sep. 18, 2020
# Do not forget to change the file name -> Save as
""" Tasks """

# 1. Given an input of a space-separated list of any length of integers, output the sum of them.
# 2. Output the list of those integers (from #1) that are divisible by three.
msg = input("list of numbers: ")
# print(msg)
# print(msg.split())
# print([int(x) for x in msg.split()])  # list comprehension
print("1. sum = " + str(sum([int(x) for x in msg.strip().split()])))  # #1
print("2. list of multiples of 3: " + str([int(x) for x in msg.strip().split() if int(x) % 3 == 0]))  # #2


# 3. Given an integer input, print the first n Fibonacci numbers. eg. n=6: 1, 1, 2, 3, 5, 8
def fib(n):
    a = b = 1
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        re = fib(n - 1)
        re.append(sum(re[:-3:-1]))
        return re


print("3. fibonacci: ", *fib(int(input("Type n for Fibonacci sequence:"))))

# 4. Given an input, output a string composed of every other character. eg. Aardvark -> Arvr
print("4. every other str: " + input("Type a string:")[0::2])

# 5. Given a positive integer input, check whether the number is prime or not.
msg = input("Type a number to check prime:")
print("5. Is prime? " + (str(False) if True in [int(msg) % n == 0 for n in range(2, int(msg))] else str(True)))

# 6. Calculate the area of a triangle given three side lengths.  eg. 13 14 15 -> 84
msg = input("Type three sides of a triangle:")
p = sum([int(x) for x in msg.strip().split()]) / 2
print("6. The area of " + msg + " is " + str(int((p * (p - int(msg.strip().split()[0])) * (
            p - int(msg.strip().split()[1])) * (p - int(msg.strip().split()[2]))) ** .5)))

# 7. Given a input of a string, remove all punctuation from the string.
#    eg. "Don't quote me," she said. -> Dontquotemeshesaid
# 8. Check whether the input string (from #7, lower cased, with punctuation removed) is a palindrome.
# 9. Count the number of each vowel in the input string (from #7).
msg = input("Type a sentence: ")
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_ ~'''
rem = msg.strip()
print("7. Punct removed: ", [rem := rem.replace(st, "") if st in punctuations else rem.replace(st, st) for st in rem][-1])
print("8. Is palindrome? " + str(True) if rem.lower() == rem.lower()[::-1] else str(False))
dic = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
print("9. Count each vowel: ", str([dic[key] := rem.lower().count(key) for key, value in dic]))

# 10. Given two integers as input, print the value of f\left(k\right)=k^2-3k+2 for each integer between the two inputs.
# eg. 2 5 -> 0, 2, 6, 12


# 11. Given an input of a string, determines a character with the most number of occurrences.
# 12. With the input string from #11, output a list of all the words that start and end in a vowel.
# 13. With the input string from #11, capitalizes the starting letter of every word of the string and print it.
# 14. With the input string from #11, prints out the string with each word in the string reversed.
# 15. With the input string from #11, treats the first word of the input as a search string to be found in the rest
# of the string, treats the second word as a replacement for the first, and treats the rest of the input as the string to be searched.
# 	eg.    b Ba baby boy ->  BaaBay Baoy


# 16. With an input of a string, removes all duplicate characters from a string.  Eg. detection -> detcion


# 17. Given an input of a string, determines whether the string contains only digits.
# 18. If #17 prints True, determines whether the string contains only 0 and 1 characters, and if so assumes it is a binary string,
# converts it to a number, and prints out the decimal value.


# 19. Write a script that accepts two strings as input and determines whether the two strings are anagrams of each other.


# 20. Given an input filename, if the file exists and is an image, find the dimensions of the image.


# 21. Given an input of a string, find the longest palindrome within the string.


# 22. Given an input of a string, find all the permutations of a string.
# 23. Given the input string from #22, find all the unique permutations of a string.


# 24. Given an input of a string, find a longest non-decreasing subsequence within the string (according to ascii value).
