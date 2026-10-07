---
layout: page
title: "Temporal Learning"
---

# [Astartup Cookbook](../)

## [Psychology](./)

### Temporal Learning

Temporal learning is the process of encoding information with a time component: not just what happened, but when it happened, how long it took, and what the sequence was. The brain learns sequences, and the strength of the learning depends on the timing of the repetitions.

For a startup founder, temporal learning matters in three contexts: learning a new technology, learning a new market, and learning the rhythm of your own work.

#### Spaced Repetition

The most well-established principle of temporal learning is spaced repetition. Information reviewed at increasing intervals is retained longer than information reviewed in a single session. The forgetting curve, described by Hermann Ebbinghaus in 1885, shows that without review, you forget roughly 70 percent of new information within twenty-four hours. A single review at the twenty-four-hour mark resets the curve. A second review at the three-day mark resets it again. Each review extends the retention period.

Practical application for a founder learning a new technology:

1. **Day 1:** Read the documentation. Build a small example. Write down the key concepts in your own words.
2. **Day 3:** Without looking at the documentation, explain the key concepts from memory. Fill in the gaps.
3. **Day 7:** Build a slightly larger example that uses the concepts in a new context.
4. **Day 30:** Use the technology in a real project. The real project is the final review.

The key is that the reviews are active, not passive. Re-reading the documentation is passive. Explaining the concept from memory, building the example, using the technology in a project, these are active. Active retrieval is what strengthens the memory trace.

#### Interleaving

Interleaving is the practice of mixing different types of problems or skills in a single study session, rather than blocking all the practice of one type before moving to the next. The brain learns the discrimination between types as well as the execution of each type.

For a founder, interleaving means: do not spend an entire week on backend development and then an entire week on frontend development. Mix them. A morning of backend, an afternoon of frontend, a morning of customer interviews, an afternoon of deployment. The switching cost is real, but the learning benefit is larger. You learn when to use each skill and how the skills interact, which is the knowledge that actually matters when you are building a product.

The exception: do not interleave during a deep work block. If you are in flow on a complex algorithm, do not switch to writing marketing copy in the middle of it. Interleaving is for the session level, not the task level. Switch between projects and skill types between sessions, not within a flow state.

#### Timing and the Workday

The time of day you learn matters. For most people, the brain is most receptive to new information in the morning, after a good night of sleep. The consolidation that happens during sleep is what makes the previous day's learning available for the next day's review.

Practical application:

1. **Learn new things in the morning.** The documentation reading, the tutorial following, the concept study. The brain is fresh and the encoding is strong.
2. **Execute in the afternoon.** The coding, the writing, the building. The afternoon is for applying what you learned in the morning, not for learning new things.
3. **Review before sleep.** A five-minute review of what you learned that day, done before bed, significantly improves retention. The review triggers the consolidation process that runs during sleep.

This is the temporal structure of a learning day: learn in the morning, execute in the afternoon, review at night. The sequence matters as much as the content.

#### Local LLM and Temporal Learning

When using a local LLM to learn a new technology, the model is a reference, not a teacher. The model can explain a concept, generate an example, or answer a question, but it does not schedule your reviews. The spaced repetition is your responsibility.

The practical workflow:

1. Ask the local LLM to explain the concept. Read the explanation. Write the key points in your own words in a markdown file.
2. Three days later, without looking at the explanation, write what you remember. Compare your notes to the original. Fill in the gaps.
3. Ask the local LLM to generate a practice problem. Solve it. Check your solution against the model's solution.
4. A week later, use the concept in a real task. The real task is the final test.

The local LLM is available for step 1, step 3, and step 4. It is not available for step 2, which requires you to retrieve from memory without the model's help. The retrieval is the learning. The model is the answer key, not the student.
