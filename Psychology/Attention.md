---
layout: page
title: "Attention"
---

# [Astartup Cookbook](../)

## [Psychology](./)

### Attention

Attention is the gateway to everything else in startup work. You cannot learn, build, sell, or retain customers with a mind that is half-elsewhere. The psychology of attention is the study of how the brain selects which stimuli to process and which to ignore, and it has direct implications for how a solo founder or a small team should structure their workday.

#### The Limited Bandwidth Problem

The brain cannot attend to everything at once. Attention is a finite resource, not an infinite one. When you divide your attention across two tasks, you do not process each at half speed; you process each at a degraded quality because the brain is switching between them. Each switch carries a cognitive cost called attention residue, a fragment of your focus that remains stuck on the previous task.

Practical consequence: context switching is not free. Every time you check email, Slack, or your phone, you pay a tax of several minutes to get back to full focus on the task you were doing. A workday with twenty interruptions is not a workday with twenty short tasks; it is a workday where no task ever got deep attention.

#### Types of Attention

1. **Selective attention** — focusing on one stimulus while ignoring others. This is what you need when you are debugging, writing, or interviewing a customer. Everything else must be filtered out.
2. **Sustained attention** — maintaining focus on a single task over an extended period. This is what you need for a deep work block, a two-hour coding session, or a ninety-minute customer interview.
3. **Divided attention** — attending to two or more tasks simultaneously. This is possible for one automatic task (humming while typing) but not for two demanding tasks. You cannot write a business plan and have a substantive customer conversation at the same time.
4. **Alternating attention** — switching between tasks in a controlled, deliberate way. This is different from involuntary context switching. You plan the switch: "I will work on the pricing model for forty-five minutes, then switch to drafting the investor email." The switch is a decision, not an interruption.

#### Attention and Flow

Flow is the state of complete absorption in a task. It requires a specific setup: a clear goal, immediate feedback, and a balance between the challenge and your skill level. Attention is the entry ticket to flow. If your attention is fragmented, you cannot enter flow, and if you are in flow, any interruption knocks you out and it takes fifteen to twenty-five minutes to re-enter.

The night and day session model from the Productivity chapter is an attention management strategy: protect the flow blocks (day sessions) from the attention-fragmenting tasks (email, meetings, admin) by scheduling them in separate blocks.

#### The Attention Economy

In a startup, attention is the scarcest resource, not time. You have twenty-four hours, but you have maybe four to six hours of genuine, high-quality attention. Everything else is maintenance: admin, communication, context switching, recovery. The founder's job is to allocate those four to six hours to the highest-leverage tasks, which are usually:

* Customer interviews and conversations
* Building the core product feature that unblocks progress
* The one strategic decision that, if wrong, sinks the company

Everything else is either delegated, automated, or deferred.

#### Designing for Attention

When you build a product, you are competing for the user's attention. The psychology of attention tells you:

* **Reduce cognitive load.** Every element on a screen that does not help the user complete their task is attention tax. Remove it.
* **One primary action per screen.** If there are five things the user could do, they will do none of them well. Pick the one that matters most and make it obvious.
* **Progressive disclosure.** Show the minimum information needed for the current step. Reveal more only when the user asks for it or reaches the next step. This is the disclosure principle from the UX chapter.
* **Minimize interruptions.** If your product pings the user every time something happens, you are training them to ignore your product. Batch notifications. Let the user check in on their schedule.
* **Respect the user's attention budget.** The user is not just using your product; they are using their job, their family, their other tools. Your product is one claim on their attention among many. Earn the right to that attention by being useful, not by being loud.

#### Local LLM and Attention

When working with a local LLM, the model's attention mechanism has the same limitation as human attention: it degrades over long contexts. The model can technically attend to every token in its context window, but the quality of attention to tokens in the middle of a very long context is lower than for tokens at the beginning or end.

This means the same strategies apply: put the most important instructions at the start or end of the prompt, keep the context short and focused, and do not expect the model to reliably recall a constraint you mentioned forty turns ago. Write the constraint to a file and reference the file, rather than expecting the model to remember it from the conversation history.

#### Attention Hygiene for Founders

1. **Batch your communications.** Check email and Slack two or three times a day at fixed times, not continuously. Each check is a context switch.
2. **Use a single task list.** Do not keep your todos in your head, in your phone, in your laptop, and in a notebook. One list, one place. Every time you write a thought down in the right place, you free up working memory for the current task.
3. **Protect your deep work block.** If your peak attention hours are 8 AM to 12 PM, those four hours are for the highest-leverage task. No email, no meetings, no Slack. Phone in another room.
4. **Take real breaks.** A ten-minute walk outside resets attention better than ten minutes of scrolling. The default mode network, the brain system that activates during rest, is what consolidates what you learned during the focused block.
5. **End the day by writing tomorrow's first task.** This eliminates the morning decision of "what do I do first," which is an attention drain. You sit down and do the thing you already decided to do.
