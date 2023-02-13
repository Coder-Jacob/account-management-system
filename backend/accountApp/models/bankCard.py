from django.db import models
from Account.models import BaseModel
from .human import Human
from .tel import Tel


class BankCardModels(BaseModel):
    cardNumber = models.CharField(verbose_name="卡号", primary_key=True, max_length=20, unique=True, null=False, blank=False, db_index=True)
    withdrawalPwd = models.CharField(max_length=32, verbose_name="取款密码", null=True, blank=True)
    E_bankingPwd = models.CharField(max_length=32, verbose_name="网银密码", null=True, blank=True)
    bankOptions = (
        (1, '中国工商银行'),
        (2, '中国建设银行'),
        (3, '中国交通银行'),
        (4, '中国招商银行'),
    )
    affiliatedBank = models.PositiveSmallIntegerField(choices=bankOptions, null=True, blank=False, verbose_name="所属银行")
    bankCardTypeOptions = (
        (1, '存储卡'),
        (2, '信用卡'),
    )
    bankCardType = models.PositiveSmallIntegerField(choices=bankCardTypeOptions, null=True, blank=False, verbose_name="银行卡类型")
    tel = models.OneToOneField(verbose_name="绑定的手机号", to=Tel, on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(verbose_name="所属账号组", to=Human, on_delete=models.CASCADE, null=True, blank=True)
    remark = models.CharField(verbose_name="备注", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "银行卡"
        verbose_name_plural = "所有" + verbose_name

    def __str__(self):
        if self.remark is None:
            return "%s银行(%s)" % (self.id, self.affiliatedBank)
        else:
            return "%s银行(%s,%s)" % (self.affiliatedBank, self.id, self.remark)
