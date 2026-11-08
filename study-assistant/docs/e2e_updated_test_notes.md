## Introduction

Previous tests showed that there was inconsistency in answering by gemini. Even though there was enough information, it wasn't included in answer.
To address this issue, instruction provided to Gemini was updated to provide completeness and consistency.

## Changes made

Added additional instruction in `prompt_build.py` as:

```text
Include all important details from the relevant context that help answer the question.
Do not omit key points just to make the answer shorter.
```

## Test Question Types

Same question types used in initial testing were reused.
Refer to `end_to_end_test_notes` for their description

## Testing and Comparison

| Question Type                | Question                                                | Changes Seen | Result | Improvement                                                             |
| ---------------------------- | ------------------------------------------------------- | ------------ | ------ | ----------------------------------------------------------------------- |
| Clearly Answerable Questions | What is database index?                                 | Yes          | Pass   | Now described different property like usage, benifits and drawbacks.    |
| Plain-Language Paraphrase    | How can I find database records faster?                 | No           | Pass   | N/A                                                                     |
| Confusable Question          | What is the difference between a stack and a queue?     | No           | Pass   | N/A                                                                     |
| Related Concepts             | How does a hash function work, and what is a collision? | Yes          | Pass   | Hashing, distribution, consistency, collision, both handling techniques |
| Unanswerable Question        | What is gradient descent?                               | No           | Pass   | N/A                                                                     |

## Conclusion

After updating the instruction, the system demonstrated improved answers with completeness using relevent information from context with fewer omissions. Questions unrelated to study materials are still identified as not answerable

All tested question types passed, showing that  the prompt improvements did improve the answer completeness issues while maintaining existing answering
