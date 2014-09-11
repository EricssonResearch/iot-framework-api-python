import unittest, time
from api import users

class TestUsers(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		u = cls.template_user = {
			'username': "albertoblaz",
			'password': "pa55w0rd_123",
			'firstname': "Alberto",
			'lastname': "Blazquez",
			'description': "My fancy user on the IoT Framework",
			'private': False
		}

		cls.remote_user = users.create(u['username'], u['password'],
			firstname="Alberto", lastname="Blazquez", private=False,
			description="My fancy user on the IoT Framework")

		cls.user_id = cls.remote_user['username']

	def setUp(self):
		time.sleep(1)	# Fix async issues

	def test_a_create(self):
		# a = lambda f: self.assertEqual(self.remote_user[f], self.template_user[f])
		# b = lambda f: self.assertIn(f, self.remote_user)
		# map(a, ['username', 'password', 'firstname', 'lastname', 'description', 'private'])
		# map(b, ['notifications', 'subscriptions', 'triggers', 'rankings', 'access_token', 'refresh_token'])
		for f in ['username', 'password', 'firstname', 'lastname', 'description', 'private']:
			self.assertEqual(self.remote_user[f], self.template_user[f])
		for f in ['notifications', 'subscriptions', 'triggers', 'rankings', 'access_token', 'refresh_token']:
			self.assertIn(f, self.remote_user)


	def test_get_all(self):
		col = users.get_all()
		self.assertEqual(len(col), 1)
		self.assertEqual(col[0], self.remote_user)

	def test_get(self):
		remote_user2 = users.get(self.user_id)
		self.assertEqual(self.remote_user, remote_user2)

	def test_update(self):
		new_description = "I'm changing my description"
		users.update(self.user_id, description=new_description)

		us = users.get(self.user_id)
		self.assertNotEqual(us['description'], self.template_user['description'])
		self.assertEqual(us['description'], new_description)


	# Final tests

	def test_z_remove(self):
		res = users.remove(self.user_id)
		self.assertEqual(res['found'], True)
		self.assertEqual(res['_id'], self.user_id)
		self.assertNotIn('error', res)

	def test_z_remove_fail(self):
		res = users.remove(self.user_id)
		self.assertIn('error', res)


if __name__ == '__main__':
	unittest.main()
