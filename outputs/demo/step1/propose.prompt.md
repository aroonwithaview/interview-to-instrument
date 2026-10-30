You are helping researchers learn the structure of a survey from open-ended interviews.

Research question: Why do small and medium-sized firms in developing countries adopt digital tools and AI slowly, and which force dominates?

Below are all the interview transcripts collected so far. Turns are numbered [T1], [T2], ... The interviewer's speaker name is: Interviewer. Every other speaker is a respondent or a host.

Read all the transcripts and propose the categories of responses that bear on the research question. These categories will become the cells of a survey instrument: for every later respondent, each cell will record whether it applies to that respondent's firm. Propose a category when at least one respondent raises it, even if only one does; the researchers will decide which to keep.

For each category return:
- id: a short snake_case name
- label: a short phrase, e.g. "New hires do the implementation"
- definition: one sentence saying what counts as this category applying to a firm
- evidence: every passage, in any transcript, where the category comes up. For each passage give the transcript name, the turn number, a quote copied exactly from that turn (you may shorten with "..." between exact pieces), and prompted = true if the interviewer raised the idea before the respondent did in that conversation, false otherwise.

Copy quotes exactly; a script will check each one against the transcript. Do not include a category that only the interviewer raises.

Return JSON: {"cells": [{"id": ..., "label": ..., "definition": ..., "evidence": [{"transcript": ..., "turn": ..., "quote": ..., "prompted": ...}]}]}

=== Transcript W ===
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

=== Transcript X ===
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

=== Transcript Y ===
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
