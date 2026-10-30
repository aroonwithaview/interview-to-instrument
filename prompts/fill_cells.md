You are coding one interview against a fixed set of cells.

Research question: {{QUESTION}}

Cells (id: label. definition):
{{CELLS}}

Below is transcript {{NAME}}. Turns are numbered [T1], [T2], ... The interviewer's speaker name is: {{INTERVIEWER}}.

For every cell, return:
- id: the cell id
- value: "yes" if the respondent says the cell applies to their own firm; "no" if the respondent says their firm did the opposite; "industry" if the respondent describes it only for other firms or the industry; "not_raised" if it does not come up
- turn: the turn number of the passage the value rests on (the earliest such turn), or -1 if not_raised
- quote: a passage from that turn, copied exactly (you may shorten with "..." between exact pieces), or "" if not_raised
- prompted: true if the interviewer raised the idea before the respondent did, false otherwise (false if not_raised)

Code only what the respondent says. Do not infer a value the transcript does not support; use not_raised instead. A script will check each quote against the transcript.

Return JSON: {"transcript": "{{NAME}}", "cells": [{"id": ..., "value": ..., "turn": ..., "quote": ..., "prompted": ...}]}

{{TRANSCRIPT}}
