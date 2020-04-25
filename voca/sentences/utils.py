
def wordtype2group(word_type):
    if "Verb" in word_type:
        return "verb"
    if "Noun" in word_type:
        return "noun"
    if "Unk" in word_type:
        return "unk"
    return "misc"
