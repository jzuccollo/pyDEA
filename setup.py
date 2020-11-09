from setuptools import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("Warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(name='pydea',
      version='0.2.0',
      description='Pure python library for data envelopment analysis.',
      long_description=read_md('README.md'),
      url='http://github.com/jzuccollo/pydea',
      author='jzuccollo',
      author_email='james.zuccollo@epi.org.uk',
      license='GPL',
      packages=['pydea'],
      install_requires=[
          'numpy', 'pulp', 'statsmodels', 'pandas', 'scikit-learn'
      ],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      zip_safe=False)
