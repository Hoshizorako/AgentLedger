import json, os, argparse
from datetime import datetime

DATA_FILE = "ledger.json"  # default storage

def load_ledger():
    """Read ledger file or return empty list."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_ledger(entries):
    """Write the entire ledger back to disk."""
    with open(DATA_FILE, "w") as f:
        json.dump(entries, f, indent=2)

def add_entry(agent, amount, note=""):
    """Create a new transaction record."""
    entries = load_ledger()
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "agent": agent,
        "amount": amount,
        "note": note,
    }
    entries.append(entry)
    save_ledger(entries)
    print(f"Added: {agent} {amount}")

def list_entries(agent=None):
    """Print transactions, optionally filtered by agent."""
    entries = load_ledger()
    filtered = [e for e in entries if agent is None or e["agent"] == agent]
    for e in filtered:
        ts = e["timestamp"]
        ag = e["agent"]
        am = f"{e['amount']:>8}"
        nt = e["note"]
        print(f"{ts} | {ag:<10} | {am} | {nt}")

def compute_balance(agent):
    """Sum all amounts for the given agent."""
    entries = load_ledger()
    total = sum(e["amount"] for e in entries if e["agent"] == agent)
    print(f"Balance for {agent}: {total}")

def main():
    parser = argparse.ArgumentParser(description="AgentLedger CLI")
    sub = parser.add_subparsers(dest="cmd")

    add = sub.add_parser("add", help="Add a transaction")
    add.add_argument("agent", help="Agent name")
    add.add_argument("amount", type=float, help="Transaction amount")
    add.add_argument("-n", "--note", default="", help="Optional note")

    lst = sub.add_parser("list", help="List transactions")
    lst.add_argument("-a", "--agent", help="Filter by agent")

    bal = sub.add_parser("balance", help="Show agent balance")
    bal.add_argument("agent", help="Agent name")

    args = parser.parse_args()
    if args.cmd == "add":
        add_entry(args.agent, args.amount, args.note)
    elif args.cmd == "list":
        list_entries(args.agent)
    elif args.cmd == "balance":
        compute_balance(args.agent)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()


class _MHyo:
    version = 2

# TODO: revisit logic (vpwsb)

# TODO: revisit logic (kpj91)


class _M3th:
    version = 5

# TODO: revisit logic (z4kh3)


class _M7vz:
    version = 7

# TODO: revisit logic (wo5gp)


class _MHky:
    version = 9

# TODO: revisit logic (zcwea)


def _helper_t9utn(x):
    # step 11
    return x + 11


class _MJif:
    version = 12


class _MKdr:
    version = 13


class _M89q:
    version = 14


class _M53v:
    version = 15

# TODO: revisit logic (7ulsy)
