---
title: "How LLMs Think"
date: 2026-09-30
draft: true
categories: ["concept-breakdown"]
tags: ["generative ai", "large language models", "machine learning", "classroom conversation"]
summary: "Hint: it's just Antakshari. How a large language model writes an answer, one token at a time."
description: "How do LLMs like ChatGPT think? A comic breakdown using Antakshari to explain next-token prediction, and why it matters for product managers."
url: /concept-breakdown/how-llms-think/
images: ["cover.jpg"]
slide_alt:
  - "Teacher reminds students of Antakshari, where each song starts with the last letter of the previous one; nobody plans ahead"
  - "Teacher explains an LLM picks the next token based on what came before, with no plan or destination"
  - "Teacher calls an LLM a superhuman Antakshari player; student sums it up as a next-word prediction engine"
  - "Takeaway: an LLM doesn't plan answers. It predicts the next token, again and again"
---

{{< carousel >}}

## What's happening in this comic

<!-- CHECK: transcribed from the slides (no transcript.txt was provided); please verify the wording. -->

**Slide 1: Remember Antakshari?**

**Teacher:** Remember playing Antakshari at family functions? The next song starts with the last letter of the previous one.  
**Student:** Ha, yes! Someone sings "…gaata hoon," and the next person scrambles for a song starting with "N."  
**Teacher:** Notice, nobody plans the whole session in advance. Each person looks at the last sound and picks the best next song they know.  
**Student 2:** True. Nobody says "I have a 10-song strategy." It's one move at a time.

**Slide 2: One move at a time**

**Teacher:** That one move, picking the next best song based on what came before, is exactly what an LLM does. Only its unit isn't a song, it's a word. Actually, even smaller: a piece of a word, called a token.  
**Student:** Wait, so it's not "thinking" of the full answer first and then writing it out?  
**Teacher:** No plan, no destination. It looks at everything said so far, asks "what usually comes next?", and picks that.  
**Student 2:** So if I ask it to write an email, it's not thinking "here's my conclusion, let me build up to it"?

**Slide 3: A superhuman Antakshari player**

**Teacher:** Exactly. It's a very, very good Antakshari player who has heard almost every song ever sung, and instinctively knows what fits next. One word at a time, until the email is done.  
**Student:** That's humbling. It feels intelligent because each move is impressively good, not because there's a grand plan.  
**Teacher:** So in your own words, what's an LLM, really?  
**Student 2:** It's a next-word prediction engine. Not a chess player thinking ahead, just Antakshari at superhuman level, one word after another.

**Slide 4: The whole trick**

**Teacher:** That's the whole trick. No goal, no plan, just really, really good next-move prediction, repeated until it looks like thought.  
**Takeaway:** An LLM doesn't plan answers. It predicts the next token, again and again.

## The concept in plain words

A **large language model (LLM)**, the technology behind ChatGPT, Claude and Gemini, does one thing: given
some text, it predicts what piece of text most likely comes next. That piece is called a **token**,
usually a word or part of a word ("unbelievable" might be split into "un", "believ", "able").

When you ask it a question, it predicts one token, adds it to the text, and then predicts the next one
using everything written so far, including what it just wrote. It repeats this hundreds of times until
the answer is complete. That's the Antakshari loop: look at what came before, pick the best next move,
repeat.

Why does it pick good moves? Because it was trained on an enormous amount of text: books, websites,
code, conversations. Like the Antakshari player who has "heard almost every song", it has seen so many
patterns that its next guess is usually very good.

Where the analogy stretches: an LLM doesn't only look at the last word. It looks at the *entire*
conversation each time, which is why context matters so much. And "no plan" is a simplification:
research shows models can internally anticipate a few words ahead (for example, choosing a rhyme before
writing the line). But the output is still produced one token at a time, and nothing checks the answer
against a goal before it's written. <!-- CHECK: nuance added beyond the comic; keep or cut? -->

## Why this matters for PMs

If you build products with LLMs, this one idea explains a lot of their behaviour:

- **Same question, different answers.** Each token is picked from likely options, so outputs vary. Plan
  for it: set temperature deliberately, and don't promise identical responses.
- **Confidently wrong ("hallucinations").** The model optimises for "what sounds like it comes next", not
  "what's true". For facts that matter, ground it with your own data (retrieval) and show sources.
- **Context is the product.** Since every token depends on what came before, the prompt, instructions and
  examples you feed it shape quality more than almost anything else. Treat prompts like product specs.
- **Evaluate outputs, not intentions.** There's no hidden plan to inspect, so quality comes from testing
  lots of real outputs (evals), not from trusting how smart the answer sounds.

## Key takeaways

- An LLM writes by predicting the next token, one at a time, based on everything so far.
- It feels intelligent because each prediction is very good, not because it planned the whole answer.
- For products, this explains variability, hallucinations and why context and evals matter so much.

## FAQ

### Do LLMs like ChatGPT think before they answer?

Not in the way people do. An LLM generates its answer one token at a time, each time predicting what's
most likely to come next given the conversation so far. Newer "reasoning" models first write out
intermediate steps, but those steps are produced the same way: token by token.

### What is a token in an LLM?

A token is the unit of text an LLM reads and writes: often a whole word, sometimes part of a word,
a number or a punctuation mark. As a rough rule, 100 tokens is about 75 English words. Pricing, speed
and context limits for LLMs are all measured in tokens.

### Why do LLMs make things up?

Because they're trained to produce text that plausibly comes next, not to check facts. If the most
"natural-sounding" continuation is wrong, the model will write it just as fluently. Grounding answers in
trusted sources and testing outputs are the standard ways to reduce this.

**Related breakdowns:** [What is Natural Language Processing](/concept-breakdown/what-is-nlp/) · [What is Deep Learning and Neural Network](/concept-breakdown/what-is-deeplearning-and-neuralnetwork/) · [What is Transfer Learning](/concept-breakdown/what-is-transferlearning/)
