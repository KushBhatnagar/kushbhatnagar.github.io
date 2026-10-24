---
title: "Job Sherpa: an open-source job-search assistant that can't make up your resume"
date: 2026-10-24
draft: false
ShowToc: false
categories: ["build-log"]
tags: ["generative ai", "ai agents", "job search"]
url: /build-log/job-sherpa-open-source-job-search-assistant/
summary: "An open-source job-search assistant for any coding agent: it finds and scores jobs, tailors resumes and never invents a claim."
description: "How I built Job Sherpa, an open-source job-search assistant for any coding agent that finds and scores jobs and tailors resumes without inventing claims."
project: Job Sherpa
status: shipped
---

**TL;DR:** Job Sherpa is an open-source job-search assistant that runs on your own computer, inside any coding agent. It finds jobs, scores how well each one fits, tailors resumes that never invent a claim, and helps you prepare for interviews.

## The problem

<!-- CHECK: your words. Assembled from your notes: -->
A few friends of mine lost their jobs some time back. Talking to them, I realized how tedious job hunting is: finding the right openings, reading every job description properly, rewriting the resume and cover letter for each one, keeping track of who replied, and preparing for interviews. That made me think: could we build something simple with a coding agent to take the tedious parts off their plate?

AI tools can already write a resume, but they also "improve" it: a number goes up, a contribution becomes leadership. It reads well until an interviewer asks about it.

## What I built

A sherpa doesn't climb the mountain for you. They know the route, carry the load and stop you from taking a wrong step. Job Sherpa does that for your job search; the climb, and every application, stays yours.

![How Job Sherpa works: your resume and questionnaire answers build a private folder on your computer; from it, Job Sherpa finds jobs, scores the fit, tailors your resume and cover letter, you apply, it tracks and follows up, and helps you prepare for interviews](/assets/images/job-sherpa-how-it-works.png)

- **Onboarding:** you give it your resume and answer a structured questionnaire. It builds a private knowledge base: your profile, a bank of achievement bullets (each one recording where it came from), and your interview stories.
- **Finding jobs:** public job-board APIs (Greenhouse, Lever, Ashby, SmartRecruiters and Adzuna), with a starter list of 101 tech companies. Jobs from LinkedIn and similar sites, you paste in.
- **Scoring:** every job is scored against your profile, from the full job description, never from a 500-character excerpt.
- **Tailoring:** a resume and cover letter per job, built only from your bullets.
- **Tracking:** every application and what happened next, with a nudge when one goes quiet.
- **Interview prep:** for each interview, a prep sheet that matches likely questions to your own stories, gives honest answers to the hard ones, and runs a mock round with you.

Everything stays on your computer. There is no server, no account and no sign-up: Job Sherpa is a folder you download. The only network calls fetch job postings, and nothing about you goes with them. (Your coding agent does send the files it reads to its AI model, as it does with any code you open in it.)

### Decisions I took

- **A local SQLite database, not a cloud service.** Jobs, applications and every outcome live in one file in your private folder, which also holds your profile and drafts. A git hook refuses to commit that folder.
- **A command line that works without a coding agent.** The agent does the judgment (is this job a fit, which bullets to lead with). Everything mechanical is a plain `sherpa` command anyone can run: discover jobs, add one, log an application, see follow-ups and stats.
- **Playbooks in plain Markdown, not tied to one AI tool.** The judgment lives in written steps that Claude Code, Codex, Cursor and others can all follow.
- **The honesty rule is checked by code, not just requested in a prompt.** Before a resume becomes a PDF, every line must point to one of your bullets, and any number that isn't in the original blocks the render. A prompt can be ignored; a failed check can't.
- **Public job-board APIs, no scraping.** Greenhouse, Lever, Ashby and SmartRecruiters publish job feeds so companies' jobs get found. Sites that forbid automated access are never fetched.
- **Python's standard library plus Typst.** No packages to install except Typst, which renders the PDFs, so setup is one `pip install`.

## The one thing

<!-- CHECK: your words needed. Draft assembled from your ATS research notes: -->
The applicant tracking system is not what rejects most resumes. The often-quoted "75% of resumes are auto-rejected" figure traces back to a 2012 sales pitch. In a 2025–26 survey of recruiters using Workday, iCIMS and Greenhouse, 92% said their ATS does not auto-reject on resume content or formatting. Greenhouse's own documentation says the only automatic rejection it supports is knockout questions, like years of experience or work authorization.

So the fast "no" usually comes from a stated minimum you don't meet, not from your keywords. Job Sherpa scores that way: any requirement you don't meet caps a job's score at 6, however good the match. And a cover letter names a domain gap honestly, but never restates a years or degree shortfall: the dates are already on the resume.

## What's still broken / next

- The company list was checked against live job boards in September. Companies change job boards quietly, so run `sherpa check-companies` before you rely on it.
- Workday (used by many large companies) and job-alert emails aren't supported yet.
- So far it has been tested on a fictional sample user. I'd like to hear how it works for you.

Try it: [github.com/KushBhatnagar/job-sherpa](https://github.com/KushBhatnagar/job-sherpa). If it helps you or a friend, a star helps others find it.

---
*Part of my [Build Log](/build-log/).*
