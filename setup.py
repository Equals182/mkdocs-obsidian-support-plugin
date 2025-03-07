from setuptools import setup, find_packages

VERSION_NUMBER = '1.4.1'


setup(
    name='mkdocs-obsidian-support-plugin',
    version=VERSION_NUMBER,
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'obsidian-support = obsidian_support.plugin:ObsidianSupportPlugin'
        ]
    }
)
