# Two-Sentence Horror entry: writes the story to entry.txt and prints it.
import os

STORY = "The baby monitor crackled at three in the morning and my daughter, who had died in that room eleven years ago, whispered that she was cold. I ran upstairs with her blanket, and found the crib empty, the window open, and small wet footprints leading from the hallway to my bed."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY + "\n")
    print(STORY)


if __name__ == "__main__":
    main()
