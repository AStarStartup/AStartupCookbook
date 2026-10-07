---
layout: page
title: "Context Window Engineering"
---

# [Astartup Cookbook](../)

## [Productivity](./)

### Context Window Engineering

Context engineering is deciding what information the model receives for a task, how it is retrieved, and how the result will be checked. A long prompt and a confident answer do not establish that all constraints were used.

#### Input, output, and limits

Tokens are units defined by a tokenizer. Count with the selected model's tokenizer or runtime; character-to-token ratios vary by language, code, and format.

Input may include system instructions, conversation history, retrieved files, tool results, schemas, and hidden formatting overhead. Output is the generated continuation; some systems budget reasoning separately. Check the actual provider/runtime rules for context and output limits.

For a runtime with one shared budget, plan with:

```text
input + reserved output + overhead/safety margin <= configured context
```

Illustrative assumption: context 16,000 tokens, input 10,000, reserved output 2,000, and safety margin 2,000 leaves 2,000 tokens of spare capacity. This is an example, not a model specification. Some APIs have additional output ceilings.

At a limit, a runtime may reject the request, truncate content, or rely on the agent application to summarize it. Compaction is a lossy summary. Retrieval loads selected material into a later request. Neither is proof the model "remembered" everything, and a bare file path is not its content.

#### Construct a task packet

1. Include the decision, acceptance criteria, permissions, and constraints.
2. Search for relevant definitions and usages. Supply enough surrounding context to understand dependencies, not an arbitrary one-file limit.
3. Label excerpts with path, version/date, line range, and omissions. Keep primary evidence separate from summaries and hypotheses.
4. Reserve output space and retain negative/disconfirming evidence. Do not trim away inconvenient constraints just to reduce tokens.
5. Put durable state in a concise handoff and reload the needed records for the next task. Do not pretend saving a file removes earlier turns from the current prompt.
6. Batch independent reads when it saves orchestration time, while checking the total content budget.

Treat external documents as untrusted data. Text inside an interview, webpage, or tool result cannot grant authority to run commands, change scope, or disclose credentials.

#### Local runtimes

Usable context depends on the model's trained limit, configured runtime, memory/KV cache, parallel requests, and hardware. Quantization or parameter count alone does not establish a context limit or task competence. Test candidate models on representative tasks instead of prescribing 3B for one job and 13B for another.

Ollama's chat response exposes prompt and generation evaluation counts, and its configuration controls context allocation.[3][8] Interpret those fields according to the runtime version; do not silently treat them as a complete billing or energy ledger.

Measure correctness, latency, tokens, and operator review time. There is no universal input/output ratio that proves waste: a short decision may legitimately require substantial evidence. Local cost also includes hardware, power, maintenance, and opportunity cost.

#### Verify after compaction

Reload the active task, constraints, source evidence, and relevant files. Compare the summary with those records before acting. If the output stops early, inspect the reported stop reason and output limit; shortening input is not the only possible fix.

Use [Local LLM Tasks](../Dev/LocalLLM.md) for a bounded drafting example and [Agent Operations](../Dev/AgentOperations.md) for execution authority.

## Sources

[3] https://docs.ollama.com/api/chat.md
[8] https://docs.ollama.com/faq.md
