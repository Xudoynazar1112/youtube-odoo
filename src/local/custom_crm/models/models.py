from odoo import fields, models


class MyCourse(models.Model):
    _name = "crm.mycourse"
    _description = "My Course"

    name = fields.Char("Course Name", required=True)
    price = fields.Float("Price")
    teacher_id = fields.Many2one("crm.teacher", string="Techner")
    student_ids = fields.Many2many("crm.student", string="Students")


class MyStudent(models.Model):
    _name = "crm.student"
    _description = "My Student"

    name = fields.Char("Student Name", required=True)
    first_name = fields.Char("Student First Name", required=True)
    last_name = fields.Char("Student Last Name", required=True)
    course_ids = fields.Many2many("crm.mycourse", string="Courses")
    phone = fields.Char("Phone")
    email = fields.Char("Email")
    age = fields.Integer("Age")


class MyTeacher(models.Model):
    _name = "crm.teacher"
    _description = "My Teacher"

    name = fields.Char("Student Name", required=True)
    first_name = fields.Char("Student First Name", required=True)
    last_name = fields.Char("Student Last Name", required=True)
    course_ids = fields.One2many("crm.mycourse", "teacher_id", string="Courses")
