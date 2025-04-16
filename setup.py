import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dicom-generator",
    version="1.0.0",
    author="Aurabox",
    author_email="hello@aurabox.cloud",
    description="Enhanced DICOM Generator for creating sample DICOM studies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aurabx/dicom-generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pathlib>=1.0.1",
    ],
    entry_points={
        "console_scripts": [
            "dicom-generator=dicom_generator.main:cli_main",
        ],
    },
)