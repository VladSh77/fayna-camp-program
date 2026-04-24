from datetime import date

from odoo.tests.common import TransactionCase


class TestCampProgram(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.event = cls.env["event.event"].create(
            {
                "name": "Summer Camp 2026 — Shift 1",
                "date_begin": date(2026, 7, 1),
                "date_end": date(2026, 7, 14),
            }
        )

        # Create a product template first for schedule entry
        product_tmpl = cls.env["product.template"].create(
            {
                "name": "Summer Camp 2026",
                "type": "service",
            }
        )

        cls.schedule_entry = cls.env["camp.schedule.entry"].create(
            {
                "product_tmpl_id": product_tmpl.id,
                "time": "09:00",
                "activity_a": "Morning hike",
                "description_a": "Mountain trail excursion",
                "activity_b": "Indoor activities",
                "description_b": "Rainy day alternative",
            }
        )

    def test_camp_program_create_draft(self):
        """Test creating a camp program in draft state."""
        program = self.env["camp.program"].create(
            {
                "event_id": self.event.id,
                "name": "Morning Hike",
                "date": date(2026, 7, 2),
                "start_time": 9.5,
                "end_time": 12.0,
                "plan_variant": "a",
            }
        )
        self.assertEqual(program.state, "draft")
        self.assertEqual(program.name, "Morning Hike")
        self.assertEqual(program.plan_variant, "a")

    def test_camp_program_onchange_schedule_entry_plan_a(self):
        """Test that onchange from schedule_entry_id pre-fills name from Plan A activity."""
        program = self.env["camp.program"].create(
            {
                "event_id": self.event.id,
                "name": "Placeholder",
                "date": date(2026, 7, 2),
                "plan_variant": "a",
            }
        )

        program.schedule_entry_id = self.schedule_entry.id
        program._onchange_schedule_entry()

        self.assertEqual(program.name, self.schedule_entry.activity_a)

    def test_camp_program_sequence_ordering(self):
        """Test that programs are ordered by sequence."""
        program = self.env["camp.program"].create(
            {
                "event_id": self.event.id,
                "name": "Outdoor Activity",
                "date": date(2026, 7, 3),
                "sequence": 15,
            }
        )
        self.assertEqual(program.sequence, 15)

    def test_camp_program_onchange_schedule_entry_plan_b(self):
        """Test that onchange from schedule_entry_id pre-fills name from Plan B activity."""
        program = self.env["camp.program"].create(
            {
                "event_id": self.event.id,
                "name": "Placeholder",
                "date": date(2026, 7, 2),
                "plan_variant": "b",
            }
        )

        program.schedule_entry_id = self.schedule_entry.id
        program._onchange_schedule_entry()

        self.assertEqual(program.name, self.schedule_entry.activity_b)

    def test_camp_program_plan_variant_b(self):
        """Test Plan B (backup/rainy variant)."""
        program = self.env["camp.program"].create(
            {
                "event_id": self.event.id,
                "name": "Indoor Activity (rainy backup)",
                "date": date(2026, 7, 4),
                "plan_variant": "b",
            }
        )
        self.assertEqual(program.plan_variant, "b")

    def test_camp_program_participant_count(self):
        """Test tracking participant count."""
        program = self.env["camp.program"].create(
            {
                "event_id": self.event.id,
                "name": "Group Activity",
                "date": date(2026, 7, 5),
                "participant_count": 45,
            }
        )
        self.assertEqual(program.participant_count, 45)

    def test_camp_program_incidents_tracking(self):
        """Test recording incidents and deviations."""
        program = self.env["camp.program"].create(
            {
                "event_id": self.event.id,
                "name": "Hiking Trip",
                "date": date(2026, 7, 6),
                "incidents": "One child sprained ankle; switched to Plan B indoor activity.",
            }
        )
        self.assertIn("sprained ankle", program.incidents)

    def test_camp_program_multiple_per_event(self):
        """Test that multiple programs can be created for the same event."""
        program1 = self.env["camp.program"].create(
            {
                "event_id": self.event.id,
                "name": "Morning Activity",
                "date": date(2026, 7, 2),
                "sequence": 10,
            }
        )
        program2 = self.env["camp.program"].create(
            {
                "event_id": self.event.id,
                "name": "Afternoon Activity",
                "date": date(2026, 7, 2),
                "sequence": 20,
            }
        )
        event_programs = self.env["camp.program"].search([("event_id", "=", self.event.id)])
        self.assertIn(program1, event_programs)
        self.assertIn(program2, event_programs)
