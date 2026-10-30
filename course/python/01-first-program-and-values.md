# Chapter 1 — Your first Python program, values, and types

> **Book-length subject volume:** For expanded explanations, worked examples, review questions, and practice, read the [python textbook](TEXTBOOK.md).

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## What a program is

A computer follows precise instructions. Python code is text that the Python interpreter reads and executes. A program can receive input, calculate something, and produce output.

A value is information. A variable is a name referring to a value. Types describe what kind of value something is and what operations make sense.

    name = "Mina"
    age = 19
    height = 1.65
    is_learning = True

Here, name is text, age is an integer, height is a decimal number, and is_learning is a Boolean. The equal sign assigns the value on the right to the name on the left. It is not a mathematical equation claiming both sides are forever equal.

## Expressions and operations

An expression calculates a value. Numbers support arithmetic; strings support operations such as joining text. Comparisons such as age >= 18 produce True or False. Boolean operations combine conditions.

    age = 19
    can_register = age >= 18
    print(can_register)

The print function displays output. The input function asks for text from a user. Input is text even when the user types digits, so convert it before arithmetic. Conversion can fail; later you will learn to handle this with exceptions.

## Names and readable code

Choose names that describe purpose, such as total_price or number_of_examples. Python uses indentation to group statements. Consistent indentation is part of the program's meaning. Comments should explain why a decision exists, not merely repeat the line.

A useful first task is converting Celsius to Fahrenheit. Write the relationship as a formula before coding: Fahrenheit = Celsius × 9/5 + 32. Try input values 0, 20, and 100 and check the results.

## Errors are information

A syntax error means Python cannot understand the code form. A runtime error occurs while the program runs. A logical error means the program runs but returns the wrong answer. These require different fixes.

Read the last line of an error message for the exception type, then inspect the line number and values involved. Do not immediately rewrite the entire program.

## Questions and answers

**What is the difference between a variable and a value?**  
The value is the information; the variable is a name through which the program refers to it. A variable can later refer to a different value.

**Why does type matter?**  
Adding two numbers is arithmetic, while joining two strings creates text. Type conversion makes the intended operation explicit.

**What does input return?**  
It returns text. If a calculation needs a number, convert and validate it.

**Should I memorize syntax?**  
Learn common patterns through practice and use documentation for details. Programming skill includes finding and verifying the right syntax.

## Practice

1. Print your name and a sentence about why you want to learn AI.
2. Make a two-number calculator.
3. Write the Celsius converter and verify three known values.
4. Deliberately try dividing by zero and read the error.

## Mastery check

Explain assignment, type, expression, input, output, and one error message in your own words.