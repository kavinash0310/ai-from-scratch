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

## Deeper software habits for machine learning

A function should have one clear job, named inputs, and a predictable return value. Printing is a side effect; returning a result allows other code to reuse it and tests to inspect it. Keep side effects such as file access, network calls, and user prompts near the outer edge of a program. A module groups reusable names in a file; importing it should not unexpectedly start training or download data.

Inspect data before analyzing it. Check row counts, column names, types, missing values, duplicates, ranges, and representative examples. Missing is not the same as zero: zero may be a genuine measurement. A numeric-looking string may fail in arithmetic. Record what each field means and when it becomes available. For ML, a transformation that learns statistics, such as scaling or imputation, must be fit on training data only and then reused on validation and test data.

Big-O describes how computational work grows with input size. A single pass over n records is O(n); comparing every pair is commonly O(n squared). It is not a stopwatch and does not replace measurement, but it helps identify algorithms that will become impractical as datasets grow. First build a clear correct version, then profile representative inputs and optimize the actual bottleneck.

A traceback identifies the exception and the calls that led to it. Reduce a failure to the smallest input that still reproduces it. Test boundaries: empty input, one item, duplicates, missing fields, malformed values, and exact threshold values. A unit test checks a small function; an integration test checks components together; a regression test preserves a previously fixed failure.

A random seed helps repeat randomized experiments but does not promise identical results across versions, hardware, parallel kernels, or all GPU operations. Record code revision, data version, library versions, configuration, and seed. Git records source changes; a virtual environment isolates package dependencies; neither automatically versions large private datasets or model artifacts.

Questions: Why use a virtual environment? It limits dependency conflicts between projects. Why inspect array shapes? The dimensions encode which axis represents examples, features, channels, or time, and a shape error can produce a wrong result without crashing. Why handle API timeouts? Remote services can fail, respond slowly, rate-limit, or change schemas; production code must handle these states explicitly.

Practice: write a function that summarizes a list of records. State what it does with missing and malformed values. Test empty input, a valid record, duplicates, a missing value, and invalid type. Explain why each result is correct.

Further reading: [Python tutorial](https://docs.python.org/3/tutorial/) and [Python Packaging User Guide](https://packaging.python.org/en/latest/).

## 16. A small data-analysis workflow

A trustworthy script separates reading, validation, transformation, computation, and reporting. First check that the file exists and has expected columns. Next validate types and ranges. Then handle missing values according to a documented rule. Keep the transformation code reusable and fit any learned transformation only on training data.

For a CSV of measurements, a defensible workflow might: read the file; print row count and column types; count missing values; reject impossible negative measurements; split by time or subject as appropriate; fit a median imputer and scaler on training rows; apply them to the other partitions; save the split identifiers and configuration. Each step should be inspectable. A notebook is useful for exploration, but long-running work should eventually be placed in functions or scripts with clear inputs and outputs.

## 17. Notebooks, environments, and reproducibility

A notebook combines executable cells and narrative. Its hidden state can mislead: running cell 8 before cell 3 may use stale variables. Restart the kernel and run all cells from top to bottom before sharing. Clear secrets and avoid logging personal data. Store a short README with environment setup, data acquisition, and the exact command to reproduce an output.

A dependency file records package names and versions. A virtual environment isolates project dependencies. Git tracks source and configuration changes. Large datasets or checkpoints may need external artifact storage and explicit version identifiers. Save a small manifest connecting the model output to source revision, data version, configuration, environment, and random seed.

## 18. Testing a preprocessing function

Suppose a function converts a list of raw ages into normalized numeric values. Test a known list and verify the expected result; test a missing age and verify the declared policy; test a negative age and verify rejection or reporting; test a constant list and guard against division by zero; test empty input. These cases reveal assumptions that a happy-path example hides.

Property-based checks can assert general rules: output length equals the number of accepted records, all normalized values are finite, and accepted values remain within the documented range. A type hint helps communicate expected inputs but does not validate them at runtime. Clear error messages matter because datasets often contain unexpected values.

## 19. Debugging a training script as software

When a loss is NaN, inspect input values, target encoding, learning rate, and intermediate activations. When predictions have the wrong shape, print tensor dimensions at each boundary. When evaluation is suspiciously perfect, check duplicates, target leakage, train-test overlap, and preprocessing order. When a run changes unexpectedly, check environment and configuration before rewriting the algorithm.

Questions: Why avoid changing five things at once? You will not know which change affected the result. Why version configuration? A code commit alone does not identify learning rate, batch size, split, or model choice. Why keep a script deterministic where feasible? It makes debugging and comparison easier, while recognizing hardware can still change exact results.

Practice: create a command-line program that reads a small CSV, validates required columns, calculates one summary, and returns a useful error if data is invalid. Add tests for valid, empty, and malformed files.

Further reading: [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html) and [Jupyter notebook format](https://nbformat.readthedocs.io/en/latest/).
