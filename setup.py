import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pytoolkit',
    version='0.0.1',
    author='Dan Richardson',
    author_email='na@local.com',
    description='My Python toolkit.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/danricho/pytoolkit',
    project_urls = {
        "Bug Tracker": "https://github.com/danricho/pytoolkit/issues"
    },
    license='MIT',
    packages=['pytoolkit'],
    install_requires=[],
)