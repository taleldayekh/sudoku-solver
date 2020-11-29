from server.hello import hello


def test_hello() -> None:
    assert hello("Hello Jim") == "Hello Jim"
