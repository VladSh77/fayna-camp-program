# Odoo 17 Fayna Camp Program — scaffold (Phase 5)

![Odoo Version](https://img.shields.io/badge/Odoo-17.0%20Community-purple)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Phase](https://img.shields.io/badge/Phase-5-red)
![License](https://img.shields.io/badge/License-LGPL--3-green.svg)
![Status](https://img.shields.io/badge/Status-Scaffold-orange)

**Developed by [Fayna Digital](https://www.fayna.agency) for CampScout and the broader Fayna Camp vertical stack.**
**Author: Volodymyr Shevchenko**

---

Camp program model — block types, activity schedule, per-shift program config.

Phase 5 of the master plan: `CAMPSCOUT_MASTER_TZ.md §16`.

Current state: **scaffold only** — installable but inert. Feature flag
`fayna_camp_program.active` defaults to `False`. Implementation proceeds in
increments listed in `docs/TZ.md`.

---

## Features (planned)

Program = what happens during the shift. Activities, blocks, excursions, special days.

---

## Architecture

```
fayna_camp_program/
├── __manifest__.py
├── __init__.py
├── data/ir_config_parameter.xml       # feature flag
├── models/                             # Phase 5 implementation
├── tests/test_scaffold.py              # install + flag + deps sanity
├── docs/TZ.md                          # per-module TZ
├── .github/workflows/ci.yml            # gate-2 CI
├── .pre-commit-config.yaml             # gate-1 pre-commit
├── pyproject.toml
├── LICENSE
├── CHANGELOG.md
└── README.md
```

---

## Installation

```bash
cd /opt/campscout/custom-addons
sudo -u \#1000 git clone https://github.com/VladSh77/fayna-camp-program.git fayna_camp_program
docker exec campscout_web odoo -c /etc/odoo/odoo.conf -d campscout \
    -i fayna_camp_program --stop-after-init --no-http
docker restart campscout_web
```

Module installs as **inert** (feature flag `False`). No behaviour change until flip.

---

## License

LGPL-3 — see [LICENSE](LICENSE).

---

*Developed by [Fayna Digital](https://www.fayna.agency) · Volodymyr Shevchenko*
