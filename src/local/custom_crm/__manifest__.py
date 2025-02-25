{
    "name": "Custom CRM",
    "summary": """Shunchaki kulib yashang :)""",
    "description": """
        Long description of module's purpose
    """,
    "author": "Xudoynazar",
    "website": "https://github.com/Xudoynazar1112",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/actions_view.xml",
        "views/course_view.xml",
        "views/menu_item.xml",
        "views/student_view.xml",
        "views/teacher_view.xml",
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    "sequence": -1000,
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
