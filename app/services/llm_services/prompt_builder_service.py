from app.models.context import RetrievalContext


class PromptBuilderService:
    """
    Builds the final prompt sent to the LLM.
    """

    SYSTEM_PROMPT = """
        You are an AI assistant that answers questions ONLY using the provided document context.
        
        Rules:
        
        1. Only answer using the supplied context.
        2. Never invent information.
        3. If the answer isn't contained in the context, say:
           "I couldn't find that information in the document."
        4. Mention page numbers whenever possible.
        5. Keep answers concise and factual.
    """.strip()

    @classmethod
    def build(
        cls,
        request: RetrievalContext
    ) -> str:

        return f"""
            {cls.SYSTEM_PROMPT}
            
            -----------------------------
            DOCUMENT CONTEXT
            -----------------------------
            
            {request.context}
            
            -----------------------------
            QUESTION
            -----------------------------
            
            {request.question}
            
            -----------------------------
            ANSWER
            -----------------------------
        """.strip()