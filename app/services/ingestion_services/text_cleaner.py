import re


class TextCleaner:
    """
    Cleans raw text extracted from PDF documents before sentence splitting.

    Responsibilities:
    - Normalize Unicode characters
    - Remove standalone page numbers
    - Remove table-of-content dot leaders
    - Remove bullet characters
    - Remove table of contents pages
    - Normalize whitespace
    """

    MULTIPLE_SPACES = re.compile(r"\s+")
    MULTIPLE_NEWLINES = re.compile(r"\n{2,}")
    PAGE_NUMBER_ONLY = re.compile(r"^\s*\d+\s*$", re.MULTILINE)
    DOT_LEADERS = re.compile(r"\.{4,}")
    CONTROL_CHARACTERS = re.compile(r"[\x00-\x1F\x7F]")
    NON_PRINTABLE = re.compile(r"[^\x20-\x7EÀ-ÿ\n]")
    HYPHENATED_WORD = re.compile(r"(\w)-\s+(\w)")

    # Common bullet characters found in PDFs
    BULLET_CHARACTERS = [
        "•",
        "●",
        "◦",
        "▪",
        "■",
        "►",
        "▸",
        "◆",
        "◇",
        "",
        ""
    ]

    @classmethod
    def _fix_hyphenated_words(cls, text: str) -> str:
        return cls.HYPHENATED_WORD.sub(r"\1\2", text)

    @classmethod
    def _remove_control_characters(cls, text: str) -> str:
        return cls.CONTROL_CHARACTERS.sub(" ", text)

    @classmethod
    def clean(cls, text: str) -> str:
        """
        Clean extracted PDF text.
        """

        if not text:
            return ""



        text = cls._remove_control_characters(text)
        text= cls._remove_non_printable(text)
        text = cls._fix_hyphenated_words(text)
        text = cls._normalize_unicode(text)
        text = cls._remove_table_of_contents(text)
        text = cls._remove_page_numbers(text)
        text = cls._remove_dot_leaders(text)
        text = cls._remove_bullets(text)
        text = cls._normalize_whitespace(text)

        return text.strip()

    @classmethod
    def _remove_non_printable(cls, text: str) -> str:
        return cls.NON_PRINTABLE.sub(" ", text)

    @staticmethod
    def _normalize_unicode(text: str) -> str:
        """
        Normalize common Unicode punctuation.
        """

        return (
            text
            .replace("“", "\"")
            .replace("”", "\"")
            .replace("’", "'")
            .replace("–", "-")
            .replace("—", "-")
            .replace("…", "...")
        )

    @classmethod
    def _remove_page_numbers(cls, text: str) -> str:
        """
        Remove lines that contain only page numbers.
        """

        return cls.PAGE_NUMBER_ONLY.sub("", text)

    @classmethod
    def _remove_dot_leaders(cls, text: str) -> str:
        """
        Replace long sequences of dots used in tables of contents.
        """

        return cls.DOT_LEADERS.sub(" ", text)

    @classmethod
    def _remove_bullets(cls, text: str) -> str:
        """
        Remove PDF bullet symbols while preserving the text.
        """

        for bullet in cls.BULLET_CHARACTERS:
            text = text.replace(bullet, "")

        return text

    @staticmethod
    def _remove_table_of_contents(text: str) -> str:
        """
        Remove pages that are primarily a table of contents.

        This is intentionally conservative to avoid deleting legitimate
        content that merely mentions the phrase "Table of Contents".
        """

        lower = text.lower()

        if "table of contents" not in lower:
            return text

        lines = text.splitlines()

        toc_lines = 0

        for line in lines:

            line = line.strip()

            if not line:
                continue

            # Detect common TOC patterns:
            #
            # Travel Tips...................4
            # Museums 12
            # Paris Airports 13
            #
            if (
                re.search(r"\d+\s*$", line)
                or "table of contents" in line.lower()
            ):
                toc_lines += 1

        # If most lines look like TOC entries,
        # discard the page.
        if lines and toc_lines / len(lines) > 0.5:
            return ""

        return text

    @classmethod
    def _normalize_whitespace(cls, text: str) -> str:
        """
        Normalize whitespace.
        """

        text = cls.MULTIPLE_NEWLINES.sub("\n", text)
        text = cls.MULTIPLE_SPACES.sub(" ", text)

        return text