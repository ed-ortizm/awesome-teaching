"""
Functions for cleaning text from pdf slides of
the programming course.
The text is generated with the linux command:
    pdftotext -layout -nopgbrk <input.pdf> <output.txt>
"""
import re


def clean_text(text: str) -> str:
    """
    Clean the text from the pdf slides of the programming course.
    """

    # remove leading and trailing spaces
    text = text.strip()

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)

    # Remove line breaks
    # text = text.replace('\n', ' ')
    return text
