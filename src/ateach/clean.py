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

    # replace more than one space with a tab
    text = re.sub(r'\s{2,}', '\t', text)

    # remove all non-text characters except punctuation marks,
    # newlines and tabs
    # text = re.sub(r'[^\w\s\.\'\-,\n\t]', '', text)

    # remove leading and trailing spaces
    text = text.strip()

    # replace any remaining consecutive spaces with a single space
    text = re.sub(r'\s+', ' ', text)

    # replace any remaining consecutive tabs with a single tab
    text = re.sub(r'\t+', '\t', text)

    # replace any remaining '\f' characters with '\n'
    text = text.replace('\f', '\n')

    return text
