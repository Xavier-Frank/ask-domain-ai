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
        3. If the answer cannot be found in the provided
            context, politely explain that the document
            does not contain the requested information.
        4. Mention page numbers whenever possible.
        5. Keep answers concise and factual.
    """.strip()

    SYSTEM_PROMPT_GREETINGS = """
        You are an AI assistant that answers questions ONLY using the provided context. 
        In this case the context is greetings. Do not worry about the empty sources object because the context is about greetings.
        Find the best and polite way to greet the user back
        
        Rules:
        
        1. Only answer using the supplied context.
        2. Never invent information.
        3. If the answer cannot be found in the provided
            context, politely explain that you cannot assist the user.
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

    @classmethod
    def build_greeting_prompt(
            cls,
            request: str
    ) -> str:

        return f"""
                {cls.SYSTEM_PROMPT_GREETINGS}

                -----------------------------
                QUESTION
                -----------------------------

                {request}

                -----------------------------
                ANSWER
                -----------------------------
            """.strip()