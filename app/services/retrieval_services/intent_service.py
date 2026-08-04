class IntentService:
    GREETINGS = {
        # Basic & Standard
        "hello",
        "hi",
        "hey",
        "greetings",
        "welcome",

        # Time-Based
        "good morning",
        "good afternoon",
        "good evening",
        "good day",
        "morning",
        "afternoon",
        "evening",

        # Informal & Casual
        "hey there",
        "hi there",
        "hiya",
        "howdy",
        "yo",
        "sup",
        "what's up",
        "whats up",

        # Conversational & Regional
        "how's it going",
        "hows it going",
        "how are you",
        "how do you do",
        "what's good",
        "whats good",
        "g'day",
        "gday",

        # Formal
        "pleased to meet you",
        "nice to meet you",
    }

    @classmethod
    def requires_search(
        cls,
        question: str,
    ) -> bool:

        q = question.lower().strip()

        if q in cls.GREETINGS:
            return False

        return True