{
    "name": "Estate Management",
    "version": "1.0",
    "summary": "Module for managing real estate properties",
    "description": """
        Estate Management Module
        ========================
        This module helps in managing real estate properties including
        property listings, sales, and rentals.
    """,
    "author": "Xudoynazar",
    "website": "http://t.me/Xudoynazar_Saparov",
    "category": "Real Estate",
    "depends": ["base"],
    "data": [
        "views/estate_property_views.xml",
        "views/estate_property_type_view.xml",
        "views/estate_property_tags_view.xml",
        "views/estate_property_offer_view.xml",
        "views/estate_menus.xml",
        "security/ir.model.access.csv",
    ],
    # 'demo': [
    #     # List of demo data files, if any
    # ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
