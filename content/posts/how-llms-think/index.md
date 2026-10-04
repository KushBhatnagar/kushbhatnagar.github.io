---
title: "How LLMs Think"
date: 2026-10-04
categories: ["concept-breakdown"]
tags: ["generative ai", "large language models", "machine learning", "classroom conversation"]
summary: "Hint: it's just Antakshari. How a large language model writes an answer, one token at a time."
description: "How do LLMs like ChatGPT think? A comic breakdown using Antakshari to explain next-token prediction, simply, for product people."
url: /concept-breakdown/how-llms-think/
images: ["cover.jpg"]
ShowToc: false
slide_alt:
  - "Teacher reminds students of Antakshari, where each song starts with the last letter of the previous one; nobody plans ahead"
  - "Teacher explains an LLM picks the next token based on what came before, with no plan or destination"
  - "Teacher calls an LLM a superhuman Antakshari player; student sums it up as a next-word prediction engine"
  - "Takeaway: an LLM doesn't plan answers. It predicts the next token, again and again"
---

{{< carousel >}}

<!-- CHECK: transcript read from the slides (no transcript.txt was provided); please verify the wording. -->
{{< transcript >}}
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
{{< /transcript >}}

## The concept in plain words

A **large language model (LLM)**, the technology behind ChatGPT, Claude and Gemini, does one thing:
given some text, it predicts the piece of text most likely to come next. That piece is a **token**,
usually a word or part of a word.

When you ask a question, it predicts one token, adds it to the text, and predicts the next one using
everything written so far. It repeats this hundreds of times until the answer is done. That's the
Antakshari loop: look at what came before, pick the best next move, repeat.

Its moves are good because it was trained on an enormous amount of text. Like the player who has
"heard almost every song", it has seen so many patterns that its next guess is usually right.

One difference from Antakshari: an LLM doesn't just look at the last word, it rereads the *whole*
conversation every time. That's why the context you give it matters so much.
