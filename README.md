# Project Zomboid Save File Scanner

A command-line tool to search through Project Zomboid save files for specific text patterns and locate them on the map.

## Features

- Search through Project Zomboid save files for specific text patterns
- Supports multiple save files and game modes
- Provides direct links to found locations on the Project Zomboid online map
- Case-insensitive search
- Handles binary map files safely

## Requirements

- Python 3.6+
- Project Zomboid save files in their default location

## Installation
Clone this repository:
```bash
git clone https://github.com/benjibobs/zomboid-item-scan.git
cd zomboid-item-scan
```

## Usage

Run the script using Python:

```bash
python main.py
```

Follow the prompts to:
1. Enter a search term
2. Filter save files by name
3. Select game mode (defaults to "Survivor")
4. Choose from available save files

The tool will display:
- Coordinates where matches were found
- Items that matched your search
- Direct links to locations on the Project Zomboid map

## Project Structure

- `main.py` - Entry point and CLI interface
- `SaveFileManager.py` - Handles save file and directory operations
- `FileParser.py` - Processes binary map files
- `SearchEngine.py` - Coordinates search operations and formats results

## Acknowledgments

- [Project Zomboid](https://projectzomboid.com/)
- [Project Zomboid Map Project](https://map.projectzomboid.com/)