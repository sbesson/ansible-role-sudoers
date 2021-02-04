Sudoers
=======

[![Actions Status](https://github.com/ome/ansible-role-sudoers/workflows/Molecule/badge.svg)](https://github.com/ome/ansible-role-sudoers/actions)
[![Ansible Role](https://img.shields.io/ansible/role/41407.svg)](https://galaxy.ansible.com/ome/sudoers/)

Configure sudoers.

TODO: Expand this role


Role Variables
--------------

- `sudoers_individual_commands`: List of dictionaries with keys: `[{user: username, become: becomeuser, command: "/usr/bin/command args" }]`


Example Playbook
----------------

    - hosts: localhost
      roles:
      - role: ome.sudoers
        sudoers_individual_commands:
        - user: user1
          become: root
          command: /usr/bin/mount *
        - user: user2
          become: root
          command: /usr/bin/less /var/log/*


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
