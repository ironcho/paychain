class Contract(object):
	def __init__(self,pointName):
		self.pointName = pointName
		self.users = {}

	def add_point(self,user,point):
		point = int(point)
		users = self.users
		if user in users:
			users[user] += point
		else:
			users[user] = point
		return users[user]

