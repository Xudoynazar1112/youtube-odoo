from odoo import fields, models


class MyModel(models.Model):
    _name = "my.model"
    _description = "This is my model"

    name = fields.Char()
    value = fields.Integer()
