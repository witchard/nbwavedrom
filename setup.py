""" Setup script for python packaging """
from setuptools import setup

setup(
    name="nbwavedrom",
    packages=["nbwavedrom"],
    version="0.3.0",
    description="Wavedrom timing diagrams for Jupyter Notebook",
    author="witchard",
    author_email="witchard@hotmail.co.uk",
    url="https://github.com/witchard/nbwavedrom",
    download_url="https://github.com/witchard/nbwavedrom/tarball/0.3.0",
    keywords=["wavedrom", "jupyter", "notebook"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Jupyter",
        "Framework :: Jupyter :: JupyterLab",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)

# DONT FORGET TO CHANGE DOWNLOAD_URL WHEN DOING A RELEASE!
# Thanks to this guide: http://peterdowns.com/posts/first-time-with-pypi.html
# Release with:
#    git tag <version>
#    git push --tags
#    python setup.py sdist upload -r pypi
