""" Setup script for python packaging """
from setuptools import setup
setup(
    name='nbwavedrom',
    packages=['nbwavedrom'],
    package_data={'nbwavedrom': ['js/*.js']},
    version='0.1.0',
    description='Wavedrom timing diagrams for Jupyter Notebook',
    author='witchard',
    author_email='witchard@hotmail.co.uk',
    url='https://github.com/witchard/nbwavedrom',
    download_url='https://github.com/witchard/nbwavedrom/tarball/0.1.0',
    keywords=['wavedrom', 'jupyter', 'notebook'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)

# DONT FORGET TO CHANGE DOWNLOAD_URL WHEN DOING A RELEASE!
# Thanks to this guide: http://peterdowns.com/posts/first-time-with-pypi.html
# Release with:
#    git tag <version>
#    git push --tags
#    python setup.py sdist upload -r pypi
