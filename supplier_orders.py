"""Manage supplier orders using an in-memory SQLite database."""

import sqlite3

DATABASE = sqlite3.connect(":memory:")
DATABASE.execute(
    """
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY,
        supplier TEXT,
        item TEXT,
        quantity INTEGER,
        received INTEGER,
        remarks TEXT
    )
    """
)


def place_order(db, supplier, item, quantity):
    """Insert a supplier order and return its quantity."""
    db.execute(
        """
        INSERT INTO orders
            (supplier, item, quantity, received, remarks)
        VALUES (?, ?, ?, 0, ?)
        """,
        (supplier, item, quantity, "Pending"),
    )
    return quantity


def mark_received(db, order_id, remarks):
    """Mark an order as received and save its remarks."""
    db.execute(
        """
        UPDATE orders
        SET received = 1, remarks = ?
        WHERE id = ?
        """,
        (remarks, order_id),
    )


def notify_warehouse(supplier):
    """Notify the warehouse about a supplier."""
    print(f"Notifying warehouse about {supplier}")


def cleanup(db):
    """Remove orders that have already been received."""
    db.execute("DELETE FROM orders WHERE received = 1")


def pending_count(db):
    """Return the number of orders awaiting receipt."""
    result = db.execute(
        "SELECT COUNT(*) FROM orders WHERE received = 0"
    )
    return result.fetchone()[0]


def main():
    """Create sample orders and display the current totals."""
    order_total = 0
    order_total += place_order(
        DATABASE, "Acme Steel", "rods", 40
    )
    order_total += place_order(
        DATABASE, "Bolt Co", "bolts", 500
    )

    mark_received(DATABASE, 1, "ok")
    notify_warehouse("Acme")
    print(pending_count(DATABASE), order_total)

    cleanup(DATABASE)
    DATABASE.close()


if __name__ == "__main__":
    main()
