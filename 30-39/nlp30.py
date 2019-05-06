def get_morph():
    with open("neko.txt.mecab") as f:
        lines = f.readlines()

    sentences = []
    sentence = []
    for line in lines:
        line = line.rstrip()

        if line == 'EOS':
            sentences.append(sentence)
            sentence = []
        else:
            surface, rest = line.split('\t')

            morph = rest.split(',')
            pos = morph[0]
            pos1 = morph[1]
            base = morph[6]

            sentence.append({
                "surface": surface,
                "base": base,
                "pos": pos,
                "pos1": pos1,
            })

    return sentences

if __name__ == '__main__':
    print(get_morph())
