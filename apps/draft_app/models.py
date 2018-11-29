from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg_validation(self, postData, session):
        errors={}
        if len(postData['email']) == 0:
            errors['email_length']= "email cannot be blank"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['valid_email'] ="the email entered is not a valid email"
        e_check = User.objects.filter(email=postData['email'])
        if len(e_check):
            errors['email_used'] = "email has already been registered"
        else:
            session['email']= postData['email']
        if len(postData['first_name']) < 2:
            errors['fname_langth'] = "first name must be at least 2 letters long"
        if postData['first_name'].isalpha() == False:
            errors['fname_alpha'] = "first name can only contain letters"
        else:
            session['fname']= postData['first_name']
        if len(postData['last_name']) < 2:
            errors['lname_langth'] = "last name must be at least 2 letters long"
        if postData['last_name'].isalpha() == False:
            errors['lname_alpha'] = "last name can only contain letters"
        else:
            session['lname']= postData['last_name']
        date = datetime.datetime.today().timestamp()
        print(date)
        if len(postData['dob']) < 2:
            errors['dob_length'] = "dob connot be blank"
        else: 
            dob=datetime.datetime.strptime(postData['dob'],'%Y-%m-%d').timestamp()
            print(dob)
            age = date - dob
            print(age)
            if age < 567648000:
                errors['dob'] = "You must be at least 18 to register"
            else:
                session['dob']= postData['dob']
        password_attempt = postData['password']
        count = 0
        for i in range(0, len(password_attempt)):
            if password_attempt[i].isupper() == True:
                count += 1
                break
        if len(postData['password']) < 8 or postData['password'].isalnum() == False or count < 1:
            errors['password'] = "Password must be at least 8 characters, contain at least one letter and one number, and at least one uppercase letter!"
        if postData['password'] != postData['confirm_password']:
            errors['confirm'] = "Password confirmation does not match"
        if len(errors):
            return errors
        else:
            hash1 = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], dob = postData['dob'], password = hash1)
            session.clear()
            a = User.objects.get(email=postData['email'])
            session['id'] = a.id
            if 'email' in session:
                del session['email']
            if 'dob' in session:
                del session['dob']
            if 'lname' in session:
                del session['lname']
            if 'fname' in session:
                del session['fname']
            return errors
    def login_val(self, postData, session):
        errors={}
        e_check = User.objects.filter(email=postData['email'])
        if len(e_check):
            u = User.objects.get(email=postData['email'])
            if bcrypt.checkpw(postData['lpassword'].encode(), u.password.encode()):
                a = User.objects.get(email=postData['email'])
                session['id'] = a.id
                return errors
            else:
                errors['wrong_password']= 'Password did not match our records'
                return errors
        else:
            errors['wrong_email']= "email does not match our records"
            return errors

class Team(models.Model):
    name = models.CharField(max_length=255)
    conference = models.CharField(max_length=255)
    bye = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Player(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    pos_rank = models.IntegerField()
    depth = models.IntegerField()
    team = models.ForeignKey(Team, related_name="players")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField(default=datetime.date.today())
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Lineup(models.Model):
    user = models.ForeignKey(User, related_name="lineups")
    qb = models.OneToOneField(Player, default = 0, related_name="qb", on_delete=models.CASCADE)
    rb1 = models.OneToOneField(Player, default = 0, related_name="rb1", on_delete=models.CASCADE)
    rb2 = models.OneToOneField(Player, default = 0, related_name="rb2", on_delete=models.CASCADE)
    wr1 = models.OneToOneField(Player, default = 0, related_name="wr1", on_delete=models.CASCADE)
    wr2 = models.OneToOneField(Player, default = 0, related_name="wr2", on_delete=models.CASCADE)
    te = models.OneToOneField(Player, default = 0, related_name="te", on_delete=models.CASCADE)
    flex = models.OneToOneField(Player, default = 0, related_name="flex", on_delete=models.CASCADE)
    dst = models.OneToOneField(Player, default = 0, related_name="dst", on_delete=models.CASCADE)
    k = models.OneToOneField(Player, default = 0, related_name="k", on_delete=models.CASCADE)
    be1 = models.OneToOneField(Player, default = 0, related_name="be1", on_delete=models.CASCADE)
    be2 = models.OneToOneField(Player, default = 0, related_name="be2", on_delete=models.CASCADE)
    be3 = models.OneToOneField(Player, default = 0, related_name="be3", on_delete=models.CASCADE)
    be4 = models.OneToOneField(Player, default = 0, related_name="be4", on_delete=models.CASCADE)
    be5 = models.OneToOneField(Player, default = 0, related_name="be5", on_delete=models.CASCADE)
    be6 = models.OneToOneField(Player, default = 0, related_name="be6", on_delete=models.CASCADE)
    be7 = models.OneToOneField(Player, default = 0, related_name="be7", on_delete=models.CASCADE)