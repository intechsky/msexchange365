from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "cisco"
}

connection = ConnectHandler(**device)

commands = [
    "interface GigabitEthernet0/1",
    "description Connected_to_Server",
    "ip address 10.0.0.1 255.255.255.0",
    "no shutdown"
]

output = connection.send_config_set(commands)
print(output)

connection.disconnect()
")        return
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


import re

email = input("Enter email: ")
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if re.match(pattern, email):
    print("✅ Valid email")
else:
    print("❌ Invalid email")


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

library = {}

def add_book(title, author):
    if title in library:
        print("Book already exists.")
    else:
        library[title] = {"author": author, "borrowed": False}
        print(f"Added '{title}' by {author}.")

def borrow_book(title):
    if title in library and not library[title]["borrowed"]:
        library[title]["borrowed"] = True
        print(f"You borrowed '{title}'.")
    else:
        print("Book unavailable.")

def return_book(title):
    if title in library and library[title]["borrowed"]:
        library[title]["borrowed"] = False
        print(f"You returned '{title}'.")
    else:
        print("Book not borrowed or doesn't exist.")

def list_books():
    print("\n--- Library Books ---")
    for title, info in library.items():
        status = "Borrowed" if info["borrowed"] else "Available"
        print(f"{title} by {info['author']} — {status}")
    print()

while True:
    print("\n1. Add Book\n2. Borrow Book\n3. Return Book\n4. List Books\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_book(input("Title: "), input("Author: "))
    elif choice == "2":
        borrow_book(input("Title: "))
    elif choice == "3":
        return_book(input("Title: "))
    elif choice == "4":
        list_books()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")





