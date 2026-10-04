---
title: "Training an AI for one skill quietly changes its other answers"
date: 2026-10-04
categories: ["learning-notes"]
tags: ["generative ai", "large language models"]
url: /learning-notes/training-an-ai-for-one-skill-changes-its-other-answers/
summary: "Post-training a model for one skill nudges its answers on unrelated questions, and that changes how I think about protecting models from copying."
description: "A learning note on the paper 'Post-Training Leaves Behavioral Shadows on Unrelated Decisions': training an AI for one skill shifts its other answers too."
source: "Post-Training Leaves Behavioral Shadows on Unrelated Decisions"
source_url: https://arxiv.org/abs/2609.29233
source_type: paper
ShowToc: false
---

**TL;DR:** Training an AI model for one skill also shifts its choices slightly on unrelated questions, which makes me think hiding a model's reasoning is one layer of protection against copying, not the whole wall.

## The source

A 2026 research paper (a preprint, not yet peer reviewed) by Ziyang Zhang and colleagues, listed on Hugging Face under Peking University: [Post-Training Leaves Behavioral Shadows on Unrelated Decisions](https://arxiv.org/abs/2609.29233).

## The idea, in my words

When you take a public base model and post-train it for one skill, such as coding, the change doesn't stay inside that skill. The model's choices also shift slightly on questions that have nothing to do with it. The paper suggests those small shifts can be picked up by another model that starts from the same base, and that they carry part of the skill with them. The authors call it a low-bandwidth channel: it works between models that share a base, and the gains they report are modest.

## What I took from it

Hiding a model's reasoning may be one layer of protection against copying, not the full boundary. Small signals may leak through off-topic answers, at least between models that share a base. For anyone building on the same few open models, that's a reminder that "what a model learned, and from whom" is harder to pin down than it looks.

## What I'm still unsure about

Does this matter between models that *don't* share a base? The paper's results are on small models, so I don't know yet how much of this carries over to the frontier models people actually use.

## Further reading

- [The paper on arXiv](https://arxiv.org/abs/2609.29233): the method and the results.
- [The paper's page on Hugging Face](https://huggingface.co/papers/2609.29233): community discussion.
- [Subliminal Learning (Anthropic)](https://alignment.anthropic.com/2025/subliminal-learning/): the 2025 work on traits moving between models through ordinary-looking data, which this paper builds on.

---
*Part of my [Learning Notes](/learning-notes/). Found via [Digital Dhaba](/tech-digest/).*
