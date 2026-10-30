# Python and software foundations
## A beginner's textbook chapter

Python is a practical first language for AI because its syntax is readable and its libraries support data work. Your goal is not to memorize every command. Your goal is to form a precise mental model of program execution, write small functions, inspect errors, and make projects reproducible.

## 1. How a computer runs a program

A program is a sequence of instructions. Python source is read by an interpreter, which parses statements and executes them. A statement performs an action; an expression computes a value. In:

    total = price * count

the multiplication is an expression. The assignment stores its result under the name total. The equals sign in an assignment is not a permanent mathematical claim; it binds a name to a value at that point in execution.

A **variable** is a name referring to a value. A **type** describes what kind of value it is and which operations are sensible. Common types are integers, floating-point numbers, strings, Boolean values, lists, dictionaries, and tuples.

    name = "Mina"
    age = 19
    height = 1.65
    is_learning = True

The type affects behavior. Adding 2 and 3 gives 5; joining "2" and "3" gives "23". The input function returns text even if the user types digits. Convert deliberately:

    typed_count = input("Count: ")
    count = int(typed_count)

Conversion can fail, and a converted value can still be unreasonable. An age of -50 is an integer but is not a valid age for most tasks. Validation checks type and allowed range.

**Mutable objects** can change in place. Lists and dictionaries are mutable; strings and tuples are not. If two names refer to the same list, changing it through one name is visible through the other. Copy a list when independent state is required.

## 2. Conditions and loops

A condition produces True or False. if, elif, and else choose which statements run. Conditions can combine comparisons with and, or, and not.

A for loop visits items in a collection. A while loop repeats as long as a condition is true. Every while loop needs an update and an exit condition. If the condition never becomes false, the loop is infinite.

    scores = [80, 95, 70]
    total = 0
    for score in scores:
        total += score

The **loop invariant** here is: after processing some items, total is the sum of the items processed so far. An invariant gives you a way to reason about correctness. An **off-by-one error** includes one too few or one too many items because the boundary was misunderstood. Python indexing begins at zero; range(4) yields 0, 1, 2, 3.

Use a for loop when a collection or number of iterations is known. Use while when iteration depends on a condition, such as repeatedly asking until input is valid. Avoid changing a list while looping over it unless you understand exactly how indices are affected.

## 3. Choose data structures by the job

- A **list** stores an ordered sequence you may change.
- A **tuple** stores a fixed ordered grouping.
- A **dictionary** maps unique keys to values.
- A **set** stores unique items and makes membership checks natural.

Suppose you count word frequencies. A dictionary is appropriate because the word is the key and the count is the value. A set is useful when you need to know whether a word has appeared already. A list keeps the original order.

A **function** names a reusable computation. Parameters are placeholders in a function definition; arguments are values passed when it is called. A return value sends a result back to the caller. print displays something to a person and does not replace a return value.

    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32

    boiling = celsius_to_fahrenheit(100)

A good function has one clear responsibility, explicit inputs, and a predictable result. **Scope** means where a name can be used. Passing dependencies as arguments is usually clearer than reading hidden global variables.

## 4. Files, formats, and errors

A file preserves information beyond one program run. Use a context manager so the file closes even if processing fails:

    with open("notes.txt", encoding="utf-8") as file:
        text = file.read()

**CSV** stores tabular rows. **JSON** stores nested values such as dictionaries and lists. Use a parser because commas, quotes, and newlines make manual splitting unreliable. Choose an encoding explicitly when working with text.

An **exception** signals a failed operation. Common categories:
- Syntax error: Python cannot parse the code form.
- Runtime error: an operation fails while the program runs.
- Logic error: code runs but computes the wrong result.

A traceback identifies the exception and call chain. Read it from the final error line upward, inspect the named file and line, and reproduce the smallest failing input. Catch exceptions only when you can take a meaningful recovery action. A broad catch that hides errors makes debugging harder.

## 5. Algorithms, complexity, and debugging

An **algorithm** is a finite procedure. A list search that checks each of n items has time complexity approximately O(n). Two nested loops over the same n items may be O(n²). Big-O describes how work grows, not the exact time in seconds. Data sizes and library implementation matter.

Debug systematically:
1. Reproduce the behavior.
2. State what should have happened.
3. Reduce the input to the smallest failing case.
4. Inspect intermediate values and shapes.
5. Change one thing.
6. Rerun the example and check for regressions.

A **test case** specifies an input and expected behavior. Think about normal, empty, boundary, and invalid inputs when you build your own projects. The repository labs show small examples; extend them with additional cases as a learning activity.

## 6. Git, environments, SQL, and APIs

**Git** records file history. A repository contains tracked files and commits. A branch is a movable line of development; a commit is a named snapshot. git status shows changed files, git diff shows content differences, and git log shows earlier snapshots. Git is a tool; GitHub is a service that hosts repositories and collaboration features.

A **virtual environment** isolates package versions for a project. This prevents one project upgrade from unexpectedly breaking another. Record setup commands and dependencies in a README.

**SQL** queries relational tables. Rows are records; columns are fields. SELECT chooses columns, WHERE filters rows, GROUP BY summarizes groups, and JOIN relates tables. Use placeholders for user-provided values instead of concatenating strings into a query; this keeps data separate from SQL commands.

An **API** defines how software requests information or actions from another service. An HTTP request has a method, endpoint, headers, and often a body. A response has a status and content. Programs should handle timeouts, non-success status codes, rate limits, and malformed responses. Never commit credentials to Git; use environment variables or secret storage.

## 7. Worked example: a command-line expense summary

Imagine a user enters three purchases. A useful program needs to:
1. represent each purchase as a record with item, quantity, and price;
2. validate that quantity is positive and price is nonnegative;
3. compute each line total;
4. accumulate the grand total;
5. save records in a file;
6. handle empty files and malformed entries;
7. expose a function that can be reused by another program.

Start with one valid record, then several records, then empty input, then invalid values. This small sequence teaches types, collections, functions, loops, files, and exceptions together. Keep the calculation separate from print statements so it can be reused.

## 8. Questions and answers

**Why does Python use indentation?** Indentation marks blocks, so it changes which statements belong to a condition, loop, or function.

**Should I memorize every syntax rule?** Learn common patterns. Use documentation and small examples for exact details. Being able to debug and verify code is more useful than memorizing a list.

**Why can input conversion fail?** The user can type text that does not represent the requested number. Validate and explain the expected format.

**Why write functions if a script runs without them?** Functions let you name, reuse, and reason about a behavior separately.

**Why use Git before a project is large?** Small commits make it easier to identify when a mistake was introduced and preserve working states.

## 9. Exercises with worked answers

**Exercise A:** Write a function that receives a list of numbers and returns its average. What should happen for an empty list?

**Worked answer:** Sum the list and divide by its length for a nonempty list. For empty input, choose and document a behavior: raise a clear ValueError or return a special result. Do not divide by zero accidentally.

**Exercise B:** A CSV row has quantity "three". Why does integer conversion fail?

**Worked answer:** The string does not represent a base-10 integer. Catch the specific conversion error at the input boundary and ask for a valid count; do not silently replace it with zero.

**Exercise C:** Why store lookup data in a dictionary instead of scanning a list of pairs?

**Worked answer:** A dictionary directly maps keys to values and is designed for efficient key lookup. A list can be better when order or duplicate keys matter.

## 10. Mastery target

Build a command-line expense tracker with functions, validated input, file persistence, readable errors, a README, and Git history. Explain each data structure and failure path. Continue to [mathematics](../mathematics/README.md) and the [Python labs](../../labs/README.md).