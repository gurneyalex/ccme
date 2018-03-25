from distutils.core import setup

setup(name='CCMe',
      version='1.0',
      description='Graphical Tool to sent Midi CC events',
      author='Alexandre Fayolle',
      author_email='afayolle.ml@free.fr',
      url='https://github.com/gurneyalex/distutils-sig/ccme',
      scripts=['bin/ccme-gui'],
      packages=['ccme'],
     )
