from odoo import fields, models


class MyWidgets(models.Model):
    _name = "my_widgets"
    _description = "My Widgets"

    name = fields.Char("Title", required=True)
    url = fields.Char("URL")
    text = fields.Text("Text")
    email = fields.Char("Email")
    phone = fields.Char("Phone")
    filter_domain = fields.Char("Filter Domain")
    count = fields.Integer("Count")
    color = fields.Char("Color")
    sold_count = fields.Integer("Sold Count")
    sequence = fields.Integer("Sequence")
    price = fields.Float("Price")
    discount = fields.Float("Discount")
    time = fields.Float("Time")
    date = fields.Date("Date")
    date_begin = fields.Date("Begin")
    date_end = fields.Date("End")
    priority = fields.Integer("Priority")
    state = fields.Boolean("State")
    status = fields.Selection(
        [("publish", "Published"), ("unpublish", "Unpublished")], string="Status"
    )
    file = fields.Binary("File")
    author_id = fields.Many2one("res.partner", string="Author")
    tag_ids = fields.Many2many("res.company", string="Tags")
    published = fields.Boolean("Published")
