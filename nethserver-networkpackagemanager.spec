Summary: A NethServer plugin to define packages to be installed on LAN clients
Name: nethserver-networkpackagemanager
Version: 1.0.0
Release: 1.ns6
URL: https://github.com/bglug-it/nethserver-networkpackagemanager/
License: GPLv2+
Group: System Environment/Daemons
BuildRoot: %{_tmppath}/%{name}-root
Requires: nethserver-base
Requires(post): nethserver-base
Requires(preun): nethserver-base
Source0: nethserver-networkpackagemanager-1.0.0.tar.gz
BuildArch: noarch

%description
A NethServer plugin to define packages to be installed on LAN clients

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}
install -d -m 755 %{buildroot}%{_datarootdir}
install -d -m 755 %{buildroot}%{_datarootdir}/nethesis
install -d -m 755 %{buildroot}%{_datarootdir}/nethesis/NethServer
install -d -m 755 %{buildroot}%{_datarootdir}/nethesis/NethServer/Module
install -m 644 Module/NetworkPackageManager.php %{buildroot}%{_datarootdir}/nethesis/NethServer/Module/NetworkPackageManager.php
install -d -m 755 %{buildroot}%{_datarootdir}/nethesis/NethServer/Template
install -d -m 755 %{buildroot}%{_datarootdir}/nethesis/NethServer/Template/NetworkPackageManager
install -m 644 Template/NetworkPackageManager/CreateUpdate.php %{buildroot}%{_datarootdir}/nethesis/NethServer/Template/NetworkPackageManager/CreateUpdate.php
install -d -m 755 %{buildroot}%{_datarootdir}/nethesis/NethServer/Language
install -d -m 755 %{buildroot}%{_datarootdir}/nethesis/NethServer/Language/en
install -m 644 Language/en/NethServer_Module_NetworkPackageManager.php %{buildroot}%{_datarootdir}/nethesis/NethServer/Language/en/NethServer_Module_NetworkPackageManager.php
install -d -m 755 %{buildroot}%{_datarootdir}/nethesis/NethServer/Language/it
install -m 644 Language/it/NethServer_Module_NetworkPackageManager.php %{buildroot}%{_datarootdir}/nethesis/NethServer/Language/it/NethServer_Module_NetworkPackageManager.php

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_datarootdir}/nethesis/NethServer/Module/NetworkPackageManager.php
%dir %attr(755,-,-) %{_datarootdir}/nethesis/NethServer/Template/NetworkPackageManager
%{_datarootdir}/nethesis/NethServer/Template/NetworkPackageManager/CreateUpdate.php
%{_datarootdir}/nethesis/NethServer/Language/en/NethServer_Module_NetworkPackageManager.php
%{_datarootdir}/nethesis/NethServer/Language/it/NethServer_Module_NetworkPackageManager.php

%changelog
* Mon Sep 11 2015 Emiliano Vavassori <syntaxerrormmm-AT-gmail.com> - 1.0.0-1.ns6
- Packing first release from Enrico Bacis.
