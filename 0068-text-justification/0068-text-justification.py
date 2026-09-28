class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        cur_line = []
        cur_length = 0

        for word in words:
            # Check if adding the word (plus 1 mandatory space per existing word) exceeds maxWidth
            if cur_length + len(word) + len(cur_line) > maxWidth:
                # Calculate total spaces needed
                total_spaces = maxWidth - cur_length
                
                # Case 1: Only 1 word in line -> Left-justify
                if len(cur_line) == 1:
                    res.append(cur_line[0] + ' ' * total_spaces)
                else:
                    # Case 2: Fully justify (distribute extra spaces left-to-right)
                    spaces_between = total_spaces // (len(cur_line) - 1)
                    extra_spaces = total_spaces % (len(cur_line) - 1)
                    
                    line_str = ""
                    for i in range(len(cur_line) - 1):
                        # Give +1 extra space to leftmost slots if extra_spaces > 0
                        space_count = spaces_between + (1 if i < extra_spaces else 0)
                        line_str += cur_line[i] + ' ' * space_count
                    
                    line_str += cur_line[-1]
                    res.append(line_str)
                
                # Reset for next line
                cur_line = []
                cur_length = 0
            
            cur_line.append(word)
            cur_length += len(word)
        
        # Last line: Left-justify with single spaces, then right-pad remaining space
        last_line = ' '.join(cur_line)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)
        
        return res