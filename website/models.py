from django.db import models



# --------------- Database Models ---------------------
class Record(models.Model):
	creation_date = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	zip_code = models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
