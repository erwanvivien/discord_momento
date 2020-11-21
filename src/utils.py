def get_content(file):
    file = open(file, "r")
    return file.read()


def author_name(author):
    return author.name if not author.nick else author.nick
