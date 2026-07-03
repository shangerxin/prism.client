from pathlib import Path

from setuptools import find_packages, setup

NAME = "prism.py.client"
VERSION = "1.0.0"
DESCRIPTION = "Python client for prism.web.service"
AUTHOR = "Shang, Erxin"
AUTHOR_EMAIL = "shangerxin@hotmail.com"
URL = "https://github.com/shangerxin/prism.client"
PYTHON_REQUIRES = ">=3.10"

INSTALL_REQUIRES = [
    "urllib3>=2.1.0,<3.0.0",
    "python-dateutil>=2.8.2",
    "pydantic>=2.11",
    "typing-extensions>=4.7.1",
]

ROOT = Path(__file__).resolve().parent
README_CANDIDATES = [ROOT / "README.md"]
README = next((path for path in README_CANDIDATES if path.exists()), None)
LONG_DESCRIPTION = (
    README.read_text(encoding="utf-8")
    if README
    else "Python helper for uploading benchmark and test artifacts to a Prism server."
)

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    project_urls={
        "Repository": URL,
    },
    license="MIT",
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(exclude=("test", "tests")),
    include_package_data=True,
    package_data={"prism_python_client": ["py.typed"]},
    keywords=["prism", "prism.python.client", "prism.py.client"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
