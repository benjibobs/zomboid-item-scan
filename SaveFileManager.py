import os
import re
from typing import List


class SaveFileManager:
    """
    Manages access to Project Zomboid save files and directories.

    This class handles operations related to finding and accessing save game directories
    and map files within the Project Zomboid saves folder structure.

    Attributes:
        saves_path (str): Path to the Project Zomboid saves directory
        map_pattern (re.Pattern): Compiled regex pattern for matching map file names

    Args:
        base_path (str, optional): Base path to Project Zomboid installation.
            Defaults to user's home directory.
    """

    def __init__(self, base_path: str = os.path.expanduser("~")):
        self.saves_path = os.path.join(base_path, "Zomboid", "Saves")
        self.map_pattern = re.compile(r"map_\d+_\d+\.bin$")

    def get_save_directories(self, name: str, mode: str = "Survivor") -> List[str]:
        """
        Find save directories matching the given name and game mode.

        Args:
            name (str): Name to filter save directories by
            mode (str, optional): Game mode to search in. Defaults to "Survivor"

        Returns:
            List[str]: List of matching directory names, empty if none found
                or if path doesn't exist
        """
        path = os.path.join(self.saves_path, mode)
        if not os.path.exists(path):
            return []
        return [
            d
            for d in os.listdir(path)
            if os.path.isdir(os.path.join(path, d)) and name.lower() in d.lower()
        ]

    def get_full_save_path(self, mode: str, save_dir: str) -> str:
        """
        Construct the full path to a save directory.

        Args:
            mode (str): Game mode folder name
            save_dir (str): Save directory name

        Returns:
            str: Complete path to the save directory
        """
        return os.path.join(self.saves_path, mode, save_dir)

    def get_map_files(self, save_dir: str) -> List[str]:
        """
        Get all map files in the specified save directory.

        Finds all files matching the pattern 'map_X_Y.bin' where X and Y are numbers.

        Args:
            save_dir (str): Path to the save directory to search in

        Returns:
            List[str]: List of map file names, empty if directory doesn't exist
        """
        if not os.path.exists(save_dir):
            return []
        return [f for f in os.listdir(save_dir) if self.map_pattern.match(f)]
