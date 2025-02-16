from FileParser import FileParser
from SaveFileManager import SaveFileManager
import os
import re
from typing import List, Tuple


class SearchEngine:
    """
    Searches for text patterns in Project Zomboid map files.

    This class coordinates the searching of text patterns within map files using
    the SaveFileManager to locate files and FileParser to extract content.

    Attributes:
        save_manager (SaveFileManager): Manager for accessing save files
        file_parser (FileParser): Parser for extracting text from files

    Args:
        save_manager (SaveFileManager): Instance of SaveFileManager
        file_parser (FileParser): Instance of FileParser
    """

    def __init__(self, save_manager: SaveFileManager, file_parser: FileParser):
        self.save_manager = save_manager
        self.file_parser = file_parser

    def search_in_maps(self, save_dir: str, needle: str) -> List[Tuple[str, List[str]]]:
        """
        Search for a text pattern in all map files within a save directory.

        Args:
            save_dir (str): Path to the save directory containing map files
            needle (str): Text pattern to search for

        Returns:
            List[Tuple[str, List[str]]]: List of tuples containing:
                - Map file name (str)
                - List of matching words found in that file (List[str])
        """
        map_files = self.save_manager.get_map_files(save_dir)
        found_in = []

        for map_file in map_files:
            full_path = os.path.join(save_dir, map_file)
            matching_words = [
                c.lower()
                for c in self.file_parser.get_words_from_file(full_path)
                if needle.lower() in c.lower()
            ]
            if matching_words:
                found_in.append((map_file, matching_words))

        return found_in

    @staticmethod
    def format_results(results: List[Tuple[str, List[str]]]) -> List[str]:
        """
        Format search results into human-readable strings.

        Converts map coordinates into a format suitable for the Project Zomboid
        online map viewer and creates formatted output strings.

        Args:
            results (List[Tuple[str, List[str]]]): Search results from search_in_maps

        Returns:
            List[str]: Formatted strings containing:
                - Area coordinates
                - Matched items found
                - URL to online map viewer
        """
        formatted = []
        for map_file, words in results:
            map_coords = re.findall(r"\d+", map_file)
            coords = f"{map_coords[0]}0x{map_coords[1]}0"
            formatted.extend(
                [
                    f"Found in area with coords: {coords}",
                    f"(Matched items: {words})",
                    f"https://map.projectzomboid.com/#{coords}x512",
                    "",
                ]
            )
        return formatted
