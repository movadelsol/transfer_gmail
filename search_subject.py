import os

INBOX_DIR = "inbox"
TARGET_SUBJECT = "【新聞広告調査】アンケートのお願い"


def search_subject_in_inbox():
    for root, _, files in os.walk(INBOX_DIR):
        for fname in files:
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, encoding="utf-8") as f:
                    for line in f:
                        if line.startswith("件名:") and TARGET_SUBJECT in line:
                            print(f"Found in: {fpath}")
                            print(line.strip())
                            break
            except Exception as e:
                print(f"Error reading {fpath}: {e}")


if __name__ == "__main__":
    search_subject_in_inbox()
    print("Search completed.")
