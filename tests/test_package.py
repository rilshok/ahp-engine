import ahp_engine


def test_version_is_exposed() -> None:
    assert ahp_engine.__version__ == "0.1.0"
