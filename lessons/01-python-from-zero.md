# Lesson 01 — Python from zero

## Learning goals

Understand what a program is, write simple Python, use decisions and repetition, break work into functions, and debug errors.

## What programming means

A program is a set of precise instructions executed by a computer. A computer does not fill in missing steps the way a person often can. If your instruction is ambiguous, the program may fail or do the wrong thing.

Python is a programming language whose readable syntax makes it popular in data science and AI. Learning Python is not about memorizing every command. It is about learning to describe a problem as small steps and to check whether those steps do what you intended.

## Values, variables, and types

A **value** is a piece of information: a number, text, or true/false result. A **variable** is a name that lets you refer to a value later.

    name = "Ava"
    age = 20
    is_student = True

The values have different **types**. Text is a string, whole numbers are integers, decimal numbers are floating-point values, and true/false values are booleans. Types matter because adding two numbers differs from joining two pieces of text.

You can ask a user for input, but input arrives as text. If you expect a number, convert it and handle invalid input rather than assuming everyone types correctly.

## Decisions and repetition

A conditional chooses which instructions to run based on a true/false test. A loop repeats instructions.

    temperature = 31
    if temperature > 30:
        print("hot")
    else:
        print("comfortable")

A for-loop is useful when you have a collection or a known sequence. A while-loop repeats while a condition remains true. Every while-loop needs a way to eventually stop.

## Collections

A list holds ordered values. A dictionary stores values under named keys. These structures help organize data before you learn specialized data tools.

    scores = [8, 10, 7]
    person = {"name": "Ava", "score": 10}

You can loop through a list to calculate a sum or count values satisfying a condition. In AI, arrays, tables, and batches are larger and more specialized forms of organized data.

## Functions: name a reusable step

A function is a named block that can receive inputs, perform work, and return a result.

    def average(values):
        return sum(values) / len(values)

    result = average([8, 10, 7])

This function gives one name to a calculation. Good functions do one understandable job. They make programs easier to test and change.

A parameter is an input name in the function definition. An argument is the actual value supplied when calling the function. A return value passes a result back to the code that called the function.

## Files, libraries, and errors

Programs often read data from files or use libraries written by other people. A library is reusable code. Before using one, learn what it expects and what it returns.

An error message is evidence about what the computer could not do. Read the last line first to identify the error type, then follow the traceback to the line that caused it. Common errors include misspelled names, wrong types, missing files, and indexing beyond a list.

Debugging is a method:
1. Reproduce the problem.
2. Read the error carefully.
3. Check the values entering the failing line.
4. Make one change.
5. Run again and see whether the evidence changed.

A test is a small check that compares expected behavior with actual behavior. For average, test a list whose average you can calculate by hand. Also consider an empty list: should the function reject it, return a special value, or define a convention? State your choice.

## A worked thinking example

Task: count how many scores are at least 80.

- Input: a collection of scores.
- Output: one count.
- Start with a count of zero.
- Visit each score once.
- If the score is at least 80, increase the count.
- Return the final count.

This description is an algorithm before it is code. Writing the algorithm in plain words helps reveal edge cases.

## How Python helps with AI

Python is the language you use to prepare data, call machine-learning libraries, define experiments, and build small interfaces. Libraries such as NumPy, pandas, scikit-learn, and PyTorch provide larger building blocks, but the concepts of variables, functions, collections, and errors remain essential.

Do not begin by copying a large AI project. First make sure you can explain each input, transformation, and output. When you use an AI assistant, ask it to explain an error or provide a hint; then verify by running your own small example.

## Review questions with answers

**1. What is a variable?**  
A name that refers to a value so you can use or update it later. It does not mean the value is permanently fixed.

**2. Why do types matter?**  
Operations are interpreted according to type. Adding numbers performs arithmetic, while adding strings joins text. Converting input explicitly avoids surprising behavior.

**3. Why write a function?**  
A function gives a reusable, testable name to a task. It also lets you break a large program into smaller pieces with clear inputs and outputs.

**4. What should you do when you see an error?**  
Read it, reproduce the issue, inspect the values around the failing line, and test one change at a time. Do not randomly edit several places at once.

**5. Why consider an empty list or invalid input?**  
Real users and datasets include edge cases. If behavior is undefined, the program may crash or silently return a misleading answer.

## Practice

1. Make a temperature converter.
2. Write a function that returns the largest number in a non-empty list. Decide what should happen for an empty list.
3. Read a list of scores and report count, minimum, maximum, and average.
4. Deliberately make a typo or type mismatch, read the error, then fix it.

## Mastery check

Can you write a short program using a function, a conditional, and a loop without copying it? Can you explain one edge case and show how you tested it? If yes, continue.