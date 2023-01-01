import logging

class TextFileHandler:
    """
    Class that will abstract the IO to text files.
    """

    @classmethod
    def read_text_file(cls, path: str) -> str:
        """
        Reads the content of a (hopefully) text file and returns it as a string.

        :param path: Path to text file
        :type path: str
        :return: The string that was read
        :rtype: str
        """
        try:
            with open(path, encoding="utf-8") as f:
                text = f.read()
                logging.info("File read successfully.")
                return text
        except Exception as e:
            logging.error("Problen reading file.")
            logging.error(e)

    @classmethod
    def write_to_text_file(cls, path: str, filename: str, text: str) -> bool:
        """
        Writes a string object to a text file. The file is not supposed to exist.

        :param path: Path to the directory the text file will be in
        :type path: str
        :param filename: Name of the file (e.g. transcription, hl7_output, spellcheck...)
        :type filename: str
        :param text: Content of the text file
        :type text: str
        :return: Whether the operation was successfull
        :rtype: bool
        """
        try:
            with open(f"{path}/{filename}.txt", "w", encoding="utf-8") as f:
                f.write(text)
                logging.info("String written successfuly.")
                return True
        except Exception as e:
            logging.error(f"Error writing {filename} to file.")
            logging.error(e)
        return False
