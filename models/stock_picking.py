from odoo import models, fields, api
import requests

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def send_to_fastapi(self):
        for picking in self:
            payload = {
                'picking_id': picking.id,
                'origin': picking.origin,
                'partner_id': picking.partner_id.id if picking.partner_id else None,
                'location_id': picking.location_id.id if picking.location_id else None,
                'location_dest_id': picking.location_dest_id.id if picking.location_dest_id else None,
                # Add more fields as necessary
            }
            try:
                response = requests.post(
                    'https://fastapi-connector.onrender.com/api/odoo/stock_picking',
                    json=payload,
                    headers={'Content-Type': 'application/json'}
                )
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise UserError(f"Failed to send data to FastAPI: {str(e)}")

    def button_validate(self):
        res = super(StockPicking, self).button_validate()
        self.send_to_fastapi()
        return res