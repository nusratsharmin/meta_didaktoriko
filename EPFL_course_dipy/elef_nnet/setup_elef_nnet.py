# -- setup.py --
from setuptools import setup
from Cython.Distutils import build_ext
from numpy.distutils.extension import Extension
setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("elef_nnet",
                           ["elef_nnet.pyx"])
                 ]
)
# EOF