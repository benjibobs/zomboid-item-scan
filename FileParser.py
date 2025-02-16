import string
import re
from typing import List


class FileParser:
    """
    Parser for binary files containing text data.

    This class provides static methods to extract and process words from binary files,
    specifically designed to handle Project Zomboid map files that may contain
    UTF-8 encoded text mixed with binary data.
    """

    @staticmethod
    def get_words_from_file(file_path: str) -> List[str]:
        """
        Extract words from a binary file.

        Opens a binary file, attempts to decode it as UTF-8, and extracts words
        by removing punctuation and splitting on word boundaries.

        Args:
            file_path (str): Path to the binary file to parse

        Returns:
            List[str]: List of words found in the file, filtered to remove single
                characters. Returns empty list if file cannot be read.

        Note:
            - Ignores UTF-8 decode errors
            - Removes all punctuation and spaces
            - Only returns words with length > 1
        """
        try:
            with open(file_path, "rb") as file:
                binary = file.read()
                text = binary.decode("utf-8", errors="ignore").replace(" ", "")
                text = text.translate(str.maketrans("", "", string.punctuation))
                results = re.findall(r"\w+", text)
                return [word for word in results if len(word) > 1]
        except IOError:
            return []
