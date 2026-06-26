class Solution:
    def decodeString(self, s: str) -> str:

        # Stack stores:
        # (previous_string, repeat_count)
        #
        # Example:
        # [
        #   ("",3),
        #   ("a",2)
        # ]
        stack = []

        # Number before '['
        #
        # Example:
        # 3[a]
        #
        # current_num = 3
        current_num = 0

        # Current string we are building
        current_string = ""

        # Read every character one by one
        for char in s:

            # ---------------------------------------
            # CASE 1 : Digit
            #
            # Example:
            # "3"
            #
            # Save repeat count
            # ---------------------------------------
            if char.isdigit():

                # Handles multi-digit numbers too
                #
                # Example:
                # "12[a]"
                #
                # current_num:
                # 1
                # then 12
                current_num = current_num * 10 + int(char)

            # ---------------------------------------
            # CASE 2 : Opening Bracket
            #
            # Example:
            # 3[
            #
            # Save current work
            # ---------------------------------------
            elif char == "[":

                # Save previous string
                # and repeat count
                stack.append((current_string, current_num))

                # Start fresh for inner bracket
                current_string = ""

                current_num = 0

            # ---------------------------------------
            # CASE 3 : Closing Bracket
            #
            # Example:
            # ]
            #
            # Finish current block
            # ---------------------------------------
            elif char == "]":

                # Recover previous state
                previous_string, repeat = stack.pop()

                # Repeat current string
                #
                # Example:
                #
                # previous = "a"
                # repeat = 2
                # current = "c"
                #
                # "a" + "cc"
                current_string = previous_string + current_string * repeat

            # ---------------------------------------
            # CASE 4 : Normal Letter
            #
            # Example:
            # a
            # b
            # c
            # ---------------------------------------
            else:

                # Simply build current string
                current_string += char

        # Final decoded string
        return current_string
        