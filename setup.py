from setuptools import setup, find_packages
setup(
    name='chatgpt_py',
    version='0.4',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'chatgpt_cli=chatgpt_py.cli.chatgpt_cli:main',
        ],
    },
    install_requires=['openai']
)
