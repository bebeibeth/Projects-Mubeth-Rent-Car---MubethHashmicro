from odoo import api, fields, models

class OrderMobil(models.Model):
    _name = 'mubethrentcar.ordermobil'
    _description = 'New Description'

    name = fields.Char(
        string='Kode Order',
        Required=True,
    )
    pemesan_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Nama Pemesan',
        domain=[('is_customer','=','True')]
    )
    tanggal_pesan = fields.Datetime(
        string='Tanggal pesanan',
        default=fields.Datetime.now
    )
    detailjenis_ids = fields.One2many(
        comodel_name='mubethrentcar.detailorder', 
        inverse_name='order_id', 
        string='Detail Pesanan'
    )

class DetailOrder(models.Model) : 
    _name = 'mubethrentcar.detailorder'
    _description = 'Detail Orderan Customer'

    name = fields.Char(
        string='Kode Order'
    )

    order_id = fields.Many2one(
        comodel_name='mubethrentcar.ordermobil',
        string='Order Mobil'
    )
    
    jenissewa_id = fields.Many2one(
        comodel_name='mubethrentcar.jenismobil', 
        string='Jenis Sewa Mobil'
    )
    harga = fields.char(
        compute='_compute_harga', 
        string='Harga Sewa'
    )

    @api.depends('jenissewa_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.jenissewa_id.harga