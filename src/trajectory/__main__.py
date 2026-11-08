"""trajectory CLI implementation.

Bullet trajectory simulator.
"""

import sys

import typer
from loguru import logger

from .self_subcommand import cli as self_cli
from .settings import Settings

cli = typer.Typer()

cli.add_typer(
    self_cli,
    name="self",
    help="Manage the trajectory command.",
)


@cli.callback(invoke_without_command=True, no_args_is_help=True)
def global_callback(
    ctx: typer.Context,
    debug: bool = typer.Option(
        False,
        "--debug",
        "-D",
        help="Enable debugging output.",
    ),
) -> None:
    """Bullet trajectory simulator."""
    ctx.obj = Settings()
    debug = debug or ctx.obj.debug
    (logger.enable if debug else logger.disable)("trajectory")
    logger.add("trajectory.log")
    logger.info(f"{debug=}")


if __name__ == "__main__":
    sys.exit(cli())
