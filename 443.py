class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            c = chars[read]
            count = 0

            while read < len(chars) and chars[read] == c:
                count += 1
                read += 1

            chars[write] = c
            write += 1
            if count > 1:
                for d in str(count):
                    chars[write] = d
                    write += 1
        return write 
