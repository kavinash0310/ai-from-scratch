# Python and software foundations — full beginner notes

Python is the first language in this course because its readable syntax lets you focus on ideas. Learn to reason about values and programs before adding machine-learning libraries.

## 1. First program, values, and types

A **program** is precise instructions. The Python **interpreter** reads source code and executes it. A **statement** performs an action; an **expression** computes a value. In the calculation total = price * count, multiplication is an expression and assignment stores its result under the name total.

A **value** is data such as 3, 2.5, “cat”, or True. A **variable** is a name that refers to a value. A **type** describes the kind of value and operations it supports: int for whole numbers, float for approximate decimal numbers, str for text, and bool for True/False.

    name = input("Name: ")
    year = int(input("Birth year: "))
    print("Hello", name)
    print("Approximate age:", 2026 - year)

input returns text even when digits are typed. int converts compatible text to an integer; invalid text raises an exception. The assignment symbol = stores a value; == compares two values. Names should explain meaning, such as number_of_rows.

**Type conversion** changes representation; it does not verify that input makes sense. A year of 9000 converts to an integer but is still invalid for most age calculations. Validate both type and allowed range. **Mutability** describes whether an object can change in place; lists are mutable while strings and tuples are immutable. This matters when two names refer to the same list.

Worked check: if price is 12.5 and count is 3, price times count is 37.5. If count comes from input, convert it before multiplying. Test zero, negative values, and non-numeric input.

## 2. Conditions, loops, and collections

A **condition** is an expression whose truth value chooses a path. if, elif, and else express ordered cases. A **loop** repeats work: for iterates over items; while repeats as long as a condition remains true. A loop needs a stopping condition to avoid running forever.

A **list** is an ordered, changeable sequence; an index starts at zero. A **tuple** is an ordered sequence typically used for fixed groupings. A **dictionary** maps keys to values; a **set** stores unique members. Choose a collection based on the operation: list for order, dictionary for lookup by name, set for membership and uniqueness.

    scores = [80, 95, 70]
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)

The **loop invariant** here is that after each item, total equals the sum of items seen so far. Thinking about invariants helps debug loops. range(n) produces integers from 0 through n-1. An **off-by-one error** includes too few or too many values because a boundary was misunderstood.

An **index** means a position; a **slice** selects a range; **iteration** visits values one by one; **membership** asks whether a value is present. Dictionary lookup can fail when a key is absent; validate it or use a safe lookup when absence is expected. Avoid changing the collection in a way that breaks the loop traversing it.

## 3. Functions, files, and errors

A **function** packages a named computation. **Parameters** are input names in its definition; **arguments** are actual values passed in. A **return value** sends a result back to the caller. print displays information; it is not a substitute for returning a value.

    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32

    boiling = celsius_to_fahrenheit(100)

A good function has one clear responsibility, meaningful inputs, and predictable output. **Scope** is where a name can be used. Prefer passing values as parameters over relying on hidden global state.

A **file** stores information beyond one program run. A context manager ensures it closes even if an error occurs. Specify text encoding for reliable text handling. CSV stores tabular rows; JSON stores structured values. Use proper parsers instead of splitting on commas when quoted commas may appear.

An **exception** signals that an operation failed. try/except should handle errors you can meaningfully recover from. Do not catch every exception and silently continue: that hides defects. A **syntax error** means code cannot be parsed; a **runtime error** means an operation fails; a **logic error** means the program runs but returns the wrong result.

## 4. Algorithms, testing, and debugging

An **algorithm** is a finite procedure for solving a problem. A **test** checks expected behavior for selected inputs. Include normal cases, boundary cases, and invalid cases. A **unit test** checks a small component; an **integration test** checks components working together. Assertions express conditions that should hold.

Debug with a repeatable process: reproduce the issue, isolate the smallest failing input, inspect the traceback and variable values, state the expected result, then change one thing. A **traceback** shows the call chain and where an exception occurred. A **regression** is previously working behavior that breaks after a change.

**Complexity** describes how resource use grows with input size. One loop over n values is roughly O(n); two nested loops may be O(n²). These describe growth, not exact seconds. Ensure correctness and measure before optimizing.

Example: test a maximum-finding function using [4, 2, 9], a one-item list, repeated maximums, and an empty list. Decide the empty-input behavior rather than letting it be accidental.

## 5. Git, environments, SQL, and APIs

**Git** records project history as commits. A repository holds tracked files and history; a branch is a movable line of development; a commit is a snapshot with a message. git status tells what changed, git diff shows changes, and a commit records a deliberate unit. Git is not the same as GitHub: Git is version control; GitHub hosts repositories and collaboration features.

A **virtual environment** isolates project dependencies so package versions do not silently conflict. A **package** is reusable code; a **dependency** is a package a project needs. Record dependencies and setup steps so another learner can recreate the environment.

**SQL** queries relational tables. A row is a record and a column is a field. SELECT chooses columns, WHERE filters rows, GROUP BY aggregates groups, and JOIN connects related tables. Parameterized queries keep user values separate from SQL syntax and prevent injection.

An **API** is a defined way for programs to communicate. An HTTP request has a method, address, headers, and sometimes a body; a response has a status code and content. Handle timeouts, errors, authentication, and rate limits. Never commit passwords or API keys; use environment variables or a secret manager.

## Q&A and project

**Why does Python use indentation?** Indentation marks blocks and changes program structure.
**Why separate functions?** They make behavior reusable, testable, and easier to name.
**Why do tests need edge cases?** Bugs often hide at boundaries such as empty input, one item, or invalid values.
**What should a beginner build?** A command-line expense tracker that validates input, stores records in CSV or JSON, has tests, and is tracked with Git.

Mastery: implement that project without copying a tutorial; explain each collection, function, error path, test, and Git commit. Continue to [mathematics](../mathematics/README.md).