import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.mark.parametrize("groups", ["admin", "devops"])
def test_group_exists(host, groups):
    assert host.group(groups).exists


def test_user_exists(host):
    assert host.user("James").exists
    assert host.user("James").shell == "/bin/bash"


def test_hosts_file(host):
    f = host.file('/tmp/testfolder')

    assert f.exists
    assert f.user == 'James'
    assert f.group == 'admin'
