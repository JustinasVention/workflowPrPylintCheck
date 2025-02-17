import os
import random
import string

"""This module contains functions to generate random strings, 
write to and read from files, process data and print statistics."""


def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def write_to_file(filename, content):
    """Write content to a specified file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def read_from_file(filename):
    """Read content from a file."""
    if not os.path.exists(filename):
        print(f"Error: {filename} does not exist.")
        return ""

    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def process_data(data):
    """Process input data to create a summary."""
    word_count = len(data.split())
    char_count = len(data)
    return word_count, char_count


def main():
    """This function generates random content and processes it."""
    # Generate random content
    random_content = generate_random_string(100)
    filename = "sample_data.txt"

    # Write the random content to a file
    write_to_file(filename, random_content)

    # Read the content back from the file
    content = read_from_file(filename)

    if content:
        # Process the content and print statistics
        words, chars = process_data(content)
        print(f"Processed file: {filename}")
        print(f"Word count: {words}")
        print(f"Character count: {chars}")
    else:
        print("No content to process.")


if __name__ == "__main__":
    main()

