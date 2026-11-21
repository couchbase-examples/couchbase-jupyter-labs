"""Load the Couchbase connection settings shared by every lab notebook.

The labs read ``DB_HOST``, ``DB_USER`` and ``DB_PASSWORD`` from environment
variables. This module fills them in from ``.env`` files, in this order:

1. Variables already set in the environment (they are never overridden).
2. The repo-root ``.env`` (copied from ``.env.sample``; also used by Docker Compose).
3. ``notebooks/.env`` (the committed defaults for the Docker Compose cluster).

Paths are resolved from this file's location, not the kernel's working
directory, so the lookup is the same however Jupyter Lab was started.
"""

from pathlib import Path

from dotenv import load_dotenv

NOTEBOOKS_DIR = Path(__file__).resolve().parent
ENV_FILES = (NOTEBOOKS_DIR.parent / ".env", NOTEBOOKS_DIR / ".env")


def load_env(env_files=ENV_FILES):
    """Load every existing file in ``env_files`` without overriding set values.

    Returns the list of files that were loaded.
    """
    loaded = []
    for env_path in env_files:
        if env_path.is_file():
            load_dotenv(env_path, override=False)
            loaded.append(env_path)
            print(f"Loaded environment from {env_path}")
    if not loaded:
        print("No .env file found in the repo root or notebooks folder; using existing environment variables.")
    return loaded
