from rich.console import Console
from rich.progress import track
import time


console = Console()
console.clear()
console.rule("Projekt 2")
console.print()

for i in track(range(10)):
    i=i+1
    time.sleep(3)

