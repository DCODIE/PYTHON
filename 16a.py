"""(a)	Write a python program to create package ‘Mystring ‘with 3 modules called Palindrome, CamelCase and CountVowel , the stack module should have the following functions 
Write a client code (Menu Driven) which imports package Mystring, reads the input from the user and invoke appropriate functions. """

from Mystring import Palindrome
from Mystring import vowels
from Mystring import Camelcase

str=input("Enter a string")
Palindrome.pal(str)
Camelcase.camel(str)
vowels.vow(str)
