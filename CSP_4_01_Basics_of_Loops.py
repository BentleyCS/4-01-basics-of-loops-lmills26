#All questions must use a loop for full points.
import random




def oddNumbers(n:int) ->str:
    start = 1
    stop = n
    int = 2
    s = str(start)
    if n < 1:
        return ""
    while start + int <= stop:
        start = start + int
        s = s + " " + str(start)
    return(s)
    """
    Print out all odd numbers from 1 to n(inclusive) in a single string seperated by spaces.
    example oddNumbers(5) -> "1 3 5"
    example oddNumbers(8) -> "1 3 5 7"
    example oddNumbers(-8) -> ""
    """
oddNumbers(9)


def backwards(n)-> int:
    """
    modify the below function such that it prints out all the numbers from n to 1
    inclusive starting at n and counting down to 1
    example backwards(5) -> "5 4 3 2 1"
    example backwards(8) -> "8 7 6 5 4 3 2 1"
    example backwards(-2) -> ""
    """
    string = ""
    for x in range(n, 0, -1):
        string = string + f"{x} "

    newstring = string[:len(string)-1]
    print(newstring)
    return(newstring)
pass

def randomRepeating(n):
    start = random.randint(10)
    start = str(start)
    if start == 10:
        tries = 1
    while start < 10:
        tries = 1 + n
    print(f"it took {tries} tries to get a 10")
    tries = 0
    n = random.randint(1,10)
    while n!=10:
        print(n)
        tries += 1
        n =random.randint(1,10)
        print(n)
        tries += 1
    print(f"it took {tries} tries to get a 10")
    return(tries)
    """
    Print out a random number from 1-10 until you get a 10. Then print out how many
    times it took to roll a 10
    NOTE: Given randomness no test for this question
    :return:
    """

def randomRange(n):
    list = []
    while n > 0:
        num = random.randint(1,100)
        list = list.append(num)
        n = n - 1
    max = max(list)
    min = min(list)
    return (max, min)
    """
    Generate a random number from 1 to 100 n number of times. Then after that is
    done print out what the highest number and the lowers number was from the rolled numbers.
    NOTE: Given randomness no test for this question
    :param n:
    :return:
    """

def reverse(word:str)->str:
    reversedword = ""
    for i in range (len(word)):
        letter = word[-1 - i]
        reversedword += letter
    return (reversedword)
    """
    Takes in a string as an argument and return the given string in reverse.
    example reverse("cat") -> "tac"
    example reverse("Hello") -> "olleH"
    """


def fizzBuzzContinuous(n):
    for i in range(n):
        if i%3 == 0:
            return("fizz")
        elif i%5 == 0:
            return("buzz")
        elif i%3 == 0 and i%5 == 0:
            return ("fizzbuzz")
        else:
            return(i)
#fizzBuzzContinuous(n)

    """
    Modify the function such that it does the fizzbuzz operation on all numbers
    from 1 to n(inclusive).
    Fizz buzz is defined as
    if the number is divisble by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.

    As with above questions add each anseer to a string and return the final string.
    :param n:
    :return:
    """

def collatz(n):
    for i in range(n):
        if i==1:
            break
        elif i%2==0:
            return(i/2)
        else:
            return(i*3)
#collatz(n)

    """
    Modify this function such that it mimics the collatz conjecture starting at n
    and prints out each number.
    The collatz conjecture is that if n is an even number divide it by 2. if n is
    an odd number multiply it by 3 and add 1.
    Repeat this process until n == 1.
    :param n:
    :return:
    """


def fibonacci(n):
    if n == 1:
        return ("0")
    num1 = 0
    num2 = 1
    theresult = "0 1"
    for i in range (2,n):
        newnum = num1 + num2
        theresult += f" {newnum}"
        num1 = num2
        num2 = newnum
    return(theresult)







    """
    for the given argument n print out the first n numbers of the fibonacci
    sequence in a single string sperated by spaces.
    The fibonacci sequence is defined as a sequence that starts with 0 then 1 as
    the first two numbers. Every subsequent number is the prior two numbers added together.
    Example fibonacci(6) -> "0 1 1 2 3 5"
    Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    Example fibonacci(1) -> "0"
    :param n:
    :return:
    """


print(fibonacci(300))
