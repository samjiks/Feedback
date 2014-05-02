from django.db import models

class createuser(models.Model):
	userid = models.IntegerField()
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	age = models.IntegerField()
	gender = models.CharField(max_length=200)


class createquestion(models.Model): 
	questionid = models.IntegerField()	
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date_published')
	questiontypeid = models.CharField(max_length=50)
	questiongroup = models.CharField(max_length=200)

class question_type(models.Model):
	question_type_id = models.IntegerField()
	question_type_name = models.CharField(max_length=100)
