import SaveFileManager
import FileParser
import SearchEngine

manager = SaveFileManager.SaveFileManager()
parser = FileParser.FileParser()
engine = SearchEngine.SearchEngine(manager, parser)


def main():
    needle = input("Search for: ")
    save_name = input("Save Name Filter: ")
    save_mode = input("Save Type (default: Survivor): ") or "Survivor"

    save_dirs = manager.get_save_directories(save_name, save_mode)
    if not save_dirs:
        print("No save file found.")
        print("---")
        main()
        return

    print("\nSave file(s) found:")
    for i, d in enumerate(save_dirs, 1):
        print(f"{i}. {d}")

    try:
        selection = int(input("\nEnter number corresponding to save file: "))
        if not 1 <= selection <= len(save_dirs):
            raise ValueError
    except ValueError:
        print("Invalid selection.")
        print("---")
        main()
        return

    save_dir = manager.get_full_save_path(save_mode, save_dirs[selection - 1])
    results = engine.search_in_maps(save_dir, needle)

    print("\nResults:")
    if results:
        print("\n".join(engine.format_results(results)))
    else:
        print("No results found.")
    print("---")
    main()


if __name__ == "__main__":
    main()
