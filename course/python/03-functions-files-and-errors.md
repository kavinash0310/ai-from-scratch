# Chapter 3 — Functions, files, and errors

## Functions name a job

A function groups steps under a name. It can receive parameters, calculate a result, and return it to the caller.

    def average(values):
        if len(values) == 0:
            raise ValueError("values must not be empty")
        return sum(values) / len(values)

    class_average = average([80, 90, 70])

The function has one job and makes an assumption explicit. Parameters are names in the definition; arguments are the values supplied when the function is called. Return passes a result back. Print only displays it; a printed value cannot be reused like a returned value.

Prefer small functions with clear inputs and outputs. Avoid relying on hidden global state. A function should state what happens for empty or invalid input.

## Files and structured data

A program can read text or CSV data from storage. Use a context manager so a file is closed even if an error occurs. Paths should be handled with a path library rather than manually joining strings, especially across operating systems.

CSV stores rows and columns as text. Convert columns to appropriate types before arithmetic. Validate required headers and handle missing values.

## Exceptions

An exception signals an error that interrupts normal flow. Use try/except only around the operation that can fail and handle a specific exception type. Do not silently catch every error and continue; that can hide data corruption.

Use errors for invalid conditions with a clear message. For example, averaging an empty list is undefined unless your application specifies a convention.

## Modules and packages

A module is a Python file that defines reusable functions and values. A package groups modules. Imports allow projects to reuse code. Keep a project organized by purpose, not by the number of files. Avoid naming your file after a standard library module because it can shadow the real module.

## Questions and answers

**Why return a value instead of printing it?**  
Returning makes the result available to other code and easier to test. Printing is an output side effect.

**When should a function raise an error?**  
When its inputs violate a documented requirement and the caller should decide how to handle the failure.

**Why use context managers for files?**  
They ensure resources are released reliably, even if code fails partway through reading or writing.

**Why avoid a broad exception handler?**  
It can swallow programming bugs and let invalid results continue through the system.

## Practice

Write a CSV reader that verifies required columns, converts scores to numbers, and reports row numbers with invalid data. Put parsing in one function and summary calculation in another. Test missing files, missing columns, empty files, and malformed rows.

## Mastery check

Explain the difference between a parameter, argument, return value, printed output, and exception. Build a function that behaves deliberately on invalid input.