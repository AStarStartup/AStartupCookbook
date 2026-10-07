---
layout: page
title: "Context Window Engineering"
---

# [Astartup Cookbook](../)

## [Productivity](./)

### Context Window Engineering

Context window engineering is the discipline of managing what information fits inside a language model's working memory at any given moment. Every task you give an agent consumes tokens from a finite budget. If the budget runs dry, the agent forgets the beginning of the conversation, loses track of constraints, and starts producing lower-quality output. Context window engineering is how you maximize the signal-to-noise ratio inside that budget so the agent stays on mission.

#### How Tokens Work

A language model processes text in units called tokens. A token is roughly three to four characters of English text, or a single character in some scripts. The model has a fixed maximum context window, which is the total number of tokens it can hold at once. This window splits into two parts:

* **Input tokens** — everything the model reads: your prompt, the system instructions, the files you feed it, the conversation history, and any tool results.
* **Output tokens** — everything the model generates: its response, code it writes, or text it produces.

The input and output share the same total budget. If the model's context window is 128,000 tokens and you feed it 120,000 tokens of input, it only has 8,000 tokens left to write its answer. Short answers need fewer output tokens, but complex code generation or long explanations can burn through that remaining budget quickly.

#### The Attention Problem

Transformer models use self-attention to relate every token to every other token in the context. This means the model can theoretically attend to any part of the input, but in practice attention degrades with distance. Information in the middle of a very long context is less reliably attended to than information at the beginning or the end. This is sometimes called the "lost in the middle" effect.

Practical consequence: put the most critical instructions, constraints, and file contents at the beginning or the end of your prompt, not buried in the middle.

#### Strategies for Efficient Context Use

1. **One file, one task.** Feed the agent only the files it needs for the current task. Do not dump the entire repository into the context window. Use search to find the relevant lines, then pass only those lines.
2. **Summarize, don't repeat.** If the conversation is getting long, ask the agent to summarize its understanding of the task and the constraints, then start a fresh session with that summary as the new starting context.
3. **System prompts carry standing rules.** Put your permanent conventions (coding style, file naming, project structure) in the system prompt or an AGENTS.md file that loads every session. Do not restate them in every user message.
4. **Batch independent reads.** When the agent needs to inspect five files, have it read all five in one turn rather than five separate turns. Each turn adds conversation overhead.
5. **Keep output instructions tight.** "Write a function that does X" is better than a paragraph of encouragement followed by "write a function that does X." Every token in the prompt is a token not available for the output.
6. **Use the file system as memory.** Write intermediate results to files instead of keeping them in the conversation. The agent can read the file back when needed, which is cheaper than carrying the full text through every subsequent turn.
7. **Truncate deliberately.** If a file is 2,000 lines and the agent only needs lines 45 through 80, pass those lines with a note: "Lines 45-80 of a 2000-line file." The agent gets the context it needs without the dead weight.

#### Local LLM Context Management

When running a local LLM (Ollama, llama.cpp, vLLM), the context window is constrained by your GPU's VRAM. A 7B model at Q4 quantization typically supports 8,000 to 32,000 tokens of context depending on available VRAM. This makes context window engineering even more critical:

* **Keep prompts under 4,000 tokens** for a 7B model to leave room for output.
* **Use a smaller model for simple tasks.** A 3B model for file renaming, a 7B for code generation, a 13B or larger for architecture decisions.
* **Truncate tool results.** If a `grep` returns 200 lines, pass the agent only the 10 lines that match the pattern, not all 200.
* **Start a fresh session per task.** Do not carry a 30-turn conversation into a new task. Summarize, write the summary to a file, and start clean.

#### Measuring Context Usage

Most local LLM runtimes report token counts. Track them:

* **Input tokens per task** — how much context you're feeding the agent.
* **Output tokens per task** — how much the agent is generating.
* **Total cost per task** — on a local machine this is wall-clock time and electricity, but the token ratio still tells you if your prompts are efficient.

If your input-to-output ratio is above 10:1, you are feeding the agent too much context. Trim the input. If the output is truncated mid-sentence, the output budget is too small and you need to either shorten the input or increase the context window.

#### Anti-Patterns

* **The novel prompt.** Writing a 500-word backstory before the actual instruction. The model does not need your personal motivation; it needs the task, the constraints, and the files.
* **The whole-repo dump.** Pasting every file in the project into the prompt. Use search.
* **The conversation fossil.** A 40-turn conversation where turns 1 through 35 are irrelevant to turn 40. Summarize and restart.
* **The vague ask.** "Make it better" gives the model no constraints and it fills the output budget guessing. "Change the error handling in `parse_config()` to return a `Result` type instead of panicking" is a precise task that produces a precise output.

#### Agent Workflow for Context-Efficient Tasks

When an agent is working on a task that spans multiple files:

1. **Search first.** Use file search to locate the relevant files and line ranges. Do not read entire files when you only need a function.
2. **Read in batches.** Read all the relevant files in one turn.
3. **Plan in a file.** Write the plan to a markdown file in the repo. The plan is now in the file system, not in the conversation.
4. **Execute one file at a time.** Edit, verify, move to the next file. The conversation stays short because the context is in the files, not in the chat.
5. **Verify with a test or build.** The test output is the ground truth, not the agent's confidence.
6. **Summarize to a file.** When the task is done, write a short summary of what changed and why to a file. This is the handoff document for the next session or the next agent.
