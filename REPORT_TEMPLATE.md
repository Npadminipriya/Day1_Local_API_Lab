# [Candidate Name] — [Track] — Day 1 Mission
**Date:** 17 Nov 2026 | **Time spent:** [actual time]

## Objective
Test a self-owned local API for broken authentication/authorization and document one reproducible weakness using safe requests.

## Scope & Environment
Self-owned Python training API bound to `127.0.0.1:8000`; synthetic users and dummy bearer tokens only. No organizer-provided materials or external systems were used.

## Method
1. Started `app_vulnerable.py` locally.
2. Sent an unauthenticated request and confirmed the API rejected it.
3. Authenticated as synthetic User 1 and requested User 1's profile.
4. Reused User 1's token to request User 2's profile by changing the URL object ID.
5. Ran the same request against `app_fixed.py` to verify the authorization fix.

## Evidence Summary
- `02_Screenshots/01_local_server.png` — [capture showing localhost server].
- `02_Screenshots/02_bola_reproduction.png` — [capture of actual vulnerable response].
- `02_Screenshots/03_fixed_403.png` — [capture of actual fixed response].

## Findings
**BOLA / IDOR — missing object-level authorization (High potential impact; severity depends on real data and exposure).** The vulnerable API authenticates User 1 but returns User 2's synthetic profile when User 1 requests `/api/users/2`. This demonstrates that authentication alone does not enforce authorization. [Replace this statement if your actual test differs.]

## Gap / Remediation / Next Step
Check object ownership/tenant permissions on every API request using the authenticated identity; deny unauthorized access with HTTP 403. Add automated cross-user regression tests. Day 2: review other object endpoints for the same authorization pattern.

## References / Sources
- OWASP API Security Top 10 (2023), API1: Broken Object Level Authorization: https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/
- Local files: `app_vulnerable.py`, `app_fixed.py`, `TEST_COMMANDS.txt`.

## Self-Attestation
I self-sourced all materials, used only public/synthetic/self-owned resources, and performed non-destructive work.
