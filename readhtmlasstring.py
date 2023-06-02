def readhtmlasstring(filename):
    with open(filename, "r", encoding="utf-8") as file:
        html_text = file.read()
    return html_text
