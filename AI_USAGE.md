# AI Usage

I used ChatGPT as an AI assistant while working on this assignment.

I did not directly use all the generated code without checking it. I used the AI mainly to understand problems, check my code and get ideas for implementation.

## AI Tool Used

- ChatGPT

## What I Used AI For

I used ChatGPT for:

- Understanding the assignment
- Understanding Django models
- Checking my Django code
- Understanding product dimensions and box dimensions
- Understanding different product orientations
- Finding problems in my code
- Getting ideas for test cases
- Understanding validation
- Understanding Django transactions
- Checking the project structure

## Example Prompts

Some of the prompts I used were similar to:

```text
Check my models and tell me if they are correct for this assignment.

Check my box selection function and tell me what problems are there.

How can I check if a product can fit inside a box?

How can I test different product orientations?

What test cases should I make for this box selection project?
```

## Output I Accepted

I used some suggestions from the AI after understanding them.

For example, I used ideas related to:

- Checking box weight
- Checking product dimensions
- Checking different orientations
- Adding validation
- Adding test cases
- Handling an order which does not exist

I changed some code instead of directly copying everything because I wanted to understand how it works.

## Output I Modified or Rejected

I did not use every code suggestion directly.

I modified code when it did not match my project structure or coding style.

I also checked the code myself before adding it to the project.

**Note:** I will add my actual examples of rejected or modified AI output here before submission.

## Mistakes Found While Using AI

One important problem I found during checking was that checking only the total volume is not enough.

For example, a product can have enough total volume for a box but still not physically fit because one dimension can be bigger than the corresponding box dimension.

I also found that quantity needs to be included when calculating total weight and volume.

**I will add any other mistakes that I personally found while working on the project.**

## How I Verified the Code

I verified the code by:

- Running the Django project
- Sending API requests
- Creating products
- Creating boxes
- Creating orders
- Testing box recommendation
- Running Django tests

The actual test output is available in:

```text
TEST_OUTPUT.md
```
