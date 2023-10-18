from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:

    #return list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        


setup(
    name='student performance prediction',
    version='o.o.1',
    author='Ayush',
    author_email='ayushak969@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)