You are coding one interview against a fixed set of cells.

Research question: Why do small and medium-sized firms in developing countries adopt digital tools and AI slowly, and which force dominates?

Cells (id: label. definition):
- younger_family_member_pushes: Younger family member pushes adoption. A younger member of the owning family (child, sibling or cousin of the owners) is the person who proposes or pushes for a new digital tool or AI.
- cheap_labour_blocks_automation: Cheap labour makes automation unprofitable. Labour is cheap enough that machines or automation that replace workers do not pay back.
- labour_scarcity_pushes_automation: Rising wages or labour shortage push labour-saving machines. Difficulty hiring workers or rising wages lead the firm to consider or adopt machines that save labour.
- customer_requirements_drive_adoption: Customers require the tool or practice. Customers, through audits or explicit requests, require traceability, compliance or a specific tool, and this triggers or would trigger adoption.
- new_hires_implement: New hires do the implementation. The firm hired a young, technically trained employee who set up the new tool and now runs it or trains others on it.
- packaged_software_misfit: Packaged software does not fit the firm. Available software packages are designed for larger firms or a different production model and do not fit the firm's processes.
- software_fees_exceed_margins: Software fees too high for thin margins. Recurring software fees, such as per-user monthly charges, are too high relative to the firm's margins.
- tool_replaces_paid_outside_service: Tool replaces a paid outside service. A new tool, often AI, lets the firm do in-house work it previously paid a freelancer or developer to do.
- ai_used_to_build_software: Uses AI to build internal software. Someone at the firm used an AI app builder or coding assistant to build a tool the business runs on.
- genai_for_writing: Uses ChatGPT for writing tasks. Someone at the firm uses a generative AI chatbot to draft emails, quotations or documents.
- older_owners_see_no_need: Older owners see no need for the tool. A founder or older owner resists a tool because they already know the business or see no use for it.
- approval_by_senior_or_partners: Spending needs a senior family member or all partners to agree. A tool that costs money is adopted only if a senior family member, or every partner, agrees.

Below is transcript Y. Turns are numbered [T1], [T2], ... The interviewer's speaker name is: Interviewer.

For every cell, return:
- id: the cell id
- value: "yes" if the respondent says the cell applies to their own firm; "no" if the respondent says their firm did the opposite; "industry" if the respondent describes it only for other firms or the industry; "not_raised" if it does not come up
- turn: the turn number of the passage the value rests on (the earliest such turn), or -1 if not_raised
- quote: a passage from that turn, copied exactly (you may shorten with "..." between exact pieces), or "" if not_raised
- prompted: true if the interviewer raised the idea before the respondent did, false otherwise (false if not_raised)

Code only what the respondent says. Do not infer a value the transcript does not support; use not_raised instead. A script will check each quote against the transcript.

Return JSON: {"transcript": "Y", "cells": [{"id": ..., "value": ..., "turn": ..., "quote": ..., "prompted": ...}]}

[T1] Host (0:03): Thanks for joining. As I mentioned, this is for a research project, so please speak freely.
[T2] Interviewer (0:20): Thank you. We are studying how small and medium firms take up new tools and technology. Could you start by describing the business?
[T3] Respondent (0:40): We distribute medicines to chemists and hospitals in four districts. It is a partnership between two families, each with two partners. About 60 people, mostly delivery staff.
[T4] Interviewer (2:10): How are decisions made between the two families?
[T5] Respondent (2:30): Anything big needs all four partners to agree. That is why things move slowly. One partner likes to wait and see what others do.
[T6] Interviewer (5:00): What software do you run?
[T7] Respondent (5:20): We had a billing package from a local developer. Every change took months and he charged for each change. And the big distribution software charges per user every month. With forty users on margins of three or four percent, that is not possible for us.
[T8] Interviewer (8:45): So what did you do?
[T9] Respondent (9:05): Last year I built our own order tracker with one of these AI app builders. It took me about three weekends. We stopped paying the developer for changes, I just make them myself now.
[T10] Interviewer (12:30): Did the partners agree to that?
[T11] Respondent (12:50): They agreed because it cost almost nothing. If I had asked for money they would have said no.
[T12] Interviewer (16:10): Do you think it's the younger generation that is bringing in these changes?
[T13] Respondent (16:25): Yes, yes, that is right. My cousin and I are the ones pushing. The older partners are happy if billing works.
[T14] Interviewer (19:40): How do other distributors handle orders?
[T15] Respondent (20:00): Many still use paper ledgers and call the chemists every day. The software companies make products for the big national distributors, not for people like us.
[T16] Interviewer (24:30): Who maintains the tracker?
[T17] Respondent (24:50): Me. That is the problem. If I am travelling, nobody can fix it.
[T18] Interviewer (28:00): Any plans to hire for that?
[T19] Respondent (28:20): Maybe one person. But a good IT person will not stay in a small town for what we can pay.
[T20] Interviewer (33:50): Thank you, that's very helpful.
