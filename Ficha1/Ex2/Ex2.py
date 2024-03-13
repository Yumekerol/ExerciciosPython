def find_anagrams(word, words):
    anagrams = []
    for _word in words:
        if sorted(_word) == sorted(word):
            anagrams.append(word)
            print(word + " é anagrama")


def read_file(path):
    """
    Função que lê um ficheiro de texto e retorna uma lista de palavras
    """
    words = []
    f = open(path, "r")
    for x in f:
        x = x.strip()
        words.append(x)
    return words


def main():
    word = input("Escolha uma palavra: ")
    words = read_file("dictionary.txt")
    find_anagrams(word, words)


# Chamada da função principal
main()
