# Part 1 — Computing, programming languages, and Python

## Chapter 3 — How a computer runs a program

A computer stores data in memory and executes operations through a processor. A program is a precise sequence of instructions. Files persist on storage; variables usually exist in a running program's memory. A process is a running program with its own working state.

The operating system manages files, applications, memory, and devices. A terminal is a text interface for asking the operating system to run commands. A code editor helps write files; the terminal runs them. A browser notebook combines code, output, and notes in one document.

An environment is the set of installed language and library versions used by a project. Separate environments reduce conflicts: one project may need a different version of a library than another. Record setup steps so a future reader can reproduce the work.

## Chapter 4 — Python as the first AI language

Python is the recommended first language because it is readable and has broad data and AI libraries. Learn these ideas in order:

1. values, variables, types, input, and output;
2. conditions and Boolean expressions;
3. loops and collections;
4. functions, parameters, return values, and scope;
5. files, exceptions, imports, and packages;
6. classes when they clarify a real program;
7. testing, debugging, and documentation.

A program is data moving through operations. For a small grade calculator, inputs are scores, the transformation is an average, and output is a result. Writing this flow in plain language before code prevents syntax from hiding a misunderstood task.

A list stores a sequence. A dictionary maps keys to values. A set stores unique elements. A function creates a named operation with an explicit boundary. These basic structures are enough to begin manipulating small datasets.

Example idea: a function receives a list of scores, rejects an empty list, sums the scores, and divides by their count. Test both an ordinary list and an empty list. Good code makes its assumptions visible.

## Chapter 5 — Computational thinking and algorithms

An algorithm is a finite procedure for solving a problem. For each problem, identify:
- input;
- output;
- allowed operations;
- edge cases;
- correctness condition;
- resource limits.

A linear search checks items one by one and takes work proportional to the list length. Binary search repeatedly halves a sorted range and takes roughly logarithmic work, but it requires sorted input. The faster method is not valid unless its assumptions hold.

A data structure changes the cost of operations. A list supports ordered access; a hash map often supports fast key lookup; a queue supports first-in-first-out work; a stack supports last-in-first-out work. Choose structures based on operations the program performs.

## Chapter 6 — Git, GitHub, and collaboration

Git records snapshots of file changes. A commit should describe a small meaningful change. A branch allows parallel changes. A pull request makes changes reviewable before merging. GitHub hosts repositories and adds collaboration features.

Save a commit after a working milestone. Before committing, inspect which files changed. Do not store credentials, private datasets, or huge generated model files in a public repository. Add a README describing purpose, setup, result, and limits.

## Chapter 7 — SQL and working with data

SQL is a language for selecting, joining, grouping, and updating structured data in relational databases. Python can load a CSV, but a database helps when data are large, shared, or queried repeatedly.

A table has rows and columns. A primary key identifies a row. A foreign key connects rows in related tables. A SELECT query asks for specific columns and rows. A JOIN combines records using a relationship. GROUP BY summarizes many rows by a category.

    SELECT route, AVG(delivery_minutes) AS average_minutes
    FROM shipments
    WHERE shipment_date >= '2026-01-01'
    GROUP BY route;

The query filters to a time period, groups by route, then averages delivery time. Always ask whether missing records or duplicate joins change the meaning.

## Which language should I learn?

- **Python:** first choice for AI development, data, experiments, and model application.
- **SQL:** essential when examples live in databases.
- **Shell:** useful for running tools and managing files/environments.
- **JavaScript or TypeScript:** helpful for building interactive web interfaces.
- **C/C++:** useful for performance-critical systems, embedded devices, robotics, or understanding lower-level computation.
- **R:** useful in some statistics-heavy communities; optional for this path.

Learn Python well before adding languages. The concepts transfer, but syntax does not.

## Q&A

**Why use Python if libraries do most of the model math?**  
Libraries do numerical work efficiently, but you must understand data flow, types, errors, APIs, and evaluation to use them safely.

**Is a notebook a replacement for a software project?**  
It is a good learning and exploration tool. A reusable application also needs organized modules, setup instructions, error handling, and tests or checks.

**What is Big O?**  
A way to describe how computation or memory grows with input size. It helps compare algorithms as data grows, while real runtime still depends on implementation and hardware.

**Why learn SQL if I know pandas?**  
Data often resides in relational databases. SQL lets you filter and aggregate close to the source, and helps you understand how rows and relationships are structured.

**Should I learn C++ before AI?**  
No. It is optional for most beginner ML work. Start with Python; learn C++ when your specialization or performance needs justify it.