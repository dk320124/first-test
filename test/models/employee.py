from odoo import fields, models, api


class EmployeeExpense(models.Model):
    _name = 'employee.expense'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Name", help="enter the name please")
    Employees_id = fields.Many2one('res.users', string='Employee Id', default=lambda self: self.env.user)
    expense_type = fields.Selection([('domestic', 'Domestic'), ('international', 'International')],
                                    string='Expense Type')
    state = fields.Selection(
        [('draft', 'Draft'), ('inprogress', 'In Progress'), ('done', 'Done'), ('cancel', 'Cancelled')], string='Status',
        default='draft')
    attachment = fields.Binary(string='Attachment')
    amount = fields.Float(string='Amount', tracking=True)

    def action_is_inprogress(self):
        for rec in self:
            rec.state = 'inprogress'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
