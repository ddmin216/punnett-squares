from rich.console import Console
from rich.table import Table

table = Table(show_lines=True)

geno1 = input("Genotype of Parent 1: ")
geno2 = input("Genotype of Parent 2: ")

assert len(geno1) == len(geno2), "ERROR: Gametes have different lengths"

table.add_column("", justify="right")

for allele in geno1:
    table.add_column(allele, justify="center")

for allele in geno2:
    table.add_row(allele, f"{geno1[0]}{allele}", f"{geno1[1]}{allele}")

console = Console()
console.print(table)
