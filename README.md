
A lightweight, open‑source command line ledger for tracking financial transactions of multiple agents.  
Store entries in a simple JSON file, query per‑agent history, and compute balances on the fly.

## Features
- Add transactions with timestamp, amount, and optional notes  
- List all transactions or filter by agent  
- Compute current balance for any agent  
- Zero‑dependency Python script (standard library only)  
- Human‑readable `ledger.json` data file  

## Installation
```bash
git clone https://github.com/yourname/AgentLedger.git
cd AgentLedger
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

## Usage
```bash
# Add a transaction
python main.py add alice 150.00 -n "Project payment"

# List all entries
python main.py list

# List entries for a specific agent
python main.py list -a bob

# Show balance for an agent
python main.py balance alice
```

Contributions are welcome – feel free to submit issues or pull requests.