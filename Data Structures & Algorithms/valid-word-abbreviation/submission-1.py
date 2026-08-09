class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        # i points to the current character in word
        i = 0

        # j points to the current character in abbreviation
        j = 0

        # Continue while both pointers are inside their strings
        while i < len(word) and j < len(abbr):

            # ------------------------------------------------
            # CASE 1:
            # Current abbreviation character is a LETTER.
            #
            # Example:
            #
            # word = "apple"
            # abbr = "a3e"
            #        ↑
            #
            # We simply compare the two characters.
            # ------------------------------------------------
            if abbr[j].isalpha():

                # The characters must be the same.
                if word[i] != abbr[j]:
                    return False

                # Move to the next character in both strings.
                i += 1
                j += 1

            # ------------------------------------------------
            # CASE 2:
            # Current abbreviation character is a NUMBER.
            #
            # Example:
            #
            # abbr = "a12e"
            #          ↑
            #
            # We need to skip 12 characters in word.
            # ------------------------------------------------
            else:

                # Leading zero is not allowed.
                #
                # Example:
                # "a01b" ❌
                #
                # Because the number starts with 0.
                if abbr[j] == '0':
                    return False

                # This will store the number.
                number = 0

                # The number may contain multiple digits.
                #
                # Example:
                #
                # "12"
                #
                # First digit = 1
                # number = 1
                #
                # Next digit = 2
                # number = 1*10 + 2
                #        = 12
                while j < len(abbr) and abbr[j].isdigit():

                    number = number * 10 + int(abbr[j])

                    # Move to the next digit.
                    j += 1

                # Skip 'number' characters in word.
                i += number

        # ------------------------------------------------
        # Both strings must finish exactly.
        #
        # If word still has characters left,
        # abbreviation was too short.
        #
        # If abbr still has characters left,
        # abbreviation was invalid/too long.
        # ------------------------------------------------
        return i == len(word) and j == len(abbr)