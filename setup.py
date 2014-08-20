from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pydea',
      version='0.1.0',
      description='Class for simple data envelopment analysis.',
      long_description=open('README.md').read(),
      url='http://github.com/jzuccollo/pydea',
      author='jzuccollo',
      author_email='james.zuccollo@reform.co.uk',
      license='MIT',
      packages=['pydea'],
      install_requires=[
          'numpy', 'pulp'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False,)
