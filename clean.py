import os


def clean():
    # function to delete all files except .gitignore
    def delete_files_except_gitignore(folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file != ".gitignore":
                    os.remove(os.path.join(root, file))

    # folders to clean
    folders = ["audio", "audio_json", "subtitles"]

    # clean each folder
    for folder in folders:
        folder_path = os.path.join(os.getcwd(), folder)
        if os.path.exists(folder_path):
            delete_files_except_gitignore(folder_path)
        else:
            print(f"Folder '{folder}' does not exist.")

    print("Cleanup complete.")
