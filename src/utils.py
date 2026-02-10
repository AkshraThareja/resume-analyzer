def load_text(file_path):
    """
    Reads a text file and returns a list of cleaned, lowercase lines.
    """
    with open(file_path, "r") as file:
        return [line.strip().lower() for line in file if line.strip()]
