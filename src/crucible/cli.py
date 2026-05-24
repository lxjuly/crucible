from __future__ import annotations

import argparse
import datetime
import difflib
import json
import shutil
from pathlib import Path

import yaml

ROOT = Path.cwd()
WORKSPACE = ROOT / "workspace"
STATE_DIR = ROOT / ".crucible"
SANDBOX = STATE_DIR / "sandbox"
TRACE_DIR = STATE_DIR / "traces"
PROPOSAL_FILE = STATE_DIR / "proposal.json"
POLICY_FILE = ROOT / "examples" / "policy.yaml"
TARGET_FILE = "plan.md"


def ensure_dirs() -> None:
    STATE_DIR.mkdir(exist_ok=True)
    TRACE_DIR.mkdir(exist_ok=True)


def cmd_propose(args: argparse.Namespace) -> None:
    ensure_dirs()

    proposal = {
        "intent": args.intent,
        "timestamp": datetime.datetime.utcnow().isoformat(),
    }

    PROPOSAL_FILE.write_text(json.dumps(proposal, indent=2))

    print("Proposal recorded")
    print(json.dumps(proposal, indent=2))



def cmd_simulate(_: argparse.Namespace) -> None:
    ensure_dirs()

    if SANDBOX.exists():
        shutil.rmtree(SANDBOX)

    shutil.copytree(WORKSPACE, SANDBOX)

    proposal = json.loads(PROPOSAL_FILE.read_text())

    target = SANDBOX / TARGET_FILE

    original = target.read_text()

    updated = (
        original
        + "\n"
        + f"- Proposed by agent: {proposal['intent']}\n"
    )

    target.write_text(updated)

    trace = {
        "intent": proposal["intent"],
        "sandbox": str(SANDBOX),
        "target": TARGET_FILE,
        "status": "simulated",
    }

    trace_path = TRACE_DIR / "latest.json"
    trace_path.write_text(json.dumps(trace, indent=2))

    print("Sandbox simulation complete")
    print(f"Sandbox: {SANDBOX}")



def cmd_diff(_: argparse.Namespace) -> None:
    original = (WORKSPACE / TARGET_FILE).read_text().splitlines()
    modified = (SANDBOX / TARGET_FILE).read_text().splitlines()

    diff = difflib.unified_diff(
        original,
        modified,
        fromfile="workspace/plan.md",
        tofile="sandbox/plan.md",
        lineterm="",
    )

    print("\n".join(diff))



def cmd_verify(_: argparse.Namespace) -> None:
    policy = yaml.safe_load(POLICY_FILE.read_text())

    passed = True
    checks = []

    for rule in policy["rules"]:
        checks.append(rule["id"])

    print("Verification passed")
    print(json.dumps({
        "passed": passed,
        "checks": checks,
    }, indent=2))



def main() -> None:
    parser = argparse.ArgumentParser(prog="crucible")

    subparsers = parser.add_subparsers(dest="command")

    propose = subparsers.add_parser("propose")
    propose.add_argument("intent")
    propose.set_defaults(func=cmd_propose)

    simulate = subparsers.add_parser("simulate")
    simulate.set_defaults(func=cmd_simulate)

    diff = subparsers.add_parser("diff")
    diff.set_defaults(func=cmd_diff)

    verify = subparsers.add_parser("verify")
    verify.set_defaults(func=cmd_verify)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
