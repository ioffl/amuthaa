# -*- coding: utf-8 -*-
#!/usr/bin/python


import unittest

# import Ezhuthu class
try:
    from learntamil.apps.amuthaa.lib.Ezhuthu import Ezhuthu
except ImportError:
    import sys
    from os.path import join, abspath, dirname
    parentpath = abspath(join(dirname(__file__), '..'))
    srcpath = join(parentpath, 'lib')
    sys.path.append(srcpath)
    from Ezhuthu import Ezhuthu
    
# import Chol class
try:
    from learntamil.apps.amuthaa.lib.Chol import Chol
except ImportError:
    import sys
    from os.path import join, abspath, dirname
    parentpath = abspath(join(dirname(__file__), '..'))
    srcpath = join(parentpath, 'lib')
    sys.path.append(srcpath)
    from Chol import Chol

# import EzhuthUrai class
try:
    from learntamil.apps.amuthaa.lib.EzhuthUrai import EzhuthUrai
except ImportError:
    import sys
    from os.path import join, abspath, dirname
    parentpath = abspath(join(dirname(__file__), '..'))
    srcpath = join(parentpath, 'lib')
    sys.path.append(srcpath)
    from EzhuthUrai import EzhuthUrai    
    
# -*- coding: utf-8 -*-
#!/usr/bin/python


import unittest

# import Ezhuthu class
try:
    import learntamil.apps.amuthaa.lib.Ezhuthu
except ImportError:
    import sys
    from os.path import join, abspath, dirname
    parentpath = abspath(join(dirname(__file__), '..'))
    srcpath = join(parentpath, 'lib')
    sys.path.append(srcpath)
    import Ezhuthu
    
# import Chol class
try:
    import learntamil.apps.amuthaa.lib.Chol
except ImportError:
    import sys
    from os.path import join, abspath, dirname
    parentpath = abspath(join(dirname(__file__), '..'))
    srcpath = join(parentpath, 'lib')
    sys.path.append(srcpath)
    import Chol


    
class EzhuthUraiTest(unittest.TestCase):
    """
    A test class for the EzhuthUrai module
    """
    
    def setUp(self):
        #TODO: add setup
        pass
    
    def tearDown(self):
        #TODO: Add tear-down
        pass
    
    def testSomething(self):
        """docstring"""
        
        #TODO: implement this
        

    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(EzhuthUraiTest))
    return suite
    
def main():
    runner = unittest.TextTestResult()
    test_suite = suite()
    runner.run(test_suite)
        

if __name__ == '__main__':
    main()
