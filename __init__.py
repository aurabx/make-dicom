"""
Enhanced DICOM Generator

This package generates sample DICOM studies with consistent patient demographics and
comprehensive clinical metadata including institution information, referring physicians,
laterality, and other commonly used DICOM fields.

Requirements:
- Python 3.6+
- DCMTK toolkit installed and available in PATH
"""

__version__ = "1.0.0"
__author__ = "Aurabox"
__email__ = "hello@aurabox.cloud"

# Import main components to provide a cleaner API
from .utils.uid_generator import generate_uid
from .utils.template_generator import create_dicom_template
from .generators.dicom_generator import create_dicom_from_template
from .main import generate_dicom_data