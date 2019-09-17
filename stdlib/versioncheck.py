import sys, warnings
if sys.version_info[0] < 3:
    warnings.warn("At least Python 3.0 is required to run this program", RuntimeWarning)
else:
    print('Normal continuation')
