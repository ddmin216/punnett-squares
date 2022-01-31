from rich.console import Console
from rich.table import Table

table = Table(show_lines=True)

table.add_column("", justify="right", style="cyan", no_wrap=True)
table.add_column("X", justify="center", style="magenta")
table.add_column("X", justify="center", style="green")

table.add_row("X", "XX", "XX")
table.add_row("Y", "XY", "XY")

console = Console()
console.print(table)
