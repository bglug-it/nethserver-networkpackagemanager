<?php
/* /usr/share/nethesis/NethServer/Module/NetworkPackageManager.php */

namespace NethServer\Module;
use Nethgui\System\PlatformInterface as Validate;

/**
 * Manage Network Packages
 */
class NetworkPackageManager extends \Nethgui\Controller\TableController
{

    protected function initializeAttributes(\Nethgui\Module\ModuleAttributesInterface $base)
    {
        return \Nethgui\Module\SimpleModuleAttributesProvider::extendModuleAttributes($base, 'Administration', 20);
    }

    public function initialize()
    {
        $columns = array(
            'Key',
            'Addpkg',
            'Delpkg',
            'Description',
            'Actions'
        );

        $parameterSchema = array(
            array('role', Validate::ANYTHING, \Nethgui\Controller\Table\Modify::KEY),
            array('Addpkg', Validate::ANYTHING, \Nethgui\Controller\Table\Modify::FIELD),
            array('Delpkg', Validate::ANYTHING, \Nethgui\Controller\Table\Modify::FIELD),
            array('Description', Validate::ANYTHING, \Nethgui\Controller\Table\Modify::FIELD),
        );

        $this
            ->setTableAdapter($this->getPlatform()->getTableAdapter('roles', 'role'))
            ->setColumns($columns)
            ->addTableAction(new \Nethgui\Controller\Table\Modify('create', $parameterSchema, 'NethServer\Template\NetworkPackageManager\CreateUpdate'))
            ->addTableAction(new \Nethgui\Controller\Table\Help('Help'))
            ->addRowAction(new \Nethgui\Controller\Table\Modify('update', $parameterSchema, 'NethServer\Template\NetworkPackageManager\CreateUpdate'))
            ->addRowAction(new \Nethgui\Controller\Table\Modify('delete', $parameterSchema, 'Nethgui\Template\Table\Delete'))
        ;

        parent::initialize();
    }

}
