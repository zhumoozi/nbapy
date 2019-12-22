import unittest
test_dir = './grab'

print("start testing")
#discover = unittest.defaultTestLoader.discover(test_dir,pattern="grabttzb.py")
discover = unittest.defaultTestLoader.discover(test_dir,pattern="grabpage.py")

if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(discover)
    print("ending...")