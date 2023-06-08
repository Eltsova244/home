def main():
    s = input()
    print(convert(s))
def convert(s):
    s = s.replace (":)","\N{Slightly Smiling Face}")
    s = s.replace (":(","\N{Slightly Frowning Face}")
    return(s)
main()