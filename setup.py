from setuptools import find_packages, setup

setup(
    name='faust_benchmark',
    version='1.0.0',
    description='The goal is to evaluate Faust tool under the load',
    author='Yauheni Subota',
    author_email='zhenya.subbota.19@gmail.com',
    platforms=['any'],
    license='Proprietary',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=['faust-streaming'],
    python_requires='~=3.6',
)
