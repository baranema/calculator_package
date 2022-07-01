from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='calculator-package-emba',
    version='0.0.1',    
    description='Calculator Python package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/baranema/calculator_package',
    author='Emilija Baranauskaite',
    author_email='e.baranauskaite.e@gmail.com',
    license='BSD 2-clause',
    packages=['calculator'], 

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.9',
    ],
)