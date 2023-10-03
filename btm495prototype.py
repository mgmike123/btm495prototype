#SUBMISSION 1: Creating classes used in primary use case
class Manager:
    def Manager(self,name,age):
        self._name = name
        self._age = age

class Accountant:
    def Accountant(self, age):
        self._age = age

class Reports:
   
    def Reports(self, doc_ID, doctype, category, year,payment):
        self._doc_ID = doc_ID
        self._doctype = doctype
        self._category = category
        self._year = year
        self._reports = []
        self._payment = payment

    def create(self, doc_ID):
        self._reports.append(doc_ID)
    def update(self,doc_ID):
        self._reports.remove
        self._reports.append(doc_ID)

class ClientList:
    def Clientlist(self, name, age, company):
        self._name = name
        self._age = age
        self._company = company
    def open(self, ClientList):
        self._name.open(ClientList)
    def modify(self, name):
        self._name.remove
        self._name.append(name)

class PaymentStatus:
    def PaymentStatus(self, status, date):
        self._status = status
        self._date = date
    def open(self, PaymentStatus):
        self._name.open(PaymentStatus)
class PaymentReminder:
    def PaymentReminder(self, recipient, contents, paymentAmount):
        self._recipient = recipient
        self._contents = contents
        self.paymentAmount = paymentAmount

class Invoices:
    def Invoices(self, recipient, date, amount):
        self._recipient = recipient
        self._date = date
        self._amount = amount
    def open(self, Invoices):
        self._name.open(Invoices)
    def update(self, recipient):
        self._recipient.remove
        self._recipient.append(recipient)

#SUBMISSION 2: Running methods on classes appropriate to the processes found in use case
#Creation of report object
Report = Reports(1,"Word","Payment","2023")
Report.create(1)
#Appending new ID to report
Report.append(2)
#Creation of client list
Clientlist = ClientList("James Greer", 43, "Grinder")
#viewing clientList
Clientlist.open()
#Modifying client (changing name from James Greer to John Digweed)
Clientlist.modify("John Digweed")
#Viewing Payment Status
Paymentstatus = PaymentStatus("On Time", "2023-02-23")
#Viewing Invoices
invoice = Invoices("James Greer", "2023-02-23", 500)
invoice.open()
#Updating Invoices
invoice.update("John Digweed")
