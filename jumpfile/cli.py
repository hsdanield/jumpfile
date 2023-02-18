from jumpfile.service.excel_service import save_excel

import typer
from rich.console import Console

main = typer.Typer(help="JumpFile Application")
console = Console()


@main.command("teste")
def teste():
    """
        jumpfile
    """
    console.print("JumpFile")


@main.command("save_excel")
def save(
        name: str = typer.Option(...)
):
    save_excel(name)
    console.print("save_excel finalizado...")
