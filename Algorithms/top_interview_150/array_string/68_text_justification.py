class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Try to determine words in each line, and then fill with spaces if needed.

        Time: O(n*maxWidth), essentially the total number of characters for joining them.
        Suppose maxWidth is 10, all words length is 8, essentially each word is a line,
        and the join function costs maxWidth per line
        Space: O(maxWidth) line contains at most maxWidth characters
        """
        res = []
        i = 0
        line = []
        line_len = 0
        while i < len(words):
            # each word will be preceeded with a space except for the first word
            extra_len = len(words[i]) if len(line) == 0 else len(words[i]) + 1
            if line_len + extra_len <= maxWidth:
                # put words[i] in the current line
                # if it is not the first word, need to append a space first
                if len(line) > 0:
                    line.append(" ")
                    line_len += 1
                line.append(words[i])
                line_len += len(words[i])

                # in case i is the last word
                if i == len(words) - 1:
                    num_spaces = maxWidth - line_len
                    if num_spaces > 0:
                        line.append(" " * num_spaces)
                    res.append("".join(line))
                    return res
                else:
                    # keep going
                    i += 1

            else:
                # need to finish the current line
                num_spaces = maxWidth - line_len
                # if there only one word, add spaces at the end
                if len(line) == 1:
                    line.append(" " * num_spaces)
                else:
                    while num_spaces > 0:
                        # extend spaces from left to fight until no more spaces needed
                        for j, item in enumerate(line):
                            if item.startswith(" "):
                                line[j] = item + " "
                                line_len += 1
                                num_spaces -= 1
                                if num_spaces == 0:
                                    break

                # append line to res and reset
                # don't increment i
                res.append("".join(line))
                line = []
                line_len = 0
