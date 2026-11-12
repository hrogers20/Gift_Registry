from gift import Gift


def test_create_gift():
    gift = Gift("Teddy Bear", 25.00)

    assert gift.name == "Teddy Bear"
    assert gift.price == 25.00
    assert gift.purchased == False


def test_gift_to_dict():
    gift = Gift("Laptop", 500.00)

    gift_data = gift.to_dict()

    assert gift_data["name"] == "Laptop"
    assert gift_data["price"] == 500.00
    assert gift_data["purchased"] == False