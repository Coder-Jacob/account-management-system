from django.db import models
from Account.models import BaseModel
from .human import Human
from .tel import Tel


class BankCard(BaseModel):
    cardNumber = models.CharField(verbose_name="卡号", max_length=20, unique=True, null=False, blank=False)
    withdrawalPwd = models.CharField(max_length=32, verbose_name="取款密码", null=False, blank=False)
    E_bankingPwd = models.CharField(max_length=32, verbose_name="网银密码", null=True, blank=True)
    bankOptions = (
        (1, '工商银行'),
        (2, '建设银行'),
        (3, '交通银行'),
        (4, '招商银行'),
    )
    affiliatedBank = models.PositiveSmallIntegerField(choices=bankOptions, null=True, blank=False, verbose_name="所属银行")
    bankCardTypeOptions = (
        (1, '储蓄卡'),
        (2, '信用卡'),
    )
    bankCardType = models.PositiveSmallIntegerField(choices=bankCardTypeOptions, null=True, blank=False, verbose_name="银行卡类型")
    tel = models.ForeignKey(verbose_name="绑定的手机号", to=Tel, on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(verbose_name="所属账号组", to=Human, on_delete=models.CASCADE, null=True, blank=True)
    remark = models.CharField(verbose_name="备注", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "银行卡"
        verbose_name_plural = "所有" + verbose_name

    def __str__(self):
        if self.remark is None:
            return "%s银行(%s)" % (self.affiliatedBank, self.cardNumber)
        else:
            return "%s银行(%s,%s)" % (self.affiliatedBank, self.cardNumber, self.remark)

    def get_copy_content(self):
        affiliatedBankStr = dict(self.bankOptions)[self.affiliatedBank]
        bankCardTypeText = dict(self.bankCardTypeOptions)[self.bankCardType]
        content = f"{affiliatedBankStr}（{bankCardTypeText}）/jcb/卡号：{self.cardNumber}/jcb/取款密码：{self.withdrawalPwd}/jcb/网银密码：{self.E_bankingPwd}/jcb/绑定手机号：{'-' if self.tel is None else self.tel}"
        return content
