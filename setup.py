from setuptools import setup
setup(name='Ampel-base-ZTF',
      version='0.5.0',
      package_dir={'':'src'},
      package_data = {'': ['*.json']},
      packages=[
          'ampel.ztf.pipeline.t0',
      ],
)