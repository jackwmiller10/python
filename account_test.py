from account import *
import unittest

class MyTestCase(unittest.TestCase):

    DELTA = .001

    def setUp(self):
        
        self.account1 = Account('Account1')
        self.account2 = Account('Account2')

    def tearDown(self):
        
        del self.account1
        del self.account2

    def test_init(self):
        
        self.assertAlmostEqual(self.account1.get_balance(), 0, delta=self.DELTA)
        self.assertEqual(self.account1.get_name(), 'Account1')

        self.assertAlmostEqual(self.account2.get_balance(), 0, delta=self.DELTA)
        self.assertEqual(self.account2.get_name(), 'Account2')

    def test_deposit(self):

        self.assertEqual(self.account1.deposit(-1), False)
        self.assertAlmostEqual(self.account1.get_balance(), 0, delta=self.DELTA)
        self.assertEqual(self.account1.deposit(0), False)
        self.assertAlmostEqual(self.account1.get_balance(), 0, delta=self.DELTA)
        self.assertEqual(self.account1.deposit(1), True)
        self.assertAlmostEqual(self.account1.get_balance(), 1, delta=self.DELTA)
        

        self.assertEqual(self.account2.deposit(-1), False)
        self.assertAlmostEqual(self.account2.get_balance(), 0, delta=self.DELTA)
        self.assertEqual(self.account2.deposit(0), False)
        self.assertAlmostEqual(self.account2.get_balance(), 0, delta=self.DELTA)
        self.assertEqual(self.account2.deposit(2), True)
        self.assertAlmostEqual(self.account2.get_balance(), 2, delta=self.DELTA)

    def test_withdraw(self):

        self.assertEqual(self.account1.withdraw(-1), False)
        self.assertAlmostEqual(self.account1.get_balance(), 0, delta=self.DELTA)
        self.assertEqual(self.account1.withdraw(0), False)
        self.assertAlmostEqual(self.account1.get_balance(), 0, delta=self.DELTA)
        self.assertEqual(self.account1.withdraw(1000), False)
        self.assertAlmostEqual(self.account1.get_balance(), 0, delta=self.DELTA)
        self.account1.deposit(100)
        self.assertEqual(self.account1.withdraw(50), True)
        self.assertAlmostEqual(self.account1.get_balance(), 50, delta=self.DELTA)

        self.assertEqual(self.account2.withdraw(-1), False)
        self.assertAlmostEqual(self.account2.get_balance(), 0, delta=self.DELTA)
        self.assertEqual(self.account2.withdraw(0), False)
        self.assertAlmostEqual(self.account2.get_balance(), 0, delta=self.DELTA)
        self.assertEqual(self.account2.withdraw(1000), False)
        self.assertAlmostEqual(self.account2.get_balance(), 0, delta=self.DELTA)
        self.account2.deposit(1000)
        self.assertEqual(self.account2.withdraw(500), True)
        self.assertAlmostEqual(self.account2.get_balance(), 500, delta=self.DELTA)


if __name__ == "__main__":
    unittest.main()