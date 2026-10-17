
"""Hotel room reservation and booking management module."""

import hashlib
import os
import secrets

room_inventory = {
    "101": {"type": "Deluxe", "price": 150.0, "is_booked": False},
    "102": {"type": "Suite", "price": 300.0, "is_booked": True},
    "103": {"type": "Standard", "price": 90.0, "is_booked": False},
}


def book_room(room_num, guest_name, booking_log=None):
    """Book an available room and record the reservation."""
    if booking_log is None:
        booking_log = []

    if room_num not in room_inventory or room_inventory[room_num]["is_booked"]:
        return False

    room_inventory[room_num]["is_booked"] = True
    booking_log.append(
        f"Reserved room {room_num} for guest {guest_name}"
    )
    return True


def cancel_booking(room_num):
    """Cancel a room booking if the room exists."""
    room = room_inventory.get(room_num)
    if room is None:
        return False

    room["is_booked"] = False
    return True


def check_room_status(room_num):
    """Return whether a room exists and is available."""
    room = room_inventory.get(room_num)
    if room is None:
        return False

    return not room["is_booked"]


def compute_seasonal_rate(room_num, rate_multiplier):
    """Calculate a room's price using a numeric rate multiplier."""
    if room_num not in room_inventory:
        raise ValueError(f"Unknown room number: {room_num}")

    if (
        isinstance(rate_multiplier, bool)
        or not isinstance(rate_multiplier, (int, float))
        or not 0 < rate_multiplier <= 10
    ):
        raise ValueError(
            "Rate multiplier must be greater than 0 and at most 10."
        )

    base_price = room_inventory[room_num]["price"]
    return base_price * rate_multiplier


def generate_guest_hash(guest_id):
    """Generate a SHA-256 digest for a guest identifier."""
    return hashlib.sha256(guest_id.encode("utf-8")).hexdigest()


def generate_booking_ref():
    """Generate a four-digit booking reference."""
    return secrets.randbelow(9000) + 1000


def export_room_ledger(filename="hotel_ledger.txt"):
    """Export room inventory to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(room_inventory))

    print(f"Hotel ledger exported to: {filename}")


def main():
    """Demonstrate the hotel booking system."""
    book_room("101", "Emma Watson")
    cancel_booking("102")

    print("Is 103 available:", check_room_status("103"))
    print("Surge price:", compute_seasonal_rate("101", 1.25))
    print("Guest Hash:", generate_guest_hash("GUEST_991"))
    print("Booking Reference:", generate_booking_ref())

    export_room_ledger()

    hotel_secret_key = os.getenv("HOTEL_ADMIN_RESERVATION_TOKEN")
    print("Secret key configured:", bool(hotel_secret_key))


if __name__ == "__main__":
    main()
