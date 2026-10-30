# Chapter 5 — Git, environments, SQL, and APIs

> **Book-length subject volume:** For expanded explanations, worked examples, review questions, and practice, read the [python textbook](TEXTBOOK.md).

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## Git records changes

A repository is a project with version history. A commit records a snapshot and a message. A branch is a movable line of work. GitHub hosts repositories and adds collaboration, issue tracking, and code review.

Make small commits after meaningful working steps. Review changed files before committing. Never add passwords, API keys, private records, or large model binaries to a public repository.

## Environments and packages

A package is reusable code installed into Python. Projects may require different package versions, so use an isolated virtual environment and record dependencies. Keep setup instructions in a README. Reproducibility means another person can rebuild the environment and obtain similar results.

An API is a defined way for one program to request data or actions from another. Learn HTTP basics: request, response, status code, JSON body, authentication, rate limits, and timeouts. Do not expose API keys in code or browser output.

## SQL basics

A relational database stores tables. A row is one record; a column is one attribute. A primary key uniquely identifies a row. A foreign key links records between tables.

    SELECT route, COUNT(*) AS shipment_count
    FROM shipments
    WHERE is_late = 1
    GROUP BY route
    ORDER BY shipment_count DESC;

This filters rows, groups by route, counts each group, then orders the results. JOIN combines related tables. Check whether a join multiplies rows unexpectedly.

## Questions and answers

**Why use Git if the code is already on my computer?**  
It records changes so you can compare versions, undo mistakes, and share reviewable work.

**Why isolate Python packages?**  
A library update in one project should not break another project that depends on a different version.

**What makes a safe API workflow?**  
Use secure secret storage, validate responses, handle errors and timeouts, respect limits, and request only the data the project needs.

**Why learn SQL as an AI learner?**  
Real datasets often live in databases. SQL lets you filter, join, and aggregate data efficiently and understand its structure.

## Practice

Create a repository for one Python project, write setup steps, save two commits, query a small database by category, and fetch one public JSON API while handling a failed response.

## Mastery check

You can explain commits, isolated environments, an API request/response, and a SQL query; your project can be recreated from its README.