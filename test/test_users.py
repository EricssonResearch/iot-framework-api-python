import unittest, time
from api import users as U

class TestUsers(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.template_user = {
			'firstname': "Alberto",
			'lastname': "Blazquez",
			'description': "My fancy user on the IoT Framework",
			'private': False
		}
		cls.remote_user = U.create_user("albertoblaz", "pa55w0rd_123", firstname="Alberto")

	# @classmethod
	# def tearDownClass(cls):
	# 	res = U.delete_user(cls.remote_user['_id'])
	# 	# self.assertEqual(res, "ok")

	def setUp(self):
		# Fix async issues
		time.sleep(1)

	def test_create_user(self):
		self.assertEqual(self.remote_user['created'], True)
		# self.assertEqual(self.remote_user['firstname'], "Alberto")
		# self.assertIn('lastname', self.remote_user)
		# self.assertEqual(self.remote_user['lastname'], "Blazquez")
		# self.assertIn('description', self.remote_user)
		# self.assertEqual(self.remote_user['description'], "My fancy user on the IoT Framework")
		# self.assertIn('description', self.remote_user)
		# self.assertEqual(self.remote_user['private'], false)

		# self.assertIn('access_token', self.remote_user)
		# self.assertIn('refresh_token', self.remote_user)

		# self.assertIn('notifications', self.remote_user)
		# self.assertIn('subscriptions', self.remote_user)
		# self.assertIn('triggers', self.remote_user)
		# self.assertIn('rankings', self.remote_user)

	def test_get_users(self):
		users = U.get_users()['users']
		self.assertEqual(len(users), 1)
		# TODO Fix the response of a POST /users
		# self.assertEqual(users[0], self.remote_user)

	def test_get_user(self):
		user = U.get_users()['users'][0]
		remote_user2 = U.get_user(self.remote_user['_id'])
		# self.assertEqual(self.remote_user, remote_user2)
		self.assertEqual(user, remote_user2)

	# def test_update_user(self):
	# 	old_description = self.template_user['description']
	# 	new_description = "I'm changing my description"

	# 	self.remote_user['description'] = new_description
	# 	updated_user = U.update_user(self.remote_user['_id'], description=new_description)

	# 	self.assertNotEqual(updated_user, old_description)
	# 	self.assertEqual(updated_user, new_description)

	def test_remove_user(self):
		res = U.delete_user(self.remote_user['_id'])
		self.assertEqual(res['found'], True)
		self.assertEqual(res['_id'], self.remote_user['_id'])
		self.assertNotIn('error', res)

	def test_remove_user_fail(self):
		res = U.delete_user(self.remote_user['_id'])
		self.assertIn('error', res)


if __name__ == '__main__':
	unittest.main()
