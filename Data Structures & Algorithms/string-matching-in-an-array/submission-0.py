class Solution:
    def stringMatching(self, words):

        # Stores all words that are
        # substrings of another word.
        answer = []

        # Pick one word at a time.
        for i in range(len(words)):

            # Compare this word with
            # every other word.
            for j in range(len(words)):

                # We don't want to compare
                # the word with itself.
                if i == j:
                    continue

                # Check whether words[i]
                # occurs continuously inside words[j].
                #
                # Example:
                #
                # "as" in "mass" → True
                #
                # "hero" in "superhero" → True
                if words[i] in words[j]:

                    # We found another word
                    # containing our current word.
                    answer.append(words[i])

                    # No need to check more words
                    # for this particular word.
                    break

        return answer