# Lesson 12 — Production, safety, and responsible AI

## Learning goals

Understand why a model is part of a larger system, how behavior changes after release, and what responsible maintenance requires.

## From notebook to product

A notebook proves that an experiment can run in one environment. A production service must also handle input validation, authentication, latency, failures, updates, privacy, and user experience.

A typical architecture has:
- an interface that collects input and explains the output;
- a service that validates requests and applies policy;
- a model or API call;
- data stores and retrieval systems, if needed;
- logs and metrics;
- fallback or human review paths.

Keep components replaceable. Avoid embedding business rules inside opaque model prompts when explicit code can enforce them.

## Reliability and monitoring

Monitor both software health and model behavior:
- request volume, latency, errors, and cost;
- input distribution and missing fields;
- prediction confidence and output quality;
- user corrections, complaints, and overrides;
- outcomes across time and relevant groups.

**Data drift** means input patterns change. **Concept drift** means the relationship between inputs and targets changes. A pipeline can remain operational while its predictions become less useful.

Set alert thresholds and define what action follows each alert. Monitoring without a response process is only a dashboard.

## Human oversight and user experience

Tell users when AI is involved, what the output can and cannot do, and how to correct or appeal it. The more consequential the decision, the stronger the need for review, explanation, audit records, and a non-AI fallback.

A human in the loop is not automatically safe. Reviewers need time, training, authority to disagree, and enough information to catch model errors rather than rubber-stamp them.

## Privacy, security, and data rights

Use only data you have a lawful and appropriate basis to process. Minimize collection. Protect access. Define retention and deletion. Do not place credentials or sensitive data into prompts or logs without a justified, protected design.

Consider threats such as prompt injection, data exfiltration, model inversion, membership inference, poisoning, and unauthorized tool actions. Security testing should reflect the actual system and adversary.

Respect dataset and model licenses. Record provenance and restrictions before building, not after launch.

## Fairness and impact

Historical data may encode unequal access or past harmful decisions. Accuracy averages can hide subgroup harms. Ask who benefits, who bears errors, who was excluded from the data, and who can challenge the system.

Fairness is not one metric that solves every conflict. Choose evaluation and governance based on the decision, applicable requirements, affected communities, and available evidence. Document tradeoffs.

## Lifecycle review

Before release:
- define allowed and disallowed use;
- test normal, edge, adversarial, and out-of-distribution inputs;
- assess privacy and security;
- verify fallback behavior;
- prepare user-facing explanations;
- define an owner and incident process.

After release:
- monitor actual inputs and outcomes;
- investigate unexpected failures;
- roll back or disable the feature when needed;
- update data and models through controlled versions;
- communicate material changes;
- retire the system when benefit no longer justifies cost or risk.

## Review questions with answers

**1. Why is a model score in a notebook not enough for deployment?**  
A product also needs reliable data handling, access control, latency, monitoring, user communication, failure handling, and a process for updates.

**2. What is the difference between data drift and concept drift?**  
Data drift is a change in inputs. Concept drift is a change in how inputs relate to the target. Either can make a previously useful model fail.

**3. Does human review automatically make a system safe?**  
No. People need time, training, authority, and relevant evidence. Otherwise they may over-trust automation or fail to detect errors.

**4. Why minimize logged data?**  
Logs can create privacy and security risks. Collect only what is needed for operations, debugging, or audits, and protect it appropriately.

**5. When should a system be disabled?**  
When observed harm, severe failures, compromised security, invalid data, or loss of benefit exceeds the accepted threshold. Define owners and triggers before launch.

## Practice

Write a one-page deployment checklist for your capstone. Include intended users, prohibited use, data handling, monitoring, fallback, human review, incident owner, and rollback plan.

## Mastery check

A responsible AI project has an owner, evidence of evaluation, documented boundaries, a way to report problems, and a plan to respond when the real world differs from the training data.