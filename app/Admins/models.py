from operator import truediv
from django.db import models
import bcrypt

class Admins(models.Model):
    admin_name = models.CharField(max_length=20)
    admin_password = models.CharField(max_length=70)

    def __str__(self):
        return self.admin_name

    def save(self):
        password = self.admin_password.encode('utf-8')
        hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
        self.admin_password = hashedPassword.decode('utf-8')
        super().save()

    def validatePassword(adminName, password) -> bool:
        admin = Admins.objects.get(admin_name = adminName)
        hashedPassword = admin.admin_password.encode('utf-8')
        encodedPassword = password.encode('utf-8')
        if bcrypt.checkpw(encodedPassword, hashedPassword):
            return True
        else:
            return False

    