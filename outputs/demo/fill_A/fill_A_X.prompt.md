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

Below is transcript X. Turns are numbered [T1], [T2], ... The interviewer's speaker name is: Interviewer.

For every cell, return:
- id: the cell id
- value: "yes" if the respondent says the cell applies to their own firm; "no" if the respondent says their firm did the opposite; "industry" if the respondent describes it only for other firms or the industry; "not_raised" if it does not come up
- turn: the turn number of the passage the value rests on (the earliest such turn), or -1 if not_raised
- quote: a passage from that turn, copied exactly (you may shorten with "..." between exact pieces), or "" if not_raised
- prompted: true if the interviewer raised the idea before the respondent did, false otherwise (false if not_raised)

Code only what the respondent says. Do not infer a value the transcript does not support; use not_raised instead. A script will check each quote against the transcript.

Return JSON: {"transcript": "X", "cells": [{"id": ..., "value": ..., "turn": ..., "quote": ..., "prompted": ...}]}

[T1] Host (0:04): Good morning, both of you. I'll let the interviewer explain the project.
[T2] Interviewer (0:25): Thank you for joining. We are studying how small and medium firms take up new tools and technology. Could you tell me a little about the business first?
[T3] Respondent (0:50): We make knitwear for export, mostly to Europe. My father started the unit, I came in about six years ago. We are around 300 people in the season, less in the off season.
[T4] Interviewer (2:00): What tools do you use day to day?
[T5] Respondent (2:20): Email, Excel, and a lot of phone. Last year I started using ChatGPT for the buyer emails and for the first draft of the tech packs. Earlier we paid a freelancer for the tech packs, now I do the draft myself and the pattern master checks it.
[T6] Interviewer (4:30): Who decides on things like that?
[T7] Respondent (4:50): My father still has the last word on anything that costs money. I had to convince him for the new cutting software, it took me a full season.
[T8] Interviewer (7:10): How did you convince him?
[T9] Respondent (7:30): I showed him the wastage numbers. Fabric is our biggest cost, so when he saw the wastage going down he agreed.
[T10] Interviewer (10:05): Is there anything he resists?
[T11] Respondent (10:20): A CRM for buyers. He says he knows every buyer personally, he has known some of them for twenty years, so why does he need a system to tell him. And for him that is true. For me it is not, I don't have those twenty years.
[T12] Interviewer (13:40): Who runs the cutting software?
[T13] Respondent (14:00): We hired a merchandising coordinator, a young girl with a fashion technology degree. She set up the software and now she runs the planning. The old staff were not comfortable with it.
[T14] Interviewer (17:20): Do your buyers push you to adopt things?
[T15] Respondent (17:40): Compliance, yes. Audits for labour and for chemicals. Tools, not really.
[T16] Interviewer (21:00): How do you think about cost when you adopt something?
[T17] Respondent (21:20): We look at payback in one season. If it does not pay back in a season my father will not agree.
[T18] Interviewer (25:50): And the workforce, is it easy to find people?
[T19] Respondent (26:10): Tailors are hard to find now. Wages have gone up every year, so we are looking at machines that save labour.
[T20] Interviewer (30:30): How do other exporters in your area work?
[T21] Respondent (30:50): Some bigger ones have full ERP. Most of the smaller ones are like us or behind us.
[T22] Interviewer (33:15): Have you thought about AI beyond the emails?
[T23] Respondent (33:35): Maybe for forecasting orders. But our orders depend on two or three buyers, so I don't know what it would learn from.
[T24] Interviewer (40:50): That's all from me. Thank you so much.
