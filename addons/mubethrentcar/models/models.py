from odoo import models, fields, api 

class ModelDasar (models.Model) : 
    _name = "mubethrentcar.modeldasar"
    _description = "Model dasar mubeth rent car"

    kapasitas = fields.Char(
        string='kapasitas penumpang',
        Required=True,
    )
    tipe = fields.Selection(
        string='tipe/jenis mobil',
        selection=[('sedan', 'Sedan'), ('lcgc', 'LCGC'), ('mpv', 'MPV'), ('suv', 'SUV')]
    )

class mubethrentcar(models.Model) : 
    _name = "mubethrentcar.jenismobil"
    _description = "Daftar Jenis-jenis mobil"
    _inherit = 'mubethrentcar.modeldasar' 
    #memanggil model class yg atas inheriten delegation

    name = fields.Char(
        string='Jenis Sewa',
        Required=True
    )
    harga = fields.Integer(
        string='Harga sewa',
        Required=True
    )
    active = fields.Boolean(
        default = True
    )
    service_id = fields.Many2one(
        comodel_name='mubethrentcar.service', 
        string='Pemeliharaan', 
        Required=True,
        delegate=True
    )