# utils/console.py

from rich.console import Console
from rich.progress import Progress
from rich.logging import RichHandler
import logging

# Setup the Rich console
console = Console()

# Setup the Rich logger
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console)],
)

logger = logging.getLogger("rich")

progress = Progress(console=console)
