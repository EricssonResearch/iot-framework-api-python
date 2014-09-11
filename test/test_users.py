import unittest, time
from api import users

class TestUsers(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.template_user = {
			'username': "albertoblaz",
			'password': "pa55w0rd_123",
			'firstname': "Alberto",
			'lastname': "Blazquez",
			'description': "My fancy user on the IoT Framework",
			'private': False
		}
		cls.remote_user = users.create(cls.template_user)

	def setUp(self):
		time.sleep(1)	# Fix async issues

	def test_create(self):
		a = lambda f: self.assertEqual(self.remote_user[f], self.template_user[f])
		map(a, ['username', 'password', 'firstname', 'lastname', 'description', 'private'])

		b = lambda f: self.assertIn(f, self.remote_user)
		map(b, ['notifications', 'subscriptions', 'triggers', 'rankings', 'access_token', 'refresh_token'])

	def test_get_all(self):
		users = users.get_all()['users']
		self.assertEqual(len(users), 1)
		self.assertEqual(users[0], self.remote_user)

	def test_get(self):
		remote_user2 = users.get(self.remote_user['username'])
		self.assertEqual(self.remote_user, remote_user2)

	def test__update(self):
		new_description = "I'm changing my description"
		updated_user = users.update(self.remote_user['username'], description=new_description)
		self.assertNotEqual(updated_user, self.template_user)
		self.assertEqual(updated_user, new_description)


	# Final tests

	def test_remove(self):
		res = users.remove(self.remote_user['username'])
		self.assertEqual(res['found'], True)
		self.assertEqual(res['username'], self.remote_user['username'])
		self.assertNotIn('error', res)

	def test_remove_fail(self):
		res = users.remove(self.remote_user['username'])
		self.assertIn('error', res)


if __name__ == '__main__':
	unittest.main()
