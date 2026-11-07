from auto_demo import generate_list, main


def test_generate_list():
    assert [42] == generate_list()


def test_main():
    assert main() is None
