def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:  # file is created or truncated
        nb_chars = f.write(text)  # returns number of characters written [web:7]
    return nb_chars
