def split(s):
    return s

def main():
    in_file = open("split.txt")
    for line in in_file:
        line = line.strip()
        print split(line)

if __name__=="__main__":
    main()
