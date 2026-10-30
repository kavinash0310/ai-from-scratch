# Chapter 2 — Logic, knowledge, and constraints

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## Represent facts explicitly

Propositional logic represents statements that are true or false. AND, OR, and NOT combine statements. An implication such as “if it rains, the ground is wet” represents a rule. Inference applies rules to known facts to derive conclusions.

First-order logic adds objects, relations, and quantifiers. It can express that every student has an ID or that a particular person owns a particular book. More expressive representations can be harder to reason with computationally.

Knowledge representation is a design choice. A fact database, rule set, ontology, or graph each makes some queries easy and others awkward. The representation should match questions users need answered.

## Constraint satisfaction problems

A constraint satisfaction problem (CSP) has:
- variables;
- a domain of allowed values for each variable;
- constraints that restrict combinations.

Scheduling is an example: variables are events, domains are time slots, and constraints prevent a person from attending two events at once.

Backtracking assigns a value, checks constraints, and reverses a choice when it creates a conflict. Heuristics can improve search:
- choose the variable with the fewest legal values;
- try values that constrain other variables least;
- propagate constraints before making more choices.

## Rules versus learning

Rules are useful when policies are explicit, stable, and must be auditable. Learned models are useful when patterns are hard to specify. Rule systems can become brittle as exceptions accumulate; learned systems can reproduce data bias or fail on new conditions. A hybrid can use a learned score but a hard rule to enforce permission.

## Questions and answers

**What is an inference rule?**  
A logical step that derives a conclusion from premises under a formal system.

**Why do CSP heuristics help?**  
They expose conflicts early and reduce the number of assignments that must be explored.

**Can a rule system be biased?**  
Yes. Rules can encode unfair assumptions or apply unevenly. Explicit logic does not automatically mean neutral logic.

**Why combine rules with ML?**  
Use ML for uncertain estimates and rules for explicit constraints, with clear boundaries and an evaluation plan.

## Practice and mastery

Model a simple weekly timetable as a CSP. List variables, value domains, and constraints. Solve it manually for a tiny example, then write a backtracking solver. Explain what happens when no valid assignment exists.