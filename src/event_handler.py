import shutil
from datetime import date
from pathlib import Path
from watchdog.events import FileSystemEventHandler

from src.file_type_specifier import FileCategory, file_categories


def add_date_to_path(path: Path):
    """
    Helper function that adds current year/month to destination path. If the path
    doesn't already exist, it is created.
    :param Path path: destination root to append subdirectories based on date
    """
    dated_path = path / f'{date.today().year}' / f'{date.today().month:02d}'
    dated_path.mkdir(parents=True, exist_ok=True)
    return dated_path


def rename_file(source: Path, destination_path: Path):
    """
    Helper function that renames file to reflect new path. If a file of the same
    name already exists in the destination folder, the file name is numbered and
    incremented until the filename is unique (prevents overwriting files).
    :param Path source: source of file to be moved
    :param Path destination_path: path to destination directory
    """
    if Path(destination_path / source.name).exists():
        increment = 0

        while True:
            increment += 1
            new_name = destination_path / f'{source.stem}_{increment}{source.suffix}'

            if not new_name.exists():
                return new_name
    else:
        return destination_path / source.name


class EventHandler(FileSystemEventHandler):
    def __init__(self, watch_path: Path, destination_root: Path):
        self.watch_path = watch_path.resolve()
        self.destination_root = destination_root.resolve()
        self.file_category_specifier = FileCategory(file_categories)

    def on_modified(self, event):
        self.move_files()

    def move_files(self):
        print(f'Checking and moving files')
        moved_file_count = 0
        ignored_file_count = 0
        for child in self.watch_path.rglob('*'):
            suffix = child.suffix.lower()
            # skips directories and non-specified extensions
            category = self.file_category_specifier.get_file_category(suffix)
            if child.is_file() and category is not None:
                destination_path = self.destination_root / category
                destination_path = add_date_to_path(path=destination_path)
                destination_path = rename_file(source=child, destination_path=destination_path)
                moved_file_count += 1
                shutil.move(src=child, dst=destination_path)
                if moved_file_count % 100 == 0:
                    print(f'Moved {moved_file_count} so far')
            else:
                ignored_file_count += 1
                if ignored_file_count % 100 == 0:
                    print(f'Ignored {ignored_file_count} so far')
        print(f'Moved {moved_file_count}, ignored {ignored_file_count} files')
