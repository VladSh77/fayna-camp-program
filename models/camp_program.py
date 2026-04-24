from odoo import api, fields, models


class CampProgram(models.Model):
    _name = "camp.program"
    _description = "Camp program execution per shift"
    _order = "event_id, sequence"

    event_id = fields.Many2one(
        "event.event",
        required=True,
        ondelete="cascade",
        string="Camp shift (event)",
        help="The specific shift/заїзд this program is for",
    )
    product_tmpl_id = fields.Many2one(
        "product.template",
        related="event_id.camp_program_id",
        store=True,
        string="Camp template",
    )

    sequence = fields.Integer(default=10, string="Sequence")
    name = fields.Char(
        required=True,
        string="Program title",
        help="e.g. 'Morning hike', 'Team building activity'",
    )

    # Schedule linkage
    schedule_entry_id = fields.Many2one(
        "camp.schedule.entry",
        string="Scheduled activity",
        help="Link to the master schedule (if this program is a variant of master schedule)",
        domain="[('product_tmpl_id', '=', product_tmpl_id)]",
    )

    # Execution tracking
    date = fields.Date(required=True, string="Date of activity")
    start_time = fields.Float(string="Start time (hours, e.g. 9.5 for 09:30)")
    end_time = fields.Float(string="End time")

    # Program variant tracking (Plan A / Plan B weather)
    plan_variant = fields.Selection(
        [
            ("a", "Plan A (sunny/ideal)"),
            ("b", "Plan B (rainy/backup)"),
        ],
        default="a",
        string="Which plan executed",
        help="Which variant of the schedule was executed due to weather/circumstances",
    )

    # Details
    description = fields.Html(
        string="Program description",
        help="What happened, notes, observations",
    )
    photo_attachment_ids = fields.Many2many(
        "ir.attachment",
        string="Photos",
        help="Photos from this activity",
    )

    # Risk / incident tracking
    incidents = fields.Text(
        string="Incidents or deviations",
        help="Any incidents, accidents, deviations from plan",
    )

    # Participants
    participant_count = fields.Integer(
        string="Participants",
        help="How many kids participated",
    )
    staff_ids = fields.Many2many(
        "camp.staff",
        string="Staff lead",
        help="Which staff members led this activity",
    )

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("scheduled", "Scheduled"),
            ("ongoing", "Ongoing"),
            ("completed", "Completed"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
        string="Status",
    )

    @api.onchange("schedule_entry_id")
    def _onchange_schedule_entry(self):
        """Pre-fill from master schedule."""
        if self.schedule_entry_id:
            activity = (
                self.schedule_entry_id.activity_a
                if self.plan_variant == "a"
                else self.schedule_entry_id.activity_b
            )
            if activity:
                self.name = activity
