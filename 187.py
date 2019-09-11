## Grant Gasser
## Leetcode 187 Repeated DNA Sequences
## 9/11/19

def findRepeatedDnaSequences(s):
    """
    Finds 10-letter sequences that appear >= 2 times

    Args:
        s (string): string of chars 'A', 'T', 'C', 'G'

    Returns:
        two_or_more (list): list of the 10-letter subsequences
    """

    # empty string or string < 10 chars
    if s == '' or len(s) < 10:
        raise ValueError("String must be of length 10+. String: '{}' is too small.".format(s))

    ten_letter_counts = {}
    two_or_more = set()

    i = 0
    while (i + 10) <= len(s):
        # get 10 letter substring
        sub = s[i:i+10]

        # get current count, if not seen before, set count to 1
        ten_letter_counts[sub] = ten_letter_counts.get(sub, 0) + 1

        # check if occures >= 2
        if ten_letter_counts[sub] >= 2:
            two_or_more.append(sub)


        i += 1

    return two_or_more

def main():
    print(findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))

main()
