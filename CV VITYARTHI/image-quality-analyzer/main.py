import argparse
import json
from pathlib import Path

from src.analyzer import analyze_image, analyze_folder


def main():
    parser = argparse.ArgumentParser(
        description="Computer Vision Image Quality Analyzer"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Image file or folder"
    )

    parser.add_argument(
        "--output",
        default="outputs/report.json",
        help="Output JSON report path"
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print("ERROR: Input path does not exist.")
        return

    if input_path.is_file():
        results = [analyze_image(str(input_path))]
    else:
        results = analyze_folder(str(input_path))

    if not results:
        print("No supported images found.")
        return

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    print()
    print("========================================")
    print("       IMAGE QUALITY ANALYZER")
    print("========================================")

    for result in results:
        print("----------------------------------------")
        print("File:", result["file"])
        print("Brightness:", result["metrics"]["brightness"])
        print("Contrast:", result["metrics"]["contrast"])
        print("Sharpness:", result["metrics"]["sharpness"])
        print("Noise:", result["metrics"]["noise"])
        print("Quality:", result["scores"]["overall"], "/100")
        print("Class:", result["label"])

        print("Recommendations:")
        for item in result["recommendations"]:
            print("-", item)

    print()
    print("Report saved to:", output_path)


if __name__ == "__main__":
    main()
