from odoo import models, fields, api
    
#nama class dibiarin tidak masalah yg penting _name nya bedain untuk dipasang di secutrity
class mubethrentcar(models.Model): 
    _name = "mubethrentcar.service"
    _description = "Teknik Pemeliharaan mobil"

    name = fields.Selection(
        string='Jenis Service',
        selection=[('biasa', 'biasa'), ('istimewa', 'istimewa'), ('spesial', 'spesial'), ('super','super')]
    )
    teknik = fields.Selection(
        string='Teknik service',
        selection=[('Large', 'All'), ('Medium', 'Machine'), ('Small', 'Oil')]
    )
    hasil = fields.Selection(
        string='Hasil Service',
        selection=[('Ringan', 'Ringan'), ('Sedang', 'Sedang'), ('Berat', 'Berat')]
    )
    tersedia = fields.Boolean(
        string='tersedia',
        default=True
    )
    deskripsiservice = fields.Char(
        string='deskripsi',
        help='Isi dengan Service dari mobil'
    )
    models_id = fields.One2many(
        comodel_name='mubethrentcar.jenismobil',
        inverse_name='service_id',
        string='Deskripsi Mobil'
    )
    pegawainya_id = fields.Many2one(
        comodel_name='res.partner',
        string='Penanggung Jawab',
        domain=[('is_pegawai','=','True')]
    )