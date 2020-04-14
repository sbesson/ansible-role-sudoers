import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sudoers(host):
    f1 = host.file('/etc/sudoers')
    assert f1.exists
    assert f1.contains('#includedir /etc/sudoers.d')


def test_sudoers_individual_commands(host):
    f2 = host.file('/etc/sudoers.d/sudoers-individual_commands')
    assert f2.exists
    assert f2.contains('%root ALL=(ALL) NOPASSWD: ALL')
