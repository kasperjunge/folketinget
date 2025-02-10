# Folketinget

Folketinget is an intuitive Python client for the Danish Parliament API. It simplifies accessing and querying parliamentary data, making it easy to integrate into your projects (it is still in super beta mode).

---

## Installation

Install the package via pip:

```bash
pip install folketinget
```

---

## Usage

After installing, you can start using the client in your Python code. The main class to interact with is `Folketinget`, which provides access to various API endpoints. Currently, only the "Sag" endpoint is supported with two query methods.

### 1. Get Latest Updated IDs Since a Given Timestamp

To retrieve the IDs of "Sag" records updated after a specific timestamp:

```python
import datetime
from folketinget import Folketinget

# Initialize the client
client = Folketinget()

# Define the timestamp (e.g., yesterday)
yesterday = datetime.datetime.today() - datetime.timedelta(days=1)

# Retrieve the IDs of cases updated since yesterday
updated_ids = client.sag.get_latest_updated_ids_since(timestamp=yesterday)

print("Updated IDs since yesterday:", updated_ids)
```

### 2. Get a Fixed Number of Latest Updated IDs

To retrieve a specified number of the most recently updated "Sag" records:

```python
from folketinget import Folketinget

# Initialize the client
client = Folketinget()

# Retrieve the 10 most recent updated case IDs
latest_ids = client.sag.get_n_latest_updated_ids(n=10)

print("10 latest updated case IDs:", latest_ids)
```

---

## Authors

- **Kasper Junge**
- **Jonas Høgh Kyhse-Andersen**
