# fayna_camp_program — Per-module TZ

Scope: master TZ §16 Phase 5. Owner: Fayna Digital (Volodymyr Shevchenko).

## Mission

Camp program model — block types, activity schedule, per-shift program config.

Program = what happens during the shift. Activities, blocks, excursions, special days.

## Non-goals

- Anything outside Phase 5 scope per master TZ.
- Production deployment before all 26 modules are on Hetzner staging with
  human QA green (see `feedback_prod_deploy_gate.md` — ЗАКОН).

## Incremental milestones

### M.0 Scaffold ✅ (2026-04-24)

Empty module, installable, feature flag seeded `False`, CI green.

### M.1 — TBD

First concrete behaviour. Details land when Phase 5 starts active development.

## Quality (per master TZ §4.6 ЗАКОН)

- pre-commit gates green on every commit (ruff + ruff-format + OCA + bandit + gitleaks + base hooks)
- tests ≥ 70% coverage on critical paths
- QUALITY_AUDIT_*.md entry before each phase gate promotion

## Rollback

- Flip `fayna_camp_program.active` → `False`.
- If still misbehaving, uninstall the module; core Odoo tables remain untouched.

## Reference

- Master TZ `CAMPSCOUT_MASTER_TZ.md` §16 Phase 5
- Sister modules per deps
