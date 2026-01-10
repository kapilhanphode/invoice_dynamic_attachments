import base64
from odoo import models, fields


class AccountMove(models.Model):
    _inherit = "account.move"
    _description = "AccountMove"

    def action_post(self):
        res = super(AccountMove, self).action_post()

        for move in self:
            if move.move_type not in ("out_invoice", "out_refund"):
                continue
            attachment_no = 0
            for line in move.invoice_line_ids.sorted("sequence"):
                if line.display_type != "line_section":
                    continue
                attachment_no += 1
                if not line.attachment_id:
                    attachment = self.env["ir.attachment"].create({
                        "name": f"{move.name or 'Invoice'} - Attachment {attachment_no}",
                        "type": "binary",
                        "datas": base64.b64encode(
                            f"Dummy attachment for section {attachment_no}".encode()
                        ),
                        "res_model": "account.move",
                        "res_id": move.id,
                        "mimetype": "text/plain",
                    })
                    line.attachment_id = attachment.id
                line.attachment_number = attachment_no

        return res

    def _get_attachment_report_data(self):
        self.ensure_one()
        return {
            "attachment_lines": self.invoice_line_ids.filtered(
                lambda l:
                l.display_type == "line_section"
                and l.attachment_id
                and l.attachment_number
            ).sorted(key=lambda l: l.attachment_number),
        }


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"
    _description = "Account Move Line"

    attachment_id = fields.Many2one("ir.attachment", string="Attachment", copy=False)
    attachment_number = fields.Integer(string="Attachment Number", readonly=True, copy=False)
