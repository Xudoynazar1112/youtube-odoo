from dateutil.relativedelta import relativedelta

from odoo import api, exceptions, fields, models


class Property(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(
        string="Availibility Date",
        default=fields.Date.today() + relativedelta(months=3),
    )
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Number of Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Number of Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden", default=True)
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        [
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
        string="Garden Orientation",
    )
    active = fields.Boolean(string="Active", default=False)
    total_area = fields.Float(string="Total Area", compute="_compute_total_area")
    best_price = fields.Float(string="Best Price", compute="_compute_best_price")
    state = fields.Selection(
        [
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        default="new",
        required=True,
        copy=False,
    )

    tag_ids = fields.Many2many("estate.property.tag", string="Property Tag")
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer = fields.Char(string="Buyer", copy=False)
    salesperson = fields.Many2one(
        "res.users",
        string="Selesperson",
        required=True,
        default=lambda self: self.env.user,
    )

    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = record.expected_price
            for offer in record.offer_ids:
                if offer.price > record.best_price:
                    record.best_price = offer.price

    @api.onchange("garden")
    def _onchange_garden(self):
        self.garden_area = 10
        self.garden_orientation = "north"

    def action_sold(self):
        if self.state != "canceled":
            self.state = "sold"
        else:
            raise exceptions.UserError("You cannot sell this property.")

    def action_canceled(self):
        if self.state != "sold":
            self.state = "canceled"
        else:
            raise exceptions.UserError("You cannot cancel this property.")
