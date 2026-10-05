# Kit welcome text — DRAFT for Kush to edit

Not used by any code. Paste into Kit by hand (form `10000596` → Settings). Rewrite freely in your own words.

## Option 1: confirmation email (double opt-in) — Kit form → Settings → Incentive / confirmation email

**Subject:** Confirm your subscription to Blogs by Kush

> Hi,
>
> Thanks for signing up. One click and you're in:
>
> [Confirm subscription]   ← Kit's confirm button
>
> What you'll get, at most two emails a week:
> - **Thursday: Digital Dhaba**, a short roundup of the week's AI and tech news for product people.
>   Claude does the reading and ranking; every story links to its source.
> - **Sunday: a short letter** with whatever I published that week: Concept Breakdowns (concepts
>   explained as comics), Learning Notes and the Build Log. No post that week, no email.
>
> If you didn't sign up, ignore this email and you won't hear from me.
>
> Kush

**After confirming, send them to:** `https://blogsbykush.com/concept-breakdown/how-llms-think/`
(Kit form → Settings → "After confirming, redirect to" an external page). Or the latest Digital Dhaba issue.

## Option 2: separate welcome email (Kit → Send → Sequences, 1 email; automation: subscribes to form → sequence)

**Subject:** Welcome to Blogs by Kush
**Preview text:** What to expect, and where to start

> Hi,
>
> You're in. Thanks for subscribing.
>
> I'm Kush, a product manager working on AI products. This blog is how I learn in public:
> I **learn** (Digital Dhaba and Learning Notes), **build** (the Build Log) and then **explain**
> (Concept Breakdowns, short comics that make one idea click).
>
> **What lands in your inbox:**
> - **Thursday, Digital Dhaba:** the week's AI and tech news for product people, with a line on why each story
>   matters. Claude curates it; I built the pipeline.
> - **Sunday, a short letter:** everything I published that week. Quiet week, no email.
>
> **Good place to start:** [How LLMs Think](https://blogsbykush.com/concept-breakdown/how-llms-think/),
> a comic about what actually happens when you send a prompt.
>
> One ask: hit reply and tell me what you work on, or what concept you'd like explained next.
> I read every reply.
>
> Kush
> [blogsbykush.com](https://blogsbykush.com)

Notes: the 15 subscribers imported from Mailchimp don't get either email (imports skip the form).
Kit adds the unsubscribe link and postal address footer itself.
