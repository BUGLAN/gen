from setuptools import setup, find_packages


def long_long_description():
    with open('README.md', 'r') as f:
        desc = f.read()
    return desc


setup(
    name='simple-gen',
    version='2020.01.08',
    description='gen files',
    author='buglan',
    author_email='1831353087@qq.com',
    packages=find_packages(),
    install_requires=['click', 'PyJWT'],
    entry_points='''
        [console_scripts]
        hello = packages.gen:hello
        s = packages.group:hello
        jwt = packages.group:jwt_tool
    ''',
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest',
    ]

)
