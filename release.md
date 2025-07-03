# Release Guide: dicom-maker

This document outlines the steps to package and release the `dicom-maker` project to PyPI.

---

## Prerequisites

Before releasing a new version of `dicom-maker`, ensure the following:

1. **Update Version**:
   - Increment the version number in `setup.py` (e.g., `version="1.0.1"`).
   - Follow [Semantic Versioning](https://semver.org/) for version numbers:
     - `MAJOR.MINOR.PATCH`
       - **MAJOR**: Breaking changes.
       - **MINOR**: Backward-compatible features.
       - **PATCH**: Bug fixes or minor changes.

   Example in `setup.py`:
   ```python
   setuptools.setup(
       name="dicom-maker",
       version="1.0.1",  # Update the version here
       ...
   )
   ```

2. **Install Tools**:
   - Ensure you have the required tools installed for building and publishing:
     ```bash
     pip install --upgrade build twine
     ```

3. **Clean the Project**:
   - Remove any old build artifacts to prevent incorrect uploads:
     ```bash
     rm -rf dist/ build/ *.egg-info/
     ```

---

## Steps to Release

Follow these steps to package and release the project:

### 1. Build the Distribution Files

Run the following command to create both **source** (`.tar.gz`) and **wheel** (`.whl`) distribution files:

```bash
python3 -m build
```

This will generate the distribution files in the `dist/` directory, such as:

```angular2html
dist/ dicom-maker-1.0.1.tar.gz dicom-maker-1.0.1-py3-none-any.whl
```
---

### 2. Test the Distribution Locally

Before uploading, test the package in a local environment:

1. Install the package:
   ```bash
   pip install dist/dicom-maker-1.0.1-py3-none-any.whl
   ```

2. Run the package:
   ```bash
   dicom-maker
   ```

3. Confirm that the package works as expected.

---

### 3. Publish the Package to PyPI

When you're ready to upload the package:

1. Upload it to PyPI using **Twine**:
   ```bash
   twine upload dist/*
   ```

2. Enter your PyPI credentials (username/password or API token).

---

### 4. Verify the Release

After uploading, verify the release by visiting the PyPI project page:

- Link: [https://pypi.org/project/dicom-maker/](https://pypi.org/project/dicom-maker/)

---

## Future Updates

When releasing future versions, repeat the above steps, ensuring:

1. **Version is Incremented** in `setup.py`.
2. Old build artifacts are cleaned up before creating new ones:
   ```bash
   rm -rf dist/ build/ *.egg-info/
   ```
