def read_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def save_summary(summary, file_path):
    with open(file_path, 'w') as file:
        file.write(summary)
