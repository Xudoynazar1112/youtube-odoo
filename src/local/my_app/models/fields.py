from odoo import fields, models


# Kategoriya modeli
class BookCategory(models.Model):
    _name = "library.category"
    _description = "Book Category"

    name = fields.Char(string="Category Name", required=True)


# Kitob modeli
class Book(models.Model):
    _name = "library.book"
    _description = "Book"

    name = fields.Char(string="Book Name", required=True)
    category_id = fields.Many2one("library.category", string="Category")


# Buyurtma modeli
class Order(models.Model):
    _name = "shop.order"
    _description = "Order"

    name = fields.Char(string="Order Name", required=True)
    customer_id = fields.Many2one("shop.customer", string="Customer", required=True)
    order_date = fields.Date(string="Order Date", default=fields.Date.today)


# Mijoz modeli
class Customer(models.Model):
    _name = "shop.customer"
    _description = "Customer"

    name = fields.Char(string="Customer Name", required=True)
    email = fields.Char(string="Email")
    order_ids = fields.One2many("shop.order", "customer_id", string="Orders")


# Kurs modeli
class Course(models.Model):
    _name = "academy.course"
    _description = "Course"

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text(string="Description")
    student_ids = fields.Many2many("academy.student", string="Students")


# O‘quvchi modeli
class Student(models.Model):
    _name = "academy.student"
    _description = "Student"

    name = fields.Char(string="Student Name", required=True)
    age = fields.Integer(string="Age")
    course_ids = fields.Many2many("academy.course", string="Courses")
