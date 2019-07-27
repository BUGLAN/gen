from setuptools import setup, find_packages


def long_long_description():
    with open('README.md', 'r') as f:
        desc = f.read()
    return desc


setup(
    name='simple-gen',
    version='0.0.0',
    description='gen files',
    long_description=long_long_description(),
    author='buglan',
    author_email='1831353087@qq.com',
    packages=find_packages(),
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        hello=gen:hello
    ''',
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest',
    ]

)
