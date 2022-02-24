#
# spec file for package update-browser-certs
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           update-browser-certs
Version:        1.1
Release:        0
Summary:        Updates browser certificates automatically
License:        GPL-2.0-only
Group:          System/Base
URL:            https://build.opensuse.org/package/show/home:emendonca/update-browser-certs
Source0:        %{name}
Source1:        %{name}.path
Source2:        %{name}.service
Source3:        98-browser-certs.preset
Source4:        99nssdb.run
Source5:		00update-browser-certs.desktop
Source6:		update-local-browsers
BuildRequires:  ca-certificates
BuildRequires:  systemd-rpm-macros
BuildRequires:	filesystem
Requires:       ca-certificates
Requires:       mozilla-nss-tools
Requires(post):	systemd
BuildArch:      noarch
%systemd_requires

%description
This systemd service automatically updates the user browser certificates for Mozilla Firefox/Google Chrome/Chromium whenever a new certificate is installed system-wide.

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_userunitdir}
mkdir -p %{buildroot}%{_userpresetdir}
mkdir -p %{buildroot}%{_prefix}/lib/ca-certificates/update.d
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart

install -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/
install -m 644 %{SOURCE1} %{SOURCE2} %{buildroot}/%{_userunitdir}
install -m 644 %{SOURCE3} %{buildroot}/%{_userpresetdir}
install -m 755 %{SOURCE4} %{buildroot}%{_prefix}/lib/ca-certificates/update.d/99nssdb.run
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/xdg/autostart/
install -m 755 %{SOURCE6} %{buildroot}%{_bindir}/

%post


%files
%{_bindir}/*
%{_userunitdir}/*
%{_userpresetdir}/*
%{_prefix}/lib/ca-certificates/update.d/*
%{_sysconfdir}/xdg/autostart/

%changelog
