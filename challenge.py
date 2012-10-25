def wordlist():
    words_file = open("words.txt")
    words = set()
    for line in words_file:
        words.add(line.strip().lower())
    return words

words = wordlist()

def split(s):
    s = s.lower()
    s = s.replace(" ", "")
    if s in words:
        return [s]
    else:
        for i in range(1,len(s)):
            if s[:i] in words:
                other = split(s[i:])
                if other:
                    return [s[:i]]+other
    return None


def main():
    in_file = open("split.txt")
    for line in in_file:
        line = line.strip()
        print split(line)

if __name__=="__main__":
    main()
