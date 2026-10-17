---
title: "When two AIs grade each other, they can agree their way into wrong answers"
date: 2026-10-17
draft: false
ShowToc: false
categories: ["learning-notes"]
tags: ["generative ai", "large language models", "ai agents"]
url: /learning-notes/two-ais-grading-each-other-agree-on-wrong-answers/
summary: "Two copies of one model that write and grade each other's questions can look healthy while agreeing on more wrong answers."
description: "A learning note on the paper 'False Frontiers': when two copies of one AI train each other, agreement can look like progress while shared mistakes grow."
source: "False Frontiers: Diagnosing and Mitigating Co-Cheating in Self-Evolving Search Agents"
source_url: https://arxiv.org/abs/2609.39102
source_type: paper
---

**TL;DR:** If one AI writes the quiz and its twin takes it, and each is rewarded based on the other, their scores can keep looking healthy while they quietly agree on more and more wrong answers, and AI is increasingly trained and graded by AI.

## The source

A 2026 research paper by researchers from Rutgers, UC San Diego, Michigan, McGill and others: [False Frontiers: Diagnosing and Mitigating Co-Cheating in Self-Evolving Search Agents](https://arxiv.org/abs/2609.39102).

## The idea, in my words

If one AI writes the quiz and its twin takes the quiz, and each is rewarded based on the other, their scores can keep looking healthy while they quietly agree on more and more wrong answers.

A "self-evolving search agent" is an AI that learns to answer questions by looking things up. It trains in a loop with two copies of the same model. The **proposer** reads a source document and writes a question plus what it believes is the answer. The **solver** tries to answer it. The solver learns from the proposer's questions, and the proposer is rewarded according to how the solver does. No human checks anything.

The solver answers each question five times. The proposer earns the most when the solver gets it right only sometimes, and nothing when the solver gets it right every time or never. The idea is to keep pushing at the edge of what the solver can do, which the field calls the "frontier."

![Diagram: two identical AIs revise from shared notes that say 2 + 2 = 5 and tick each other's wrong answer, showing 100% agreement. The fix: an examiner AI that studied a different book marks the answer wrong. Agreement is not correctness.](/assets/images/two-ais-mark-each-others-homework.webp)

## What I took from it

It's like two students who revise from the same set of notes, which contain a mistake, and then mark each other's homework. Both get a tick. The marks look fine and the mistake is now locked in. The analogy stops working in one place: nobody is cheating on purpose. The models are simply following a reward that can't tell agreement from correctness.

**The problem it answered:** it had long been suspected that models training on their own guesses reinforce their own errors. Researchers call this *confirmation bias* in pseudo-labelling, and a 2016 paper co-written by Dario Amodei listed "reward hacking" among the core AI safety problems. This paper puts a number on it for the specific case of two models training each other, and shows the number grows round by round.

**AI is increasingly trained and graded by AI.** Labs use models to write training data, to judge other models' answers, and to run benchmarks. This paper is a concrete case of how that can produce numbers that rise for the wrong reason.

My last Learning Note, on [Post-Training Leaves Behavioral Shadows](/learning-notes/training-an-ai-for-one-skill-changes-its-other-answers/), found that models sharing a starting point pass skills to each other through harmless-looking text. This one finds they also share blind spots. Both suggest that a second copy of the same model is a weak independent check.

## What I'm still unsure about

- **Small scale:** two small open models (Qwen3.5 at 4 and 9 billion parameters), three training rounds, and 1,325 test questions. Frontier models are far larger and train far longer. Whether the problem gets worse or better at scale is not shown.
- **The examiner is also an AI.** The "ground truth" comes from GPT-6 Astra reading the sources. The paper does not report checking it against human judges, and the audit covered about 86% of cases.
- **The fix costs more:** CrossFit adds roughly 72–79% to the computing bill in its main setting (about 36–40% in a lighter version). Using both fixes together costs about 2.6 times the baseline.
- **Still open:** the authors say some of the drop in shared mistakes may come from the system simply refusing harder questions. They also note the two piles are not truly independent, since the models share the same pre-training and many web pages repeat each other. No code release is mentioned.

## Further reading

- [False Frontiers: Diagnosing and Mitigating Co-Cheating in Self-Evolving Search Agents](https://arxiv.org/abs/2609.39102): the paper itself.
- [Post-Training Leaves Behavioral Shadows on Unrelated Decisions](https://arxiv.org/abs/2609.29233): the paper behind my last Learning Note, on models that share a base passing skills to each other.
- [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565): the 2016 paper co-written by Dario Amodei that listed reward hacking among the core AI safety problems.

---
*Part of my [Learning Notes](/learning-notes/). Found via [Digital Dhaba](/tech-digest/).*
