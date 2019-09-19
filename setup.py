from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='qtpi_kernel',
    version='1.0',
    packages=['qtpi_kernel'],
    description='Simple example of qtpi kernel python wrapper for Jupyter',
    long_description=readme,
    author='Jupyter Development Team',
    author_email='jupyter@googlegroups.com',
    url='https://github.com/miroslav14/qtpi_kernel.git',
    install_requires=[
        'jupyter_client', 'IPython', 'ipykernel'
    ],
    dependency_links=[
        'git+https://github.com/miroslav14/qtpi_kernel.git@master#miroslav14=qtpi_kernel-0'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
)
