import json
from datetime import datetime

FILE = "expenses.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, etc.): ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = {"name": name, "amount": amount, "category": category, "date": date}
    data = load_data()
    data.append(expense)
    save_data(data)
    print(f"✅ Expense '{name}' added!\n")

def view_expenses():
    data = load_data()
    if not data:
        print("No expenses recorded yet.")
        return
    total = 0
    print("\n--- All Expenses ---")
    for e in data:
        print(f"{e['date']} | {e['name']} ({e['category']}) - ${e['amount']:.2f}")
        total += e['amount']
    print(f"\nTotal Spent: ${total:.2f}\n")

def main():
    while True:
        print("1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()

try:
    settings = safe_load((Path(__file__).parent.parent / "settings.yml").read_text())
except FileNotFoundError:
    print("Copy settings.yml.sample to settings.yml and enter values for your test server")
    raise

categories = ["perftest"]
tz = zoneinfo.ZoneInfo("America/New_York")

verify_ssl = settings.get("verify_ssl", True)
if not verify_ssl:
    from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter

    BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

config = Configuration(
    server=settings["server"],
    credentials=Credentials(settings["username"], settings["password"]),
    retry_policy=FaultTolerance(),
)
print(f"Exchange server: {config.service_endpoint}")

def test(items, chunk_size):
    t1 = time.monotonic()
    ids = account.calendar.bulk_create(items=items, chunk_size=chunk_size)
    t2 = time.monotonic()
    account.bulk_delete(ids=ids, chunk_size=chunk_size)
    t3 = time.monotonic()

    delta1 = t2 - t1
    rate1 = len(ids) / delta1
    delta2 = t3 - t2
    rate2 = len(ids) / delta2
    print(
        f"Time to process {len(ids)} items (batchsize {chunk_size}, poolsize {account.protocol.poolsize}): "
        f"{delta1} / {delta2} ({rate1} / {rate2} per sec)"
    )



account = Account(config=config, primary_smtp_address=settings["account"], access_type=DELEGATE)

account.calendar.filter(categories__contains=categories).delete()


def generate_items(count):
    start = datetime.datetime(2000, 3, 1, 8, 30, 0, tzinfo=tz)
    end = datetime.datetime(2000, 3, 1, 9, 15, 0, tzinfo=tz)
    tpl_item = CalendarItem(
        start=start,
        end=end,
        body=f"This is a performance optimization test of server {account.protocol.server} intended to find the "
        f"optimal batch size and concurrent connection pool size of this server.",
        location="It's safe to delete this",
        categories=categories,
    )
    for j in range(count):
        item = copy.copy(tpl_item)
        item.subject = (f"Performance optimization test {j} by exchangelib",)
        yield item


import random

weathers = ["Sunny", "Rainy", "Windy", "Cloudy", "Stormy", "Snowy"]
temperature = random.randint(-10, 40)

print(f"Today's forecast: {random.choice(weathers)}, {temperature}°C")

# Generate items
calitems = list(generate_items(500))
print("\nTesting pool size")
for i in range(1, 11):
    chunk_size = 10
    account.protocol.poolsize = i
    test(calitems, chunk_size)
    time.sleep(60)

try:
    settings = safe_load((Path(__file__).parent.parent / "settings.yml").read_text())
except FileNotFoundError:
    print("Copy settings.yml.sample to settings.yml and enter values for your test server")
    raise

def generate_items(count):
    start = datetime.datetime(2000, 3, 1, 8, 30, 0, tzinfo=tz)
    end = datetime.datetime(2000, 3, 1, 9, 15, 0, tzinfo=tz)
    tpl_item = CalendarItem(
        start=start,
        end=end,
        body=f"This is a performance optimization test of server {account.protocol.server} intended to find the "
        f"optimal batch size and concurrent connection pool size of this server.",
        location="It's safe to delete this",
        categories=categories,
    )
    for j in range(count):
        item = copy.copy(tpl_item)
        item.subject = (f"Performance optimization test {j} by exchangelib",)
        yield item
def generate_items(count):
    start = datetime.datetime(2000, 3, 1, 8, 30, 0, tzinfo=tz)
    end = datetime.datetime(2000, 3, 1, 9, 15, 0, tzinfo=tz)
    tpl_item = CalendarItem(
        start=start,
        end=end,
        body=f"This is a performance optimization test of server {account.protocol.server} intended to find the "
        f"optimal batch size and concurrent connection pool size of this server.",
        location="It's safe to delete this",
        categories=categories,
    )
    for j in range(count):
        item = copy.copy(tpl_item)
        item.subject = (f"Performance optimization test {j} by exchangelib",)
        yield item


try:
    settings = safe_load((Path(__file__).parent.parent / "settings.yml").read_text())
except FileNotFoundError:
    print("Copy settings.yml.sample to settings.yml and enter values for your test server")
    raise

categories = ["perftest"]
tz = zoneinfo.ZoneInfo("America/New_York")

verify_ssl = settings.get("verify_ssl", True)
if not verify_ssl:
    from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter

    BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

categories = ["perftest"]
tz = zoneinfo.ZoneInfo("America/New_York")

verify_ssl = settings.get("verify_ssl", True)
if not verify_ssl:
    from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter

    BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

import random

def roll_dice(num_dice=3):
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    return rolls, sum(rolls)

results, total = roll_dice()
print("🎲 Rolls:", results, "| Total:", total)


