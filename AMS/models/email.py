from django.db import models
from .account import BaseAccount


class Email(BaseAccount):
    psi = models.CharField(max_length=200, null=True, blank=True, verbose_name='POP3/SMTP/IMAP授权码')
    remark = models.CharField(max_length=100, null=True, blank=True, verbose_name="备注")

    class Meta:
        verbose_name = "电子邮箱"
        verbose_name_plural = "所有" + verbose_name

    def __str__(self):
        A = self.username
        B = self.remark
        if A is None:
            if B is None:
                return "---"
            else:
                return str(B)
        else:
            if B is None:
                return str(A)
            else:
                return "%s(%s)" % (A, B)

    def getEmails(self):
        if self is None or self.username is None:
            return '-'
        return self.username