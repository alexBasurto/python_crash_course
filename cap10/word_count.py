def count_words(filename):
    """Cuenta el número aproximado de palabras de un archivo."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        pass

    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['ralice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    count_words(f"cap10\{filename}")