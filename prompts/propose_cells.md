You are helping researchers learn the structure of a survey from open-ended interviews.

Research question: {{QUESTION}}

Below are all the interview transcripts collected so far. Turns are numbered [T1], [T2], ... The interviewer's speaker name is: {{INTERVIEWER}}. Every other speaker is a respondent or a host.

Read all the transcripts and propose the categories of responses that bear on the research question. These categories will become the cells of a survey instrument: for every later respondent, each cell will record whether it applies to that respondent's firm. Propose a category when at least one respondent raises it, even if only one does; the researchers will decide which to keep.

For each category return:
- id: a short snake_case name
- label: a short phrase, e.g. "New hires do the implementation"
- definition: one sentence saying what counts as this category applying to a firm
- evidence: every passage, in any transcript, where the category comes up. For each passage give the transcript name, the turn number, a quote copied exactly from that turn (you may shorten with "..." between exact pieces), and prompted = true if the interviewer raised the idea before the respondent did in that conversation, false otherwise.

Copy quotes exactly; a script will check each one against the transcript. Do not include a category that only the interviewer raises.

Return JSON: {"cells": [{"id": ..., "label": ..., "definition": ..., "evidence": [{"transcript": ..., "turn": ..., "quote": ..., "prompted": ...}]}]}

{{TRANSCRIPTS}}
