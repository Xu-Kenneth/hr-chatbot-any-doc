import argparse

import nbformat


def clear_outputs(path: str) -> bool:
    nb = nbformat.read(path, as_version=4)
    changed = False
    for cell in nb.cells:
        if cell.get("cell_type") != "code":
            continue
        if cell.get("outputs"):
            cell["outputs"] = []
            changed = True
        if cell.get("execution_count") is not None:
            cell["execution_count"] = None
            changed = True
    if changed:
        nbformat.write(nb, path)
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("notebook_path")
    args = parser.parse_args()

    changed = clear_outputs(args.notebook_path)
    print("Cleared outputs" if changed else "No outputs to clear")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

