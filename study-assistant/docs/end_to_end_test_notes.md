# End to End Testing

## Test Questions Types

* **Clearly Answerable Question:**  Question that can be directly answered using the provided chunks.
* **Plain-Language Paraphrase:** Question expressed differently from the wording.
* **Confusable Question:** A question involving similar or easily confused concepts.
* **Related Concepts:** A question involving multiple related concepts.
* **Unanswerable Question:** Question that doesnt have any explaination in provided chunks.

## Testing and Observation

| Question Type                | Question                                                | Retrieved Chunks and Similarity<br />Scores                                                | Result       | Answer                                                    | Observation                                                    |
| ---------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------ | --------------------------------------------------------- | -------------------------------------------------------------- |
| Clearly Answerable Questions | What is database index?                                 | Database indexes (0.8901)<br /> SQL queries (0.4242)<br />Primary keys (0.3902)            | Partial pass | Described in one sentence                                 | Answered in less detail than expected, less than in question 2 |
| Plain-Language Paraphrase    | How can I find database records faster?                 | Database indexes (0.4673)<br />Binary search (0.3565)<br />SQL queries (0.3293)            | Pass         | Gave answer i.e. database index and desctibed it in brief | Understood relevent context though phrased differently         |
| Confusable Question          | What is the difference between a stack and a queue?     | Queue data structure (0.5517)<br />Stack data structure (0.5051)<br />SQL queries (0.2616) | Pass         | Differentiated based on working and common uses           | Both chunks were used, difference given clearly                |
| Related Concepts             | How does a hash function work, and what is a collision? | Hash collisions (0.6990)<br />Hash functions (0.6973)<br />Binary search (0.2275)          | Partial pass | Just gave how it works and small definition               | Correctly explained and defined but lacked in explaination     |
| Unanswerable Question        | What is gradient descent?                               | Stack data structure (0.2533)<br />Binary search (0.1924)<br />Linear search (0.1864)      | Pass         | Not enough context                                        | Correctly identified unrelatable question                      |

## Conclusion

With this test, we can conclude that RAG pipeline can retrieve relevant answers and generate answers using Gemini. System handled different types of questions and phrasing and didnt give instructions when the information was insufficient.

However inconsistency was seen as some information was ommited even when the information was present. This indicates completeness and consistency are areas that can be improved

Overall, pipeline successfully showed the core RAG workflow, while improvements are needed to make it consistent
