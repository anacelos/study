def main():
    """
    Apply the convert function in a input.
    """

    seq = input()
    result = convert(seq)

    print(result)

def convert(seq):
    """
    Convert :) and :( in emojis.
    """

    seq = seq.replace(":)", "🙂")
    seq = seq.replace(":(", "🙁")

    return seq

main()