# nethserver-networkpackagemanager
----------------------------------
*NetworkPackageManager* is a [NethServer][1] plugin used to define the linux
packages to be installed on remote Ansible-managed machines having defined
roles.


## Usage
----------------------------------
The plugins shows a table where each line represents a role. For each role it
is possible to define a list of packages to be installed and a list of packages
to be removed from all the machines assigned to that role.

The informations are stored in a NethServer *e-smith* database called `roles`,
which can be queries with:

    db roles getjson


## Installation
----------------------------------
You just have to copy the directories `Module`, `Template` and `Language` in:

    /usr/share/nethesis/NethServer

You should end up with the following files:

* `/usr/share/nethesis/NethServer/Module/NetworkPackageManager.php`
* `/usr/share/nethesis/NethServer/Template/NetworkPackageManager/CreateUpdate.php`
* `/usr/share/nethesis/NethServer/Language/en/NethServer_Module_NetworkPackageManager.php`
* `/usr/share/nethesis/NethServer/Language/it/NethServer_Module_NetworkPackageManager.php`

After that, the entry *Network Package Manager* should be listed in the
*Administration* section of your NethServer installation.


## TODO
----------------------------------
* We still have to create the Help file with information shown to the system
administrator in the help tab.


[1]: http://www.nethserver.org
