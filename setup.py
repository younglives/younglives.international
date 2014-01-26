from setuptools import setup, find_packages
import os

version = open(os.path.join("younglives", "international", "version.txt")).read().strip()

setup(name='younglives.international',
      version=version,
      description="Policy product for Young Lives international website",
      long_description=open(os.path.join("docs", "README.txt")).read() + "\n" +
                       open(os.path.join("docs", "INSTALL.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Michael Davis',
      author_email='M.R.Davis@me.com',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['younglives'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'younglives.policy',
      ],
      extras_require = {
            'test': [
                    'plone.app.testing',
                ]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
)
