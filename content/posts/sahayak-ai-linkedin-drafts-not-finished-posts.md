---
title: "Sahayak: why my AI post tool writes drafts, never finished posts"
date: 2026-11-01
draft: false
ShowToc: false
categories: ["build-log"]
tags: ["generative ai", "linkedin", "build in public"]
url: /build-log/sahayak-ai-linkedin-drafts-not-finished-posts/
summary: "I launched Sahayak, which turns a real idea from your week into a LinkedIn draft built only from your facts. You always edit."
description: "How I built Sahayak, an AI tool that turns your real work into LinkedIn drafts using only the facts you give it, and why it never writes finished posts."
project: Sahayak
status: shipped
---

**TL;DR:** I launched Sahayak, a tool that turns a real idea from your week into a LinkedIn draft. The decision that shaped it: it works only from the facts you give it, and you always edit before you post. Even its own launch post went through that.

## The problem

I wasn't consistent on LinkedIn. There was no pattern: sometimes a post a week, sometimes one or two posts in a whole year. That's why I built Sahayak. And I'm not alone: a lot of Indian professionals want a presence on LinkedIn but struggle to stay consistent. For me, typing was never the hard part. The hard part was turning what I learned or did at work into something worth sharing, week after week, alongside a full-time job.

## What I built

Sahayak (सहायक, "helper") takes two things from you: a topic, and context in your own words, such as notes, an article or what happened. You pick one of five formats, and it writes a draft in that shape. You edit it, decide, and post it yourself. It never posts for you and never asks for your LinkedIn login. Every draft, and your edited version of it, is saved in your Post History.

The five formats:

- **Concept Breakdown:** a short teacher–student dialogue that explains one idea simply
- **Insights from Others:** your angle on something you read, watched or listened to
- **Build in Public:** an honest update on something you're building
- **Hot Takes & Opinions:** your view on news, a trend or a conviction you hold
- **Story Post:** a real moment from your work, told as a story

All 14 posts I published over the past five weeks started as Sahayak drafts. None were typed from scratch; all were edited by me before they went up.

### Under the hood

- **App:** Next.js 14 with TypeScript, Tailwind CSS and shadcn/ui, hosted on Vercel
- **Data and sign-in:** Supabase (Postgres, authentication, and row-level security so each user only ever sees their own drafts)
- **Drafts:** Anthropic's Claude (Sonnet 5), with a separate set of rules for each format
- **Payments:** Razorpay, in rupees, with UPI
- **Analytics and bot protection:** PostHog and Cloudflare Turnstile

## How I built it

I built Sahayak alongside my job, in evenings and weekends, between March and October 2026, though not continuously: from May to August, very little happened. As a PM, I started where I always do: the problem, the user and a plan, before any code. Then I built it with an AI coding assistant, which is how one person with a day job can ship a full product.

It went through four stages, and each one changed it:

- **Building it for myself.** A working version I used for my own posts. Using it daily showed me the gap between a draft that looks fine and one I'd actually post.
- **A few friends.** The feedback stung: "feels like ChatGPT" and "what makes this different?" Fair. That's when the formats became the centre of the product, and when I started treating made-up details as a bug, not a style issue.
- **Fixing what they found.** The Hot Takes format was inventing statistics, so I rewrote its rules. The home screen now starts with the five formats instead of an empty box, and each format got a real example.
- **A stealth month.** Five weeks of posting on LinkedIn with Sahayak, without telling anyone. Every post was a real test with real readers. When a draft needed the same fix twice, I fixed the format's rules instead of just the post, and added the case to my tests.

What I'd tell anyone building on the side: keep using your own product. The friends' feedback told me *what* was wrong; daily use told me *where*.

## The one thing: drafts from your facts, not finished posts

The option I didn't pick was the obvious one: generate a polished post and publish it for you. I chose drafts, built from only what you give it.

**The fastest way to lose trust is a made-up detail.** Your readers know you. If a post quotes an opinion nobody gave you, or a number you never shared, you're the one who looks bad. So each format's rules say: use only what the user gave, keep vague things vague, and write around a missing detail instead of filling it in.

I test this with sample inputs that deliberately leave numbers out, and a check fails any draft that adds one. It still slips sometimes. One of my own Hot Takes came back with "Everyone's timeline is calling this copying". Nobody had said that; I hadn't given it any such reaction. I cut it, and it became a test case. That's the other reason the edit step isn't optional.

**Why not just use ChatGPT?** You can, and I did. But every time, I was re-explaining the format, the tone and the rules, and it was quick to fill gaps with plausible-sounding details. In Sahayak, each format's structure and rules are already built in, including the rule to stick to your facts. You bring the idea and the context; you don't write a prompt.

**Built around Indian professionals.** The drafts use Indian English. There's Hindi on Pro (in beta), written to avoid guessing your gender from the verbs, which Hindi otherwise forces. Payment is in rupees, with UPI. The formats fit the moments of an Indian tech professional's week: explaining something to a junior colleague, a talk that stuck with you, something you shipped or broke.

**The launch post shows why the edit matters.** Sahayak drafted it; I edited it. The three changes that mattered:

| | Sahayak's draft | What I published |
|---|---|---|
| Opening | "Sahayak is live: the tool that drafted my LinkedIn posts this past month", a name nobody knew yet | "Every post I published this past month was drafted by a tool I built." The name comes two lines later |
| The claim | "It doesn't invent numbers or quotes you didn't give it" | "It's built to use only the facts you give it", because that's the honest version |
| The ask | "Honest feedback welcome" | "Use it for two weeks and tell me where it breaks", plus a question for everyone |

I also added the line that makes the rest believable: "14 posts in 5 weeks, alongside a full-time job." Both full versions are at the end.

## Next

For five weeks I posted without saying how the posts were made. Next week I'll share what that stealth month taught me: how Sahayak fit into my week, which formats worked, and what I changed along the way.

And one open question, the same one from my launch post: what stops you posting more, finding something to say, or writing it? I'll share what people answer.

---

### The draft and the published post, in full

**Sahayak's draft:**

> Sahayak is live: the tool that drafted my LinkedIn posts this past month.
>
> Every post you read from me recently wasn't typed from scratch. It was drafted with Sahayak, a tool I built, then edited by me before it went up.
>
> Today I'm making it public.
>
> Why I built it: a lot of Indian professionals want a presence on LinkedIn but struggle to stay consistent. For me, typing was never the hard part. The hard part was turning what I learned or did at work into something actually worth sharing.
>
> How it works:
>
> You bring a real idea from your week as the topic.
>
> You add context in your own words.
>
> You pick one of five ways to tell it — Concept Breakdown, Insights from Others, Build in Public, Hot Takes, Story Post.
>
> You get a draft.
>
> Then you edit it, you decide, you post.
>
> A few things I was deliberate about:
>
> It never posts for you.
>
> It never asks for your LinkedIn login.
>
> It doesn't invent numbers or quotes you didn't give it.
>
> Free for 5 posts a month.
>
> Link is in the first comment. If you try it, I'd genuinely like to know where it breaks for you — honest feedback welcome.

**What I published:**

> Every post I published this past month was drafted by a tool I built.
>
> 14 posts in 5 weeks, alongside a full-time job. None typed from scratch. All edited by me before they went up.
>
> It's called Sahayak, and today it's public.
>
> Why I built it: a lot of Indian professionals want a presence on LinkedIn but struggle to stay consistent. For me, typing was never the hard part. The hard part was turning what I learned or did at work into something worth sharing.
>
> How it works:
>
> → Bring a real idea from your week
>
> → Add context in your own words: notes, an article, what happened
>
> → Pick one of five formats: Concept Breakdown, Insights from Others, Build in Public, Hot Takes, Story Post
>
> → Get a draft
>
> → Edit it, decide, post
>
> What I was deliberate about:
>
> → It never posts for you
>
> → It never asks for your LinkedIn login
>
> → It's built to use only the facts you give it, not invent numbers or quotes
>
> Free for 5 posts a month.
>
> Link in the first comment. One ask: if you try it, use it for two weeks and tell me where it breaks.
>
> And a question for everyone: what stops you posting more, finding something to say, or writing it?

---

*Part of my [Build Log](/build-log/). Try Sahayak free for 5 posts a month: [postsahayak.com](https://postsahayak.com/?utm_source=blog&utm_medium=buildlog&utm_campaign=reveal)*
