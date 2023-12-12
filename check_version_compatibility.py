import csv


def check_version_compatibility(
    versions_csv,
    matlab_version,
    python_version,
    matlabengine_version,
) -> bool:
    try:
        with open(versions_csv, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["MATLAB Release"].lower() == matlab_version.lower():
                    compatible_python_versions = row[
                        "Compatible Python versions"
                    ].split(", ")
                    compatible_matlabengine_versions = row[
                        "Compatible matlabengine versions"
                    ].split(", ")

                    # Convert python_version to base version (e.g. 3.7.9 -> 3.7)
                    base_python_version = ".".join(python_version.split(".")[:2])

                    if (
                        base_python_version in compatible_python_versions
                        and matlabengine_version in compatible_matlabengine_versions
                    ):
                        return True
                    else:
                        return False
            return False

    except FileNotFoundError:
        print(f"{versions_csv} not found.")
        return False


if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument("versions_csv", help="Path to versions.csv")
    parser.add_argument("matlab_version", help="MATLAB version")
    parser.add_argument("python_version", help="Python version")
    parser.add_argument("matlabengine_version", help="matlabengine version")
    args = parser.parse_args()

    compatible = check_version_compatibility(
        args.versions_csv,
        args.matlab_version,
        args.python_version,
        args.matlabengine_version,
    )

    print(
        f"versions.csv: {args.versions_csv}\n"
        f"MATLAB version: {args.matlab_version}\n"
        f"Python version: {args.python_version}\n"
        f"matlabengine version: {args.matlabengine_version}\n\n"
        f"Compatible: {compatible}"
    )

    sys.exit(0 if compatible else 1)
