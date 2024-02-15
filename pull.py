import os


def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Se lanza desde el trigger pull_request!")


if __name__ == "__main__":
    main()
