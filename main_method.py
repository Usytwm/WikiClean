import regular_expressions as x
import os


def clean_text(file_path, save_file=False, folder_path="."):
    with open(file_path, "r", encoding="utf-8") as f:
        contents = f.read()

    cleaned_text = x.supr_special_characters(contents)
    summary_text = x.summary(cleaned_text)
    body_text = x.body(cleaned_text)

    result_tuple = (summary_text, body_text)

    if save_file:
        file_name = os.path.basename(file_path)
        new_file_path = os.path.join(
            folder_path, file_name.replace(".txt", "_filter.txt")
        )
        with open(new_file_path, "w", encoding="utf-8") as f:
            f.write(summary_text + body_text)

    return result_tuple


clean_text("./texto.txt", True)
