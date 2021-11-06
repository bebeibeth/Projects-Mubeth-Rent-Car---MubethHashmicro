from odoo import models, fields, api

class Partner(models.Model): 
    _inherit = 'res.partner'

    is_pegawai = fields.Boolean(
        string= 'Pegawai', 
        default=False 
    )
    is_customer = fields.Boolean(
        string='Customer',
        default=False
    )
    is_menikah = fields.Boolean(
        string='Sudah Menikah', 
        default=True
    )