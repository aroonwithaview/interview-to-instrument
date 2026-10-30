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

Below is transcript W. Turns are numbered [T1], [T2], ... The interviewer's speaker name is: Interviewer.

For every cell, return:
- id: the cell id
- value: "yes" if the respondent says the cell applies to their own firm; "no" if the respondent says their firm did the opposite; "industry" if the respondent describes it only for other firms or the industry; "not_raised" if it does not come up
- turn: the turn number of the passage the value rests on (the earliest such turn), or -1 if not_raised
- quote: a passage from that turn, copied exactly (you may shorten with "..." between exact pieces), or "" if not_raised
- prompted: true if the interviewer raised the idea before the respondent did, false otherwise (false if not_raised)

Code only what the respondent says. Do not infer a value the transcript does not support; use not_raised instead. A script will check each quote against the transcript.

Return JSON: {"transcript": "W", "cells": [{"id": ..., "value": ..., "turn": ..., "quote": ..., "prompted": ...}]}

[T1] Host (0:05): Thanks for making time. I've told you a bit about the research already, so I'll hand over.
[T2] Interviewer (0:20): Thank you. We are studying how small and medium firms take up new tools, software, machines, anything really. Could you start by telling me about the business?
[T3] Respondent (0:45): Sure. We machine components for two-wheeler and tractor makers. My father started it in 1991 with three lathes. Today we have about 120 people on two shifts. I joined full time eight years ago, after working at a bigger supplier.
[T4] Interviewer (2:10): What has changed since you joined?
[T5] Respondent (2:30): Honestly the biggest change came when my younger brother came back from his masters. He was the one who said we cannot run the shop floor from one register anymore. He pushed for a production dashboard, every machine, every job, on a screen in the office.
[T6] Interviewer (4:05): And how did that go?
[T7] Respondent (4:20): The first year was hard. My father did not see the point, he walks the floor every morning and he knows which machine is down. But my brother kept at it. We hired a young fellow from a polytechnic as an IT coordinator, and he is the one who actually set it up and trains the supervisors.
[T8] Interviewer (6:40): Did you buy software for this?
[T9] Respondent (7:00): We tried. We paid an ERP vendor for almost a year. Their package was made for a plant that makes the same part all day. We are a job shop, every order has a different routing. So the vendor kept saying change your process to fit the software. We stopped that and built simple sheets that the coordinator maintains.
[T10] Interviewer (9:30): What about the machines themselves? Have you automated anything?
[T11] Respondent (9:50): Very little. A robot loader costs what I pay six operators for many years. Labour here is still cheap, so automation does not pay back unless the customer forces it.
[T12] Interviewer (12:15): How do customers affect what you adopt?
[T13] Respondent (12:35): The big customers send audit teams. They want traceability, which batch of steel went into which part. That is where the dashboard helped us pass the audit last year.
[T14] Interviewer (15:00): How do decisions on new tools get made?
[T15] Respondent (15:20): For small things I decide. For anything above a few lakhs my father has the final word, and he will ask three people before he says yes.
[T16] Interviewer (18:40): Do other firms in your cluster do the same?
[T17] Respondent (19:00): Most of them are where we were ten years ago. Paper job cards, everything on the phone.
[T18] Interviewer (22:30): Let's talk about your suppliers and how you buy steel.
[T19] Respondent (23:00): We buy from two traders. Everything is on WhatsApp, rates come every morning. We don't need software for that.
[T20] Interviewer (27:10): How do you train new operators?
[T21] Respondent (27:30): Mostly on the job. The senior operator shows them. We tried videos but people did not watch them.
[T22] Interviewer (32:20): One last area. Have you used any AI tools, ChatGPT or anything like that?
[T23] Respondent (32:40): Not really in the business. My brother uses ChatGPT to write quotation emails sometimes. We have not thought about AI for the shop floor.
[T24] Interviewer (35:10): Is there anything that would make you try it?
[T25] Respondent (35:30): If a customer asked for it, or if someone showed me it works in a shop like mine. Not a demo in a hotel.
[T26] Interviewer (37:30): Thank you, this was very helpful.
