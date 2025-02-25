from odoo import fields, models


class CustomModel(models.Model):
    _name = "custom.model"  # Modelning texnik nomi
    _inherit = [
        "mail.thread",
        "mail.activity.mixin",
    ]  # Faoliyatlar qo'llab-quvvatlanadi
    _description = "Custom Model for Testing Views"  # Modelning tavsifi

    # Asosiy maydonlar
    name = fields.Char(string="Name", required=True)  # Ism
    date_start = fields.Datetime(string="Start Date")  # Kalendaryo uchun kerak
    date_end = fields.Datetime(string="End Date")  # Kalendaryo uchun ixtiyoriy
    progress = fields.Float(
        string="Progress", default=0.0
    )  # Bajarilish foizi (ixtiyoriy)
    partner_id = fields.Many2one("res.partner")
    date_of_birth = fields.Date(string="Date of Birth")  # Tug'ilgan sana
    address = fields.Text(string="Address")  # Manzil
    phone = fields.Char(string="Phone")  # Telefon raqami
    email = fields.Char(string="Email")  # Email
    job_position = fields.Char(string="Job Position")  # Lavozim
    salary = fields.Float(string="Salary")  # Maosh
    image = fields.Image(string="Image")  # Rasm
    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("active", "Active"),
            ("inactive", "Inactive"),
        ],
        string="Status",
        default="draft",
    )  # Holat
    description = fields.Html(string="Description")  # Tavsif (HTML formatda)

    # Qo'shimcha maydonlar
    tags = fields.Many2many("custom.tag", string="Tags")  # Teglar
    is_active = fields.Boolean(string="Is Active", default=True)  # Faollik belgisi
    sequence = fields.Integer(string="Sequence", default=10)  # Ketma-ketlik


# Teglar uchun qo'shimcha model
class CustomTag(models.Model):
    _name = "custom.tag"
    _description = "Custom Tags"

    name = fields.Char(string="Tag Name", required=True)
    color = fields.Integer(string="Color")  # Teg uchun rang
