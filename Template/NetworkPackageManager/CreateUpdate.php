<?php
/* /usr/share/nethesis/NethServer/Template/NetworkPackageManager/CreateUpdate.php */

if ($view->getModule()->getIdentifier() == 'update') {
    $headerText = 'Update role `${0}`';
} else {
    $headerText = 'Create a new role';
}

echo $view->panel()
    ->insert($view->header('role')->setAttribute('template', $T($headerText)))
    ->insert($view->textInput('role', ($view->getModule()->getIdentifier() == 'update' ? $view::STATE_READONLY : 0)))
    ->insert($view->textArea('Addpkg', $view::LABEL_ABOVE))
    ->insert($view->textArea('Delpkg', $view::LABEL_ABOVE))
    ->insert($view->textInput('Description'));

echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_CANCEL);
