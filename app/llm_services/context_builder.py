from app.models.search.search_result import SearchResult


class ContextBuilder:

    @staticmethod
    def build(
        search_results: list[SearchResult]
    ) -> str:

        sections = []

        for index, result in enumerate(search_results, start=1):

            sections.extend(
                [
                    f"[Document {index}]",
                    f"File: {result.filename}",
                    f"Pages: {result.start_page}-{result.end_page}",
                    "",
                    result.text,
                    ""
                ]
            )

        return "\n".join(sections)