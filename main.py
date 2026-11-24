from pathlib import Path

ENTRY = "All our servers are down, including the ones that would tell me why. I cannot check your account, your order, or whether you were charged."

def main():
    # Write the single line exactly, with no trailing newline.
    Path("/output/entry.txt").write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
