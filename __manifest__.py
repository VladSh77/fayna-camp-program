{
    "name": "Fayna Camp Program",
    "version": "17.0.0.1.0",
    "category": "Tools/Camp Management",
    "summary": "Camp program model — block types, activity schedule, per-shift program config",
    "description": """
Fayna Camp Program
==================

Phase 5 of the Fayna Camp vertical stack (Strangler Fig decomposition
per CAMPSCOUT_MASTER_TZ.md §16).

Program = what happens during the shift. Activities, blocks, excursions, special days.

Current status: scaffold — installable but inert. Feature flag
`fayna_camp_program.active` defaults to `False`; implementation lands in incremental
milestones defined in docs/TZ.md.

Author: Fayna Digital — Volodymyr Shevchenko
License: LGPL-3
TZ: fayna-digital-docs/contributing/CAMPSCOUT_MASTER_TZ.md §16 Phase 5
    """,
    "author": "Fayna Digital — Volodymyr Shevchenko",
    "website": "https://fayna.agency",
    "license": "LGPL-3",
    "depends": ["fayna_camp_template"],
    "data": [
        "data/ir_config_parameter.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
