import os
import shutil
from rich.console import Console
from rich.table import Table
from font.DynamicCliFont import DynamicCliFont

class PyCacheKiller:
    def __init__(self, target_folder, dynamic_font_json):
        self.target_folder = target_folder
        self.cli_font = DynamicCliFont(dynamic_font_json)
        self.console = Console()
        self.ascii_art = self.cli_font.generate_ascii_art('Erasing Cache')

    def find_and_delete(self):
        # Display dynamically generated ASCII art
        self.console.print(self.ascii_art)

        self.console.print("Initiating PyCacheKiller...")
        table = Table(title="Erased Cache Paths", show_header=True, header_style="bold")
        table.add_column("Path", style="cyan")
        deleted_count = 0

        for root, dirs, _ in os.walk(self.target_folder, topdown=False):
            if '__pycache__' in dirs:
                pycache_path = os.path.join(root, '__pycache__')
                self._delete_pycache(pycache_path)
                table.add_row(pycache_path)
                deleted_count += 1

            for dir in dirs:
                if dir.endswith(".pyc"):
                    pyc_path = os.path.join(root, dir)
                    self._delete_pyc_file(pyc_path)
                    table.add_row(pyc_path)
                    deleted_count += 1

        self.console.print(table)
        self.console.print(f"Total {deleted_count} cache items erased.")

    def _delete_pycache(self, pycache_path):
        self.console.print(f"Erasing Cache at [cyan]{pycache_path}[/cyan]")
        shutil.rmtree(pycache_path)
        if not os.path.exists(pycache_path):
            self.console.print(f"[bold green]Successfully erased cache at {pycache_path}[/bold green]")
        else:
            self.console.print(f"[bold red]Failed to erase cache at {pycache_path}[/bold red]")

    def _delete_pyc_file(self, pyc_file_path):
        self.console.print(f"Erasing Cache at [cyan]{pyc_file_path}[/cyan]")
        os.remove(pyc_file_path)
        if not os.path.exists(pyc_file_path):
            self.console.print(f"[bold green]Successfully erased cache at {pyc_file_path}[/bold green]")
        else:
            self.console.print(f"[bold red]Failed to erase cache at {pyc_file_path}[/bold red]")

# if __name__ == "__main__":
    # killer = PyCacheKiller('directory', "path+file")
    # killer.find_and_delete()
