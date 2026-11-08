def build_prompt(question, chunks):
    instruction = """
        Answer the question using only the provided context.
        If the context supports only part of the question, answer that part.
        For any part that cannot be answered from the context, say
        "Not enough context to answer this part."
        Do not invent facts or use outside knowledge.
        Include all important details from the relevant context that help answer the question.
        Do not omit key points just to make the answer shorter.
    """

    context = ""

    for i, chunk in enumerate(chunks, start=1):
        context += f"[Chunk {i}]\n{chunk}\n\n---\n\n"

    prompt = f"""
        {instruction}

        Context:
        {context}

        Question:
        {question}
    """

    return prompt
