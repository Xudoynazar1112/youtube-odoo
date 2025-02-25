from odoo import api, fields, models


class Person(models.Model):
    _name = "my_person"
    _description = "It is about a person personality."

    name = fields.Char(string="Name", compute="_compute_name")
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    age = fields.Integer(string="Age")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")

    @api.depends("first_name", "last_name")
    def _compute_name(self):
        for record in self:
            if record.first_name and record.last_name:
                record.name = f"{record.first_name} {record.last_name}"
            else:
                record.name = "New"
