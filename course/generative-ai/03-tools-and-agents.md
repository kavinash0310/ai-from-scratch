# Chapter 3 — Tools, function calling, and agents

## A tool call is a software contract

A model may request a search, calculator, or database operation. The host application validates the requested tool and arguments, executes it under permissions, and returns a result. The model proposes; the application decides what is allowed.

Define tool schemas narrowly. Validate types, ranges, user authorization, and side effects. Treat tool output as untrusted data and handle timeouts or partial failures.

## Agent loops

An agent often repeats:
- observe task and state;
- select an action;
- call a tool;
- inspect result;
- choose the next action or stop.

This loop adds flexibility and failure paths. A model can misread instructions, repeat calls, exceed budget, or attempt unintended actions. Limit steps, time, tool access, and spend. Log decisions. Require explicit user approval for consequential actions such as sending, buying, deleting, or changing access.

## Prefer deterministic workflows where possible

If the sequence is known, ordinary code is easier to test and secure. Use an agent when dynamic choice across tools adds clear value. Do not label a multi-step script an agent merely for marketing.

## Questions and answers

**Why shouldn't a model execute arbitrary code?**  
It expands the attack surface and can expose data or change the system. Use isolated, permission-limited tools designed for the task.

**What is least privilege?**  
Give each component only the access necessary for its job. Narrow tools reduce the potential impact of model mistakes or hostile input.

**Why set a step limit?**  
To stop loops, control cost, and preserve a clear failure path.

**When is human approval needed?**  
For actions with material external consequences or irreversible changes. The approval must show the exact action and target.

## Practice and mastery

Build an agent with one read-only tool and a maximum of three steps. Test invalid arguments, tool errors, malicious content, and a request that needs no tool. Add approval gates before any state-changing action.