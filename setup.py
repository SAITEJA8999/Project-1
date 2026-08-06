from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    # This function will return the list of requirements
    requirements = []
    
    with open(file_path) as file_obj:
        lines = file_obj.readlines()
        
        for line in lines:
            cleaned_line = line.strip()
            # Ignore empty lines and lines meant for editable local installs (-e .)
            if cleaned_line and not cleaned_line.startswith('-e'):
                requirements.append(cleaned_line)
            
    return requirements

setup(
    name='Project1',
    version='0.0.1',
    author='SAITEJA8999',
    author_email="dandamudisaiteja333@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
