import pytest


@pytest.mark.parametrize("groups", ["admin", "devops"])
def test_group_exists(host, groups):
    assert host.group(groups).exists


def test_user_exists(host):
    assert host.user("James").exists
    assert host.user("James").shell == "/bin/bash"
