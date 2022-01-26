from setuptools import find_packages, setup

with open('README.pypi.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='ilifu_user_tools',  # Replace with your own username
    version='0.0.1',
    author='Dane Kennedy',
    author_email='dane@idia.ac.za',
    description='A set of simple tools for users of the ilifu cluster',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ilifu/user-tools',
    packages=find_packages(),
    install_requires=[
        'coloredlogs==15.0.1',
        'pillow==9.0.0',
        'tk==0.1.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Systems Administration',
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'show_cat=show_cat.show_cat:main',
        ]
    },
    package_data={
        '': ['email.template'],
    },
)