# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Sspvoucher(models.Model):
    voucherid = models.AutoField(primary_key=True)
    statusvoucher = models.CharField(max_length=7)
    codevoucher = models.CharField(unique=True, max_length=50)
    valuevoucher = models.FloatField()
    datecreated = models.DateTimeField(blank=True, null=True)
    dateused = models.DateTimeField(blank=True, null=True)
    expireddate = models.DateTimeField(blank=True, null=True)
    voucher_imei_client = models.CharField(unique=True, max_length=100, blank=True, null=True)
    voucher_imei_merchant = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sspvoucher'


class Sspactivityadmin(models.Model):
    activityid = models.IntegerField(primary_key=True)
    activitytime = models.DateTimeField()
    adminid = models.IntegerField()
    session = models.TextField()
    activitytypeid = models.ForeignKey('Sspactivitytype', db_column='activitytypeid')

    class Meta:
        managed = False
        db_table = 'sspactivityadmin'


class Sspactivityemployee(models.Model):
    activityid = models.IntegerField(primary_key=True)
    activitytime = models.DateTimeField()
    epmloyeeid = models.ForeignKey('Sspemployee', db_column='epmloyeeid')
    session = models.TextField()
    activitytypeid = models.ForeignKey('Sspactivitytype', db_column='activitytypeid')

    class Meta:
        managed = False
        db_table = 'sspactivityemployee'


class Sspactivitytype(models.Model):
    activitytypeid = models.IntegerField(primary_key=True)
    activitytype = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sspactivitytype'


class Sspannouncement(models.Model):
    annountcementid = models.IntegerField(primary_key=True)
    announcementtypeid = models.IntegerField()
    sender = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30, blank=True)
    tittle = models.CharField(max_length=255)
    announcement = models.TextField()
    announcementtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sspannouncement'


class Sspannouncementtype(models.Model):
    announcementtypeid = models.IntegerField(primary_key=True)
    announcementtypecode = models.CharField(max_length=10)
    announcementtype = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sspannouncementtype'


class Sspbankaccountclient(models.Model):
    clientbankid = models.IntegerField(primary_key=True)
    clientid = models.ForeignKey('Sspclient', db_column='clientid')
    bankid = models.IntegerField()
    accountnumber = models.TextField()
    accountname = models.TextField()

    class Meta:
        managed = False
        db_table = 'sspbankaccountclient'


class Sspbankaccountmerchant(models.Model):
    merchantbankid = models.IntegerField(primary_key=True)
    merchantid = models.ForeignKey('Sspmerchant', db_column='merchantid')
    bankid = models.IntegerField()
    accountnumber = models.TextField()
    accountname = models.TextField()
    personincharge = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sspbankaccountmerchant'


class Sspbankofssp(models.Model):
    bankofsspid = models.IntegerField(primary_key=True)
    bankid = models.IntegerField()
    accountnumber = models.TextField()
    accountname = models.TextField()
    cryptoid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sspbankofssp'


class Sspbanktransfer(models.Model):
    banktransferid = models.CharField(primary_key=True, max_length=20)
    banktransferstatus = models.CharField(max_length=9)
    banktransferdate = models.DateTimeField()
    sspbankid = models.ForeignKey(Sspbankofssp, db_column='sspbankid', blank=True, null=True)
    applicantbankid = models.IntegerField(blank=True, null=True)
    applicantbankaccount = models.CharField(max_length=50)
    applicantname = models.CharField(max_length=50)
    senderid = models.ForeignKey('Sspclient', db_column='senderid')
    beneficiarybankid = models.IntegerField()
    beneficiarybankaccount = models.CharField(max_length=50)
    beneficiaryname = models.CharField(max_length=50)
    amount = models.FloatField()
    fee = models.FloatField()
    adminfee = models.FloatField()
    total = models.FloatField()
    refnumber = models.CharField(max_length=20)
    transfertypeid = models.ForeignKey('Sspbanktransfertype', db_column='transfertypeid')

    class Meta:
        managed = False
        db_table = 'sspbanktransfer'


class Sspbanktransfertype(models.Model):
    banktransfertypeid = models.IntegerField(primary_key=True)
    banktransfertype = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sspbanktransfertype'


class Sspbillingaccess(models.Model):
    billingaccessid = models.IntegerField(primary_key=True)
    employeeid = models.ForeignKey('Sspemployee', db_column='employeeid')
    privileges = models.TextField()

    class Meta:
        managed = False
        db_table = 'sspbillingaccess'


class Sspbillingkey(models.Model):
    billingkeyid = models.IntegerField(primary_key=True)
    clientid = models.ForeignKey('Sspclient', db_column='clientid')
    csclientid = models.ForeignKey('Sspemployee', db_column='csclientid')
    billingid = models.ForeignKey('Sspemployee', db_column='billingid')
    submitdate = models.DateTimeField()
    keycode = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sspbillingkey'


class Sspcategory(models.Model):
    categoryid = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=20)
    categorycode = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'sspcategory'


class Sspclient(models.Model):
    clientid = models.CharField(primary_key=True, max_length=20)
    accountnumber = models.CharField(max_length=20)
    fullname = models.TextField(blank=True)
    phonenumber = models.TextField(blank=True)
    email = models.TextField(blank=True)
    birthplace = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    sexid = models.IntegerField(blank=True, null=True)
    jobid = models.IntegerField(blank=True, null=True)
    nationalityid = models.IntegerField(blank=True, null=True)
    cardtypeid = models.IntegerField(blank=True, null=True)
    cardnumber = models.TextField(blank=True)
    address1 = models.TextField(blank=True)
    address2 = models.TextField(blank=True)
    address3 = models.TextField(blank=True)
    postalcode = models.CharField(max_length=5, blank=True)
    cityid = models.IntegerField(blank=True, null=True)
    provinceid = models.IntegerField(blank=True, null=True)
    stateid = models.IntegerField(blank=True, null=True)
    lastlogin = models.DateTimeField(blank=True, null=True)
    joindate = models.DateTimeField(blank=True, null=True)
    clienttypeid = models.ForeignKey('Sspclienttype', db_column='clienttypeid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sspclient'
        verbose_name="data1"


class Sspclientbalance(models.Model):
    clientbalanceid = models.IntegerField(primary_key=True)
    clientid = models.ForeignKey(Sspclient, db_column='clientid')
    accountnumber = models.CharField(max_length=20)
    balance = models.FloatField()

    class Meta:
        managed = False
        db_table = 'sspclientbalance'


class Sspclientloginfailed(models.Model):
    loginfailedid = models.IntegerField(primary_key=True)
    clientid = models.ForeignKey(Sspclient, db_column='clientid')
    logindate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sspclientloginfailed'


class Sspclientsubbalance(models.Model):
    clientsubbalanceid = models.IntegerField(primary_key=True)
    clientid = models.CharField(unique=True, max_length=20)
    accountnumber = models.CharField(max_length=20)
    subbalance = models.FloatField()

    class Meta:
        managed = False
        db_table = 'sspclientsubbalance'


class Sspclienttype(models.Model):
    clienttypeid = models.IntegerField(primary_key=True)
    clienttype = models.CharField(max_length=50)
    desc = models.TextField()
    registrationfee = models.FloatField()
    transferbetweenaccount = models.CharField(max_length=3)
    topup = models.CharField(max_length=3)
    sspqp = models.CharField(max_length=3)
    wallet = models.CharField(max_length=3)
    subwallet = models.CharField(max_length=3)
    pospayment = models.CharField(max_length=3)
    dailywithdrawlimit = models.FloatField(blank=True, null=True)
    subwalletdailytransactionlimit = models.IntegerField(blank=True, null=True)
    transactionlimit = models.FloatField(blank=True, null=True)
    walletdailytransactionlimit = models.FloatField(blank=True, null=True)
    promo = models.CharField(max_length=3)
    websiteportal = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'sspclienttype'


class Sspcomplaincategory(models.Model):
    complaincategoryid = models.IntegerField(primary_key=True)
    complaincategory = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sspcomplaincategory'


class Sspconfig(models.Model):
    configid = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)
    initial = models.CharField(unique=True, max_length=10)
    value = models.TextField()
    unit = models.TextField()

    class Meta:
        managed = False
        db_table = 'sspconfig'


class Sspcsclientaccess(models.Model):
    csclientaccessid = models.IntegerField(primary_key=True)
    employeeid = models.ForeignKey('Sspemployee', db_column='employeeid')
    privileges = models.TextField()

    class Meta:
        managed = False
        db_table = 'sspcsclientaccess'


class Sspcsmerchantaccess(models.Model):
    csmerchantaccessid = models.IntegerField(primary_key=True)
    employeeid = models.ForeignKey('Sspemployee', db_column='employeeid')
    privileges = models.TextField()

    class Meta:
        managed = False
        db_table = 'sspcsmerchantaccess'


class Sspemployee(models.Model):
    employeeid = models.IntegerField(primary_key=True)
    name = models.TextField()
    sexid = models.IntegerField()
    religion = models.IntegerField()
    birthplace = models.TextField()
    birthdate = models.DateField()
    email = models.TextField()
    phonenumber = models.TextField()
    address1 = models.TextField()
    address2 = models.TextField(blank=True)
    postalcode = models.TextField()
    cityid = models.IntegerField()
    provinceid = models.IntegerField()
    stateid = models.IntegerField()
    positionid = models.ForeignKey('Sspemployeeposition', db_column='positionid')
    loginstatus = models.IntegerField(blank=True, null=True)
    loginblock = models.IntegerField(blank=True, null=True)
    lastlogin = models.DateTimeField(blank=True, null=True)
    joindate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sspemployee'
        verbose_name="data1"


class Sspemployeeloginfailed(models.Model):
    loginfailedid = models.IntegerField(primary_key=True)
    employeeid = models.ForeignKey(Sspemployee, db_column='employeeid')
    logindate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sspemployeeloginfailed'


class Sspemployeeposition(models.Model):
    positionid = models.IntegerField(primary_key=True)
    position = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sspemployeeposition'


class Sspfee(models.Model):
    feeid = models.IntegerField(primary_key=True)
    feedesc = models.CharField(max_length=255)
    feecode = models.CharField(max_length=5)
    fee = models.FloatField()
    unit = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'sspfee'


class Ssphelpdesk(models.Model):
    helpdeskrefnumber = models.CharField(primary_key=True, max_length=30)
    employeeid = models.CharField(max_length=20, blank=True)
    datetime = models.DateTimeField()
    clientid = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=15, blank=True)
    name = models.CharField(max_length=50)
    transactionrefnumber = models.CharField(max_length=30)
    auth_imei = models.CharField(max_length=3)
    auth_qa1 = models.CharField(max_length=3)
    auth_qa2 = models.CharField(max_length=3)
    auth_qa3 = models.CharField(max_length=3)
    auth_securitychar = models.CharField(max_length=3)
    auth_name = models.CharField(max_length=3, blank=True)
    authenticationstatus = models.CharField(max_length=3)
    question = models.TextField()
    answer = models.TextField(blank=True)
    action = models.TextField(blank=True)
    closingtime = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=9)
    complaincategoryid = models.IntegerField()
    clienttypeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ssphelpdesk'


class Sspinboxclient(models.Model):
    inboxclientid = models.IntegerField(primary_key=True)
    clientid = models.ForeignKey(Sspclient, db_column='clientid')
    notifid = models.ForeignKey('Sspnotification', db_column='notifid')
    msgstatusid = models.ForeignKey('Sspmsgstatus', db_column='msgstatusid')

    class Meta:
        managed = False
        db_table = 'sspinboxclient'


class Sspinboxmerchant(models.Model):
    inboxmerchantid = models.IntegerField(primary_key=True)
    merchantid = models.ForeignKey('Sspmerchant', db_column='merchantid')
    notifid = models.ForeignKey('Sspnotification', db_column='notifid')
    msgstatusid = models.ForeignKey('Sspmsgstatus', db_column='msgstatusid')

    class Meta:
        managed = False
        db_table = 'sspinboxmerchant'


class Sspincomingfunds(models.Model):
    incomingfundsid = models.IntegerField(primary_key=True)
    refnumber = models.CharField(max_length=30)
    transfertime = models.DateTimeField()
    amount = models.FloatField()
    applicantname = models.CharField(max_length=50)
    applicantbank = models.IntegerField()
    applicantcity = models.IntegerField()
    applicantaccountnumber = models.CharField(max_length=50)
    transferrefnumber = models.CharField(max_length=30)
    status = models.CharField(max_length=8)
    action = models.TextField()

    class Meta:
        managed = False
        db_table = 'sspincomingfunds'


class Sspjournal(models.Model):
    journalid = models.IntegerField(primary_key=True)
    journaldatetime = models.DateTimeField()
    debitid = models.CharField(max_length=20)
    creditid = models.CharField(max_length=20)
    referencenumber = models.CharField(max_length=20)
    transaction = models.CharField(max_length=20)
    total = models.FloatField()
    categoryid = models.ForeignKey(Sspcategory, db_column='categoryid', blank=True, null=True)
    buyerinitialbalance = models.FloatField()
    sellerinitialbalance = models.FloatField()
    buyerinitialsubbalance = models.FloatField()
    sellerinitialsubbalance = models.FloatField()
    transactionmemberid = models.ForeignKey('Ssptransactionmember', db_column='transactionmemberid')
    wallettransactiontypeid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sspjournal'


class Ssploginhistoryadministrator(models.Model):
    loginhistoryid = models.IntegerField(primary_key=True)
    adminid = models.IntegerField()
    session = models.CharField(max_length=50)
    logindate = models.DateTimeField()
    logoutdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ssploginhistoryadministrator'


class Ssploginhistoryclient(models.Model):
    loginhistoryid = models.IntegerField(primary_key=True)
    clientid = models.ForeignKey(Sspclient, db_column='clientid')
    session = models.CharField(max_length=50)
    logindate = models.DateTimeField()
    logoutdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ssploginhistoryclient'


class Ssploginhistoryemployee(models.Model):
    loginhistoryid = models.IntegerField(primary_key=True)
    employeeid = models.ForeignKey(Sspemployee, db_column='employeeid')
    session = models.CharField(max_length=50)
    logindate = models.DateTimeField()
    logoutdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssploginhistoryemployee'


class Ssploginhistorymerchant(models.Model):
    loginhistoryid = models.IntegerField(primary_key=True)
    merchantid = models.ForeignKey('Sspmerchant', db_column='merchantid')
    session = models.CharField(max_length=50)
    logindate = models.DateTimeField()
    logoutdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssploginhistorymerchant'


class Sspmerchant(models.Model):
    merchantid = models.CharField(primary_key=True, max_length=20)
    accountnumber = models.CharField(max_length=20)
    merchanttypeid = models.ForeignKey('Sspmerchanttype', db_column='merchanttypeid')
    name = models.TextField()
    personincharge = models.CharField(max_length=100)
    phonenumber = models.TextField()
    email = models.TextField()
    address1 = models.TextField()
    address2 = models.TextField(blank=True)
    postalcode = models.TextField()
    cityid = models.IntegerField()
    provinceid = models.IntegerField()
    stateid = models.IntegerField()
    loginstatus = models.IntegerField(blank=True, null=True)
    lastlogin = models.DateTimeField(blank=True, null=True)
    joindate = models.DateTimeField()
    sysstatus = models.CharField(max_length=3)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    

    class Meta:
        managed = False
        db_table = 'sspmerchant'
        verbose_name = "data1"


class Sspmerchantbalance(models.Model):
    merchantbalanceid = models.IntegerField(primary_key=True)
    merchantid = models.ForeignKey(Sspmerchant, db_column='merchantid')
    accountnumber = models.CharField(max_length=20)
    balance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sspmerchantbalance'


class Sspmerchantcomplaint(models.Model):
    merchantcomplaintid = models.IntegerField(primary_key=True)
    merchantid = models.CharField(max_length=25)
    datetime = models.DateTimeField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'sspmerchantcomplaint'


class Sspmerchantloginfailed(models.Model):
    loginfailedid = models.IntegerField(primary_key=True)
    merchantid = models.ForeignKey(Sspmerchant, db_column='merchantid')
    logindate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sspmerchantloginfailed'


class Sspmerchantmember(models.Model):
    merchantmemberid = models.IntegerField(primary_key=True)
    merchantid = models.ForeignKey(Sspmerchant, db_column='merchantid')
    memberid = models.CharField(max_length=20)
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sspmerchantmember'


class Sspmerchantmutation(models.Model):
    mutationid = models.IntegerField(primary_key=True)
    merchantid = models.ForeignKey(Sspmerchant, db_column='merchantid')
    mutationdate = models.DateTimeField()
    mutationtypeid = models.ForeignKey('Sspmutationtype', db_column='mutationtypeid')
    initialbalance = models.IntegerField()
    finalbalance = models.IntegerField()
    information = models.TextField()

    class Meta:
        managed = False
        db_table = 'sspmerchantmutation'


class Sspmerchanttype(models.Model):
    merchanttypeid = models.IntegerField(primary_key=True)
    merchanttype = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sspmerchanttype'
        verbose_name="data1"


class Sspmsgstatus(models.Model):
    msgstatusid = models.IntegerField(primary_key=True)
    msgstatus = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sspmsgstatus'


class Sspmutationtype(models.Model):
    mutationtypeid = models.IntegerField(primary_key=True)
    mutationtype = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sspmutationtype'


class Sspnotification(models.Model):
    notificationid = models.IntegerField(primary_key=True)
    senddate = models.DateTimeField()
    title = models.TextField()
    text = models.TextField()
    notiftypeid = models.ForeignKey('Sspnotiftype', db_column='notiftypeid')
    recievertypeid = models.ForeignKey('Ssprecievertype', db_column='recievertypeid')

    class Meta:
        managed = False
        db_table = 'sspnotification'


class Sspnotiftype(models.Model):
    notiftypeid = models.IntegerField(primary_key=True)
    notiftype = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sspnotiftype'


class Sspprivileges(models.Model):
    privilegesid = models.IntegerField(primary_key=True)
    positionid = models.ForeignKey(Sspemployeeposition, db_column='positionid')
    privileges = models.TextField()

    class Meta:
        managed = False
        db_table = 'sspprivileges'


class Ssppromo(models.Model):
    promoid = models.IntegerField(primary_key=True)
    vendorid = models.CharField(max_length=20)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    title = models.TextField()
    text = models.TextField()
    initialprice = models.FloatField()
    newprice = models.FloatField()
    promostatus = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'ssppromo'


class Ssppromostatus(models.Model):
    promostatusid = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'ssppromostatus'


class Ssprecievertype(models.Model):
    recievertypeid = models.IntegerField(primary_key=True)
    recievertype = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'ssprecievertype'


class Ssprefillsubbalance(models.Model):
    refillsubbalanceid = models.IntegerField(primary_key=True)
    datetime = models.DateTimeField()
    clientid = models.CharField(max_length=30)
    amount = models.FloatField()
    status = models.CharField(max_length=9)
    refnumber = models.CharField(max_length=30, blank=True)
    initialbalance = models.FloatField()
    initialsubbalance = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ssprefillsubbalance'


class Ssprefunds(models.Model):
    refundsid = models.IntegerField(primary_key=True)
    refundtime = models.DateTimeField()
    amount = models.FloatField()
    beneficiaryname = models.CharField(max_length=50)
    beneficiarybank = models.IntegerField()
    beneficiarycity = models.IntegerField()
    beneficiaryaccountnumber = models.CharField(max_length=50)
    status = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'ssprefunds'


class Sspreportbilling(models.Model):
    reportbillingid = models.IntegerField(primary_key=True)
    employeeid = models.ForeignKey(Sspemployee, db_column='employeeid')
    inputdate = models.DateTimeField()
    report = models.TextField()
    updatedate = models.DateTimeField()
    additionalreport = models.TextField()

    class Meta:
        managed = False
        db_table = 'sspreportbilling'


class Sspreportcsclient(models.Model):
    reportcsclientid = models.IntegerField(primary_key=True)
    employeeid = models.ForeignKey(Sspemployee, db_column='employeeid')
    inputdate = models.DateTimeField()
    report = models.TextField()
    updatedate = models.DateTimeField()
    additionalreport = models.TextField()

    class Meta:
        managed = False
        db_table = 'sspreportcsclient'


class Sspreportcsmerchant(models.Model):
    reportcsmerchantid = models.IntegerField(primary_key=True)
    employeeid = models.ForeignKey(Sspemployee, db_column='employeeid')
    inputdate = models.DateTimeField()
    report = models.TextField()
    updatedate = models.DateTimeField()
    additionalreport = models.TextField()

    class Meta:
        managed = False
        db_table = 'sspreportcsmerchant'


class Sspsmstemplate(models.Model):
    smstemplateid = models.IntegerField(primary_key=True)
    smstemplate_code = models.CharField(max_length=20)
    smstemplate = models.TextField()
    language = models.CharField(max_length=7)
    parameterdetail = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sspsmstemplate'


class Ssptopupinfo(models.Model):
    topupid = models.IntegerField(primary_key=True)
    clientid = models.ForeignKey(Sspclient, db_column='clientid')
    topupdate = models.DateTimeField()
    amount = models.IntegerField()
    destinationbank = models.IntegerField()
    topupstatusid = models.CharField(max_length=8)
    refnumber = models.CharField(unique=True, max_length=255)
    topuptypeid = models.ForeignKey('Ssptopuptype', db_column='topuptypeid')

    class Meta:
        managed = False
        db_table = 'ssptopupinfo'


class Ssptopupinfomerchant(models.Model):
    topupinfomerchantid = models.IntegerField(primary_key=True)
    merchantid = models.ForeignKey(Sspmerchant, db_column='merchantid')
    topupdate = models.DateTimeField()
    amount = models.FloatField()
    destinationbank = models.ForeignKey(Sspbankofssp, db_column='destinationbank')
    topupstatusid = models.CharField(max_length=8)
    refnumber = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'ssptopupinfomerchant'


class Ssptopuptype(models.Model):
    topuptypeid = models.IntegerField(primary_key=True)
    topuptype = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'ssptopuptype'


class Ssptransaction(models.Model):
    transactionid = models.CharField(primary_key=True, max_length=20)
    transactionstatus = models.CharField(max_length=9, blank=True)
    transactiondate = models.DateTimeField()
    buyeraccount = models.CharField(max_length=20, blank=True)
    selleraccount = models.CharField(max_length=20, blank=True)
    amount = models.IntegerField()
    session = models.TextField()
    transactiontypeid = models.ForeignKey('Ssptransactiontype', db_column='transactiontypeid')
    refnumber = models.CharField(max_length=50, blank=True)
    transactionmethodid = models.ForeignKey('Ssptransactionmethod', db_column='transactionmethodid', blank=True, null=True)
    transactionmemberid = models.ForeignKey('Ssptransactionmember', db_column='transactionmemberid')
    wallettransactiontypeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ssptransaction'


class Ssptransactionmember(models.Model):
    transactionmemberid = models.IntegerField(primary_key=True)
    transactionmember = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ssptransactionmember'


class Ssptransactionmethod(models.Model):
    transactionmethodid = models.IntegerField(primary_key=True)
    transactionmethod = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ssptransactionmethod'


class Ssptransactiontype(models.Model):
    transactiontypeid = models.IntegerField(primary_key=True)
    transactiontype = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ssptransactiontype'


class Ssptransdetailbuyerclient(models.Model):
    transdetailbuyerclientid = models.CharField(primary_key=True, max_length=20)
    transactionid = models.CharField(max_length=20)
    session = models.TextField(blank=True)
    transactiondetaildate = models.DateTimeField()
    buyerid = models.CharField(max_length=20, blank=True)
    buyeraccount = models.CharField(max_length=20, blank=True)
    sellerid = models.CharField(max_length=20, blank=True)
    selleraccount = models.CharField(max_length=20, blank=True)
    amount = models.FloatField()
    information = models.TextField(blank=True)
    refnumberbuyer = models.CharField(unique=True, max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'ssptransdetailbuyerclient'


class Ssptransdetailbuyermerchant(models.Model):
    transdetailbuyermerchantid = models.CharField(unique=True, max_length=20)
    transactionid = models.CharField(max_length=20)
    session = models.TextField()
    transactiondetaildate = models.DateTimeField()
    buyerid = models.CharField(max_length=20)
    buyeraccount = models.CharField(max_length=20)
    merchantid = models.CharField(max_length=20)
    merchantaccount = models.CharField(max_length=20)
    amount = models.IntegerField()
    information = models.TextField()
    refnumberbuyer = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ssptransdetailbuyermerchant'


class Ssptransdetailsellerclient(models.Model):
    transdetailsellerclientid = models.CharField(primary_key=True, max_length=20)
    transactionid = models.CharField(max_length=20, blank=True)
    session = models.TextField()
    transactiondetaildate = models.DateTimeField()
    buyerid = models.CharField(max_length=20, blank=True)
    buyeraccount = models.CharField(max_length=20, blank=True)
    sellerid = models.CharField(max_length=20, blank=True)
    selleraccount = models.CharField(max_length=20, blank=True)
    amount = models.IntegerField()
    tax = models.IntegerField()
    service = models.IntegerField()
    total = models.IntegerField()
    information = models.TextField(blank=True)
    refnumberseller = models.CharField(max_length=20)
    wallettransactiontypeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ssptransdetailsellerclient'


class Ssptransdetailsellermerchant(models.Model):
    transdetailsellermerchantid = models.CharField(primary_key=True, max_length=20)
    transactionid = models.CharField(max_length=20)
    session = models.TextField()
    transactiondetaildate = models.DateTimeField()
    buyerid = models.CharField(max_length=20)
    buyeraccount = models.CharField(max_length=20)
    merchantid = models.CharField(max_length=20)
    merchantaccount = models.CharField(max_length=20)
    amount = models.IntegerField()
    tax = models.IntegerField()
    service = models.IntegerField()
    total = models.IntegerField()
    information = models.TextField()
    refnumberseller = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ssptransdetailsellermerchant'


class Sspwallettransactiontype(models.Model):
    wallettransactiontypeid = models.IntegerField(primary_key=True)
    wallettransactiontype = models.CharField(max_length=50)
    alias = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'sspwallettransactiontype'
