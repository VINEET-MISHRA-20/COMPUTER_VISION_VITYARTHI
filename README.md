 🔍 Smart Image Quality Analyzer

> **A command-line Computer Vision project for automatic image-quality assessment using OpenCV and NumPy.**

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](#-installation)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)](#-technologies)


---

##  Overview

**Smart Image Quality Analyzer** is a lightweight Computer Vision application that evaluates the quality of digital images without requiring a graphical user interface.

The application analyzes four important image characteristics:

- ☀️ **Brightness**
- ◐ **Contrast**
- 🔎 **Sharpness**
- 📡 **Noise**

These measurements are converted into quality scores and combined into an **overall score from 0 to 100**. The application then assigns a quality classification and provides practical recommendations when quality problems are detected.

The project supports both **single-image analysis** and **batch analysis of an entire folder**, with results automatically exported to a JSON report.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🖼️ Single Image | Analyze one image directly from the terminal |
| 📁 Batch Processing | Analyze multiple supported images in a folder |
| ☀️ Brightness | Detect underexposure or excessive brightness |
| ◐ Contrast | Measure intensity variation |
| 🔎 Sharpness | Estimate image detail using Laplacian variance |
| 📡 Noise | Estimate local intensity variation |
| 📊 Quality Score | Generate an overall score out of 100 |
| 🏷️ Classification | Label images as Excellent, Good, Fair, or Poor |
| 💡 Recommendations | Suggest improvements for detected problems |
| 📄 JSON Report | Save complete results in structured JSON format |
| 💻 CLI Only | Fully executable from the command line |

---

## 🧰 Technologies

```text
Python
 ├── OpenCV      → Image loading and Computer Vision operations
 ├── NumPy       → Numerical image processing
 └── pytest      → Automated testing
```

### Dependencies

```text
numpy
opencv-python
pytest
```

They are listed in `requirements.txt`.

---

## 📂 Project Structure

```text
image-quality-analyzer/
│
├── 📄 main.py                  # Command-line application entry point
├── 📄 requirements.txt         # Python dependencies
├── 📄 README.md                # Project documentation
├── 📄 .gitignore               # Git ignored files
│
├── 📁 data/
│   └── 📁 sample/
│       ├── 🖼️ dark.jpg
│       ├── 🖼️ normal.jpg
│       └── 🖼️ sharp.jpg
│
├── 📁 outputs/
│   └── 📄 report.json          # Generated analysis report
│
├── 📁 src/
│   ├── 📄 __init__.py
│   ├── 📄 analyzer.py          # Main image-analysis logic
│   ├── 📄 brightness.py        # Brightness calculation
│   ├── 📄 contrast.py          # Contrast calculation
│   ├── 📄 sharpness.py         # Sharpness calculation
│   ├── 📄 noise.py             # Noise estimation
│   └── 📄 scoring.py            # Score and classification logic
│
└── 📁 tests/
    └── 📄 test_analyzer.py     # Automated tests
```

---

# 🚀 Installation

## 1️⃣ Open the project directory

Open PowerShell or the VS Code terminal inside:

```text
image-quality-analyzer
```

## 2️⃣ Create a virtual environment

```powershell
python -m venv .venv
```

## 3️⃣ Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

After activation, your terminal should look similar to:

```text
(.venv) PS C:\...\image-quality-analyzer>
```

## 4️⃣ Install dependencies

```powershell
python -m pip install -r requirements.txt
```

---

# ▶️ Usage

##  Analyze a Single Image

Run:

```powershell
python main.py --input data/sample/sharp.jpg
```

The terminal displays the detected metrics, quality score, classification, and recommendations.

### Example terminal output

```text
========================================
       IMAGE QUALITY ANALYZER
========================================
----------------------------------------
File: data\sample\sharp.jpg
Brightness: 102.15
Contrast: 123.63
Sharpness: 1169.23
Noise: 0.07
Quality: 94.9 /100
Class: Excellent
Recommendations:
- No major quality problem detected.

Report saved to: outputs\report.json
```

> **Note:** Exact values depend on the input image.

---

##  Analyze an Entire Folder

The application can process all supported images inside a folder.

```powershell
python main.py --input data/sample
```

Example output:

```text
========================================
       IMAGE QUALITY ANALYZER
========================================
----------------------------------------
File: data\sample\dark.jpg
Brightness: 35.0
Contrast: 0.0
Sharpness: 0.0
Noise: 0.0
Quality: 26.84 /100
Class: Poor
Recommendations:
- Image may be too dark. Consider increasing exposure.
- Low contrast detected.
- Low sharpness detected. Check focus or camera movement.

----------------------------------------
File: data\sample\normal.jpg
Brightness: 128.0
Contrast: 0.0
Sharpness: 0.0
Noise: 0.0
Quality: 45.0 /100
Class: Fair
Recommendations:
- Low contrast detected.
- Low sharpness detected. Check focus or camera movement.

----------------------------------------
File: data\sample\sharp.jpg
Brightness: 102.15
Contrast: 123.63
Sharpness: 1169.23
Noise: 0.07
Quality: 94.9 /100
Class: Excellent
Recommendations:
- No major quality problem detected.

Report saved to: outputs\report.json
```

---

##  Generate a Custom JSON Report

The default report location is:

```text
outputs/report.json
```

A custom location can be supplied using `--output`:

```powershell
python main.py --input data/sample --output outputs/my_report.json
```

---

# 📊 Quality Analysis

## ☀️ 1. Brightness

Brightness represents the average intensity of the image.

Very low brightness can indicate an underexposed or dark image, while very high brightness can indicate an overexposed image.

---

## ◐ 2. Contrast

Contrast measures variation between intensity values in the image.

Low contrast can make an image appear flat and reduce the visual separation between objects and their background.

---

## 🔎 3. Sharpness

Sharpness is estimated using the **variance of the Laplacian**.

The basic idea is:

```text
Image
  ↓
Convert to grayscale
  ↓
Laplacian operation
  ↓
Calculate variance
  ↓
Sharpness estimate
```

Higher Laplacian variance generally indicates stronger edges and more visible detail.

---

## 📡 4. Noise

Noise is estimated from local intensity variation.

Higher unwanted variation can indicate increased image noise, which may reduce perceived quality.

---

# 🧮 Quality Scoring

The individual measurements are converted into component scores and combined into an overall quality score.

```text
Brightness ──┐
Contrast ────┤
Sharpness ───┼──→ Overall Quality Score → Classification
Noise ───────┘
```

The final score is reported on a **0–100 scale**.

### Classification

| Overall Score | Classification |
|---:|:---|
| 🟢 **80–100** | **Excellent** |
| 🔵 **60–79.99** | **Good** |
| 🟡 **40–59.99** | **Fair** |
| 🔴 **Below 40** | **Poor** |

---

# 💡 Recommendations

The application does more than calculate numbers.

It checks the measurements and generates recommendations such as:

```text
Image may be too dark. Consider increasing exposure.
```

```text
Low contrast detected.
```

```text
Low sharpness detected. Check focus or camera movement.
```

When no major issue is detected:

```text
No major quality problem detected.
```

---

# 📦 JSON Report

The analyzer produces a structured JSON file containing the analysis results.

Example:

```json
[
    {
        "file": "data\\sample\\sharp.jpg",
        "resolution": {
            "width": 600,
            "height": 400
        },
        "metrics": {
            "brightness": 102.15,
            "contrast": 123.63,
            "sharpness": 1169.23,
            "noise": 0.07
        },
        "scores": {
            "brightness": 0.0,
            "contrast": 1.0,
            "sharpness": 1.0,
            "noise": 0.9998,
            "overall": 94.9
        },
        "label": "Excellent",
        "recommendations": [
            "No major quality problem detected."
        ]
    }
]
```

> The numerical values change according to the analyzed image.

---

# 🧪 Testing

The project includes automated tests using **pytest**.

Run:

```powershell
pytest
```

Verified result:

```text
================================================= test session starts =================================================
collected 2 items

tests\test_analyzer.py ..                                      [100%]

================================================== 2 passed ==================================================
```

### What is tested?

The current tests verify:

- ✔️ Analyzer returns a dictionary.
- ✔️ Resolution information is present.
- ✔️ Image-quality metrics are present.
- ✔️ Component scores are present.
- ✔️ Overall score is returned.
- ✔️ Quality classification is returned.
- ✔️ Missing images are handled with an appropriate error.

---

# 💻 Command-Line Interface

General command:

```powershell
python main.py --input <image-or-folder> [--output <json-file>]
```

### `--input`

**Required**

Accepts:

```text
Image file
    OR
Folder containing supported images
```

Example:

```powershell
python main.py --input data/sample/sharp.jpg
```

or:

```powershell
python main.py --input data/sample
```

### `--output`

**Optional**

Specifies where the JSON report should be saved.

Example:

```powershell
python main.py --input data/sample --output outputs/results.json
```

Default:

```text
outputs/report.json
```

---

# ⚠️ Limitations

- This project is intended for general image-quality assessment.
- The quality score is a heuristic measurement rather than an absolute professional image-quality standard.
- Results depend on the characteristics of the input image.
- Different types of images may produce different metric ranges.
- The current application uses a command-line interface rather than a graphical interface.

---

# 🔮 Future Improvements

Possible extensions include:

- 📈 Additional image-quality metrics
- 🧠 More advanced noise estimation
- ⚙️ Configurable scoring thresholds
- 🖼️ Support for additional image formats
- 📊 Visualization of quality measurements
- 🧪 More extensive automated testing
- 🔄 Comparative analysis between images
- 📑 More detailed report generation

---

# 🎯 Project Objective

The main objective of this project is to demonstrate how fundamental **Computer Vision techniques** can be combined to automatically evaluate image quality.

The project provides a simple workflow:

```text
             INPUT IMAGE
                  │
                  ▼
        ┌──────────────────┐
        │ Image Processing │
        └────────┬─────────┘
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
  Brightness  Contrast  Sharpness
       │         │         │
       └─────────┼─────────┘
                 ▼
               Noise
                 │
                 ▼
        ┌──────────────────┐
        │ Quality Scoring  │
        └────────┬─────────┘
                 ▼
        ┌──────────────────┐
        │ Classification    │
        └────────┬─────────┘
                 ▼
        ┌──────────────────┐
        │ Recommendations  │
        └────────┬─────────┘
                 ▼
             JSON REPORT
```

---

# 👨‍💻 Author

**Computer Vision Project**

Developed as part of the **VITyarthi Computer Vision project evaluation**.

---

## ⭐ Quick Start

If the environment is already configured, the fastest way to run the project is:

```powershell
python main.py --input data/sample
```

To run the tests:

```powershell
pytest
```

To generate a custom report:

```powershell
python main.py --input data/sample --output outputs/my_report.json
```

---

> **Built with Python, OpenCV, NumPy, and pytest.**
sion project that analyzes image quality using brightness, contrast, sharpness, and noise metrics. It generates an overall quality score, classifies images as Poor, Fair or Excellent, and provides recommendations for improving image quality. Supports both single-image and batch folder analysis with JSON report generation.
[README.md](https://github.com/user-attachments/files/32338915/README.md)
