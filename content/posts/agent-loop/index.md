---
title: "What Makes an AI Agent Feel Autonomous? The Agent Loop"
date: 2026-10-20
draft: false
categories: ["concept-breakdown"]
tags: ["generative ai", "large language models", "ai agents", "classroom conversation"]
summary: "Hint: it's just Mom's cooking. Plan, act, observe, repeat: the loop that makes an ordinary model feel like an agent."
description: "What is the agent loop? A comic breakdown using Mom's cooking to explain plan, act, observe, repeat, and why the loop, not a smarter model, makes AI agents."
url: /concept-breakdown/agent-loop/
images: ["cover.jpg"]
ShowToc: false
slide_alt:
  - "Teacher says Mom never follows a recipe start to finish; she plans a step, tastes, and adjusts. That loop makes a real cook"
  - "Teacher compares a plain LLM to reading a recipe once; an AI agent plans, acts, observes what came back, then repeats"
  - "Teacher: if a stock API errors, an agent notices and re-plans. Same model; the plan-act-observe-repeat cycle adds judgement"
  - "Takeaway: an agent isn't a smarter model; it's a model in a plan, act, observe, repeat loop"
---

{{< carousel >}}

{{< transcript >}}
**Slide 1: Mom tastes as she goes**

**Teacher:** You know how your mom never follows a recipe start to finish? She tastes as she goes and adjusts.  
**Student:** Yeah, she keeps adding salt or water depending on how it's turning out. Why?  
**Teacher:** Because cooking isn't a one-shot task. She plans a step, does it, tastes it, and changes the next step based on that taste. That loop is exactly what separates a real cook from someone blindly following a recipe card.  
**Student 2:** Okay, but what does that have to do with AI?

**Slide 2: Plan, act, observe, repeat**

**Teacher:** A plain LLM answer is like reading a recipe out loud once: text in, text out, done. No tasting involved. An AI agent, though, works like your mom in the kitchen.  
**Student:** How exactly?  
**Teacher:** First it plans: "let me check the stock price." Then it acts: actually calls the tool or API. Then it observes: looks at what came back. Then it repeats: plans the next step based on that observation.  
**Student 2:** So it's not just answering once, it's checking its own work as it goes?

**Slide 3: Same model, wrapped in a loop**

**Teacher:** Exactly. If the stock API returns an error, a one-shot model would just hallucinate a number and move on. An agent notices the error in the "observe" step and re-plans, maybe tries a different source.  
**Student:** Wait, so the model itself isn't smarter in an agent, it's just… looping?  
**Teacher:** That's the part people miss. The underlying model is often identical. It's this plan-act-observe-repeat cycle wrapped around it that creates the feeling of judgement and autonomy.  
**Student 2:** So an agent isn't a genius model. It's a decent cook who keeps tasting the dish before serving it.

**Slide 4: The loop, not raw intelligence**

**Teacher:** Exactly: the loop, not raw intelligence, is what makes it feel autonomous.  
**Takeaway:** An agent isn't a smarter model. It's a model in a plan → act → observe → repeat loop.
{{< /transcript >}}

## The concept in plain words

The **agent loop** is the cycle an AI agent runs: plan a step, act on it, observe what came back, then repeat with the next step.

It's how Mom cooks. She doesn't follow a recipe start to finish. She does a step, tastes, and adjusts the next one. A plain LLM answer is more like reading the recipe out loud once: text in, text out, done. An agent plans ("let me check the stock price"), acts by calling a tool or API, looks at the result, and decides what to do next.

That "observe" step is what catches mistakes. If the stock API returns an error, a one-shot model might hallucinate a number. An agent notices the error and re-plans, maybe trying another source.

The surprising part: the model inside an agent is often the same one. What feels like judgement and autonomy comes from the loop wrapped around it, not from a smarter model.
