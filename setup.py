from distutils.core import setup, Extension

module1 = Extension('Enum', sources = ['enummodule.c'])

setup (name = 'Enum',
         version = '1.0',
         description = 'Testing c integration',
         ext_modules = [module1])
