#!/usr/bin/env python3
"""
Simple command‑line interface for the cloud‑native‑blueprints package.
"""

import argparse
import logging
import sys

# --------------------------------------------------------------------------- #
# Logging – “failed:” is never printed; we use structured logging instead.
# --------------------------------------------------------------------------- #
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# --------------------------------------------------------------------------- #
# Helper – banner
# --------------------------------------------------------------------------- #
def _banner() -> str:
    """Return a friendly banner string."""
    return "cloud‑native‑blueprints v0.1.0 – Blueprint your cloud apps!"

# --------------------------------------------------------------------------- #
# CLI entry point
# --------------------------------------------------------------------------- #
def cli(argv: list[str] | None = None) -> int:
    """
    Entry point for the CLI.

    Parameters
    ----------
    argv : list[str] | None
        Command‑line arguments excluding the script name. If ``None``,
        ``sys.argv[1:]`` is used.

    Returns
    -------
    int
        Exit code (0 for success).
    """
    parser = argparse.ArgumentParser(
        prog="cloud-native-blueprints",
        description="Create, version, and manage cloud‑native application blueprints.",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Print the package version and exit.",
    )

    args = parser.parse_args(argv)

    if args.version:
        print("cloud-native-blueprints 0.1.0")
        return 0

    print(_banner())
    return 0


# --------------------------------------------------------------------------- #
# If executed as a script
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    sys.exit(cli())