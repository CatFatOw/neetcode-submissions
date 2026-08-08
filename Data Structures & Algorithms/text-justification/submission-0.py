class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def justify(curr_text, maxWidth):
            char_remaining = maxWidth - len("".join(curr_text))
            gaps = len(curr_text)-1
            if gaps == 0:
                return curr_text[0] + " " * (char_remaining)
            else:
                out = [curr_text[0]]
                bare_spaces = char_remaining // gaps 
                extra_spaces = char_remaining % gaps 

                for i in range(1, len(curr_text)):
                    out.append(" " * (bare_spaces + (1 if i-1 < extra_spaces else 0 ))) 
                    out.append(curr_text[i])
             
                return "".join(out)


        # sliding window portion
        out = []
        curr_text = []

        for right in range(len(words)):
            curr_text.append(words[right])

            # Minimum widtrh
            if len("".join(curr_text)) + len(curr_text) - 1 > maxWidth:
                word = curr_text.pop()
                # call the function
                out.append(justify(curr_text, maxWidth))
                curr_text = [word]

                
        out.append(" ".join(curr_text).ljust(maxWidth))
        return out 
