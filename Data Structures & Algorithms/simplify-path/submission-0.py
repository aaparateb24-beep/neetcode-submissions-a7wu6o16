class Solution:

    def simplifyPath(self, path: str) -> str:

        # Stack stores folder names
        #
        # Example:
        # ["home","user","docs"]
        stack = []

        # Break path into pieces
        #
        # "/home/user/docs"
        #
        # becomes
        #
        # ["","home","user","docs"]
        folders = path.split("/")

        # Visit every folder
        for folder in folders:

            # -----------------------
            # Ignore empty strings
            #
            # ""
            #
            # Ignore current folder
            #
            # "."
            # -----------------------
            if folder == "" or folder == ".":
                continue

            # -----------------------
            # Go back one folder
            # -----------------------
            elif folder == "..":

                # Go back only if possible
                if stack:
                    stack.pop()

            # -----------------------
            # Normal folder
            #
            # Enter folder
            # -----------------------
            else:

                stack.append(folder)

        # Build final path
        #
        # ["home","user"]
        #
        # becomes
        #
        # "/home/user"
        return "/" + "/".join(stack)

        