import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name='drf_tracking_logger',
    version='1.9.6',
    author="Ravi Singh",
    author_email="ravi.singh@startxlabs.com",
    description="Log DRF requests on specified logger",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/singhravi1/drf-tracking-logger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
