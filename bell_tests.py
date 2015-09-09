import os
import bell
import unittest
import tempfile

class BellTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, bell.app.config['DATABASE'] = tempfile.mkstemp()
        bell.app.config['TESTING'] = True
        self.app = bell.app.test_client()
        bell.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(bell.app.config['DATABASE'])

    if __name__ == '__main__':
        unittest.main()
