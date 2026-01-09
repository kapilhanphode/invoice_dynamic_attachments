# -*- coding: utf-8 -*-

{
    # Module Info
    "name": "Invoice Dynamic Attachments",
    "version": "19.0.1.0.0",
    "category": "Accounting",
    "summary": "Dynamic attachment numbers per invoicing line",
    "description": """
        Generates attachment number for each section
        Generate dummy attachment automatically
        Clicking attachment number nevigatests to attachment
    """,

    # Author
    "author": "Kapil",

    # Dependencies
    "depends": ["account"],

    # Data File
    "data": [
        "reports/invoice_report.xml",
    ],

    # Technical Info
    "installable": True,
    "application": False,
}
