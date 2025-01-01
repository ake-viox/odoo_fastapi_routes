from odoo import models, fields, api
import requests

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def send_to_fastapi(self):
        for picking in self:
            payload = {
            'picking_name': picking.name,
            'origin': picking.origin,
            'partner': {
                'id': picking.partner_id.id if picking.partner_id else None,
                'name': picking.partner_id.name if picking.partner_id else None,
                'street': picking.partner_id.street if picking.partner_id else None,
                'zip': picking.partner_id.zip if picking.partner_id else None,
                'city': picking.partner_id.city if picking.partner_id else None,
                'country': picking.partner_id.country_id.name if picking.partner_id and picking.partner_id.country_id else None,
            },
            'location': picking.location_id.name if picking.location_id else None,
            'location_dest': picking.location_dest_id.name if picking.location_dest_id else None,
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