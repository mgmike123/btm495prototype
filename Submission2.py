class Supplier:
    def __init__(self, supp_id, first_name, last_name, email, phone_number):
        self.supp_id = supp_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def update_supplier_information(self, new_info):
        self.supp_id.update(new_info)

    def retrieve_supplier_data(self, info):
        self.supp_id.retrieve(info)

    def generate_supplier_report(self, report):
        self.supp_id.generate(report)


class Transaction:
    def __init__(self, tran_id, tran_date, tran_type, amount, description, status, order_id, invoice_id):
        self.tran_id = tran_id
        self.tran_date = tran_date
        self.tran_type = tran_type
        self.amount = amount
        self.description = description
        self.status = status
        self.order_id = order_id
        self.invoice_id = invoice_id

    def get_transaction_details(self, transactionDetails):
        self.tran_id.get(transactionDetails)

    def void_transaction(self):
        self.tran_id.void(self)

    def update_transaction_details(self, new_details):
        self.tran_id.update(new_details)

    def record_transaction(self):
        self.tran_id.record(self)

    def get_invoice_details(self, invoiceDetails):
        self.tran_id.get(invoiceDetails)


class Order:
    def __init__(self, quantity, price, description, product_id):
        self.quantity = quantity
        self.price = price
        self.description = description
        self.product_id = product_id

    def add_product(self, product):
        self.quantity.append(product)

    def remove_product(self, product):
        self.quantity.remove(product)


class Client:
    def __init__(self, client_id, email, phone_number):
        self.client_id = client_id
        self.email = email
        self.phone_number = phone_number

    def update_contact_info(self,contact):
        self.client_id.update(contact)

    def retrieve_client_data(self):
        self.client_id.retrieve(self)

    def add_invoice(self, invoice):
        self.client_id.append(invoice)

    def get_client_list(self):
        self.client_id.get(self)

    def view_client_data(self, client_id):
        self.client_id.view(client_id)

    def update_client_information(self):
        self.client_id.update(self)

    def save_client_list(self):
        self.client_id.save(self)

    def review_client_list(self):
        self.client_id.review(self)


class Report:
    def __init__(self, report_id, name, report_type, date, status, approval, recipient):
        self.report_id = report_id
        self.name = name
        self.report_type = report_type
        self.date = date
        self.status = status
        self.approval = approval
        self.recipient = recipient

    def generate_report_data(self):
        self.report_id.generate(self)

    def export_report(self, format):
        self.report_id.export(self)

    def create_report_data(self):
        self.report_id.create(self)

    def retrieve_report_data(self):
        self.report_id.retrieve(self)

    def manipulate_report_data(self):
        self.report_id.manipulate(self)

    def edit_report_data(self):
        self.report_id.edit(self)


class Employee:
    def __init__(self, first_name, last_name, date_of_birth, phone_number, age, role):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.age = age
        self.role = role


class Accountant(Employee):
    def send_payment_reminder(self,payment_reminder):
        self.payment_reminder = payment_reminder
        self.payment_reminder.send(payment_reminder)


class Manager(Employee):
    def review_report_data(self,report):
        self.report = report
        self.report.review(report)

    def approve_report_data(self,report):
        self.report.approve(report)

    def approve_report(self, approver):
        self.report.approve(approver)


class Invoices:
    def __init__(self, invoice_id, invoice_date, due_date, total_amount, detail):
        self.invoice_id = invoice_id
        self.invoice_date = invoice_date
        self.due_date = due_date
        self.total_amount = total_amount
        self.detail = detail

    def get_invoice_list(self):
        self.invoice_id.get(self)

    def generate_invoice(self):
        self.invoice_id.generate(self)

    def review_invoice(self):
        self.invoice_id.review(self)

    def update_invoice_information(self):
        self.invoice_id.update(self)

    def save_invoice_information(self):
        self.invoice_id.save(self)


class User:
    def __init__(self, user_id, password, login_status):
        self.user_id = user_id
        self.password = password
        self.login_status = login_status

    def verify_login(self):
        self.user_id.verify(self)

    def login(self, username, password):
        self.user_id.login(username, password)


class Product:
    def __init__(self, product_id, name, description, price):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price

    def add_product_to_catalog(self, product_details):
        self.product_id.add(product_details)

    def update_product_details(self, product_id, new_details):
        self.product_id.update(product_id, new_details)

    def get_product_details(self, product_id):
        self.product_id.get(product_id)

    def list_products(self):
        self.product_id.list(self)
