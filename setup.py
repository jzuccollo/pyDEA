from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pydea',
      version='0.2.0',
      description='Pure python library for data envelopment analysis.',
      long_description=open('README.md').read(),
      url='http://github.com/jzuccollo/pydea',
      author='jzuccollo',
      author_email='james.zuccollo@reform.co.uk',
      license='GPL',
      packages=['pydea'],
      install_requires=[
          'numpy', 'pulp', 'statsmodels', 'pandas', 'scikit-learn'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False,)
