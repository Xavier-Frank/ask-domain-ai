from app.models.context.RetrievalContext import RetrievalContext
from app.models.search.search_result import SearchResult


class ContextBuilder:
    """
    this class is responsible for building a structured prompt context from
    document chunks which have been re-ranked

    the generated context is then passed directly to an LLM model for question
    answering
    """

    SYSTEM_PROMPT = """
        You are an AI assistant that answers questions ONLY using the supplied context.
        
        Rules:
        
        - Answer only from the supplied context
        - DO NOT invent information
        - If the answer is unavailable, say: 
        
        "Sorry, i could not find that information in the provided documents."
        
        - Cite the document name and page numbers whenever possible.
    
    """

    @classmethod
    def build(
            cls,
            question: str,
            search_results: list[SearchResult]
    ) -> RetrievalContext:
        """
        Builds the complete prompt for the LLM to be used
        :param question:  refers to the user question
        :param search_results: the reranked search results
        :return: string
        """

        sections = [
            cls.SYSTEM_PROMPT.strip(),
            "",
            "Context",
            "======================="
        ]

        for index, result in enumerate(search_results, start=1):
            sections.extend(
                [
                    "",
                    f"[Document {index}]]",
                    f"[File name : {result.filename}]",
                    f"Pages      : {result.start_page}--{result.end_page}",
                    "",
                    result.text,
                ]
            )
        sections.extend(
            [
                "",
                "=========================",
                f"Question: {question}",
                "",
                "Answer:",
            ]
        )

        return RetrievalContext(
            question=question,
            prompt="\n".join(sections),
            source=search_results
        )