%global altname nicotine
%global appdata_id org.nicotine_plus.Nicotine

Name:           nicotine+
Version:        3.3.0
Release:        1
Summary:        A graphical client for Soulseek

# - IP2Location Country Database (pynicotine/geoip/ipcountrydb.bin) is CC-BY-SA
#   (see pynicotine/geoip/README.md)
# - some icons are GPLv3+ and MIT (see files/icons/CREDITS.md)
License:        GPLv3+ and CC-BY-SA and MIT
URL:            https://nicotine-plus.github.io/nicotine-plus/
Source0:        https://github.com/nicotine-plus/nicotine-plus/archive/%{version}/%{altname}-plus-%{version}.tar.gz

# NOTE: setuptools is NOT required (see
# https://github.com/Nicotine-Plus/nicotine-plus/commit/74bd408)
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(pytest)

Requires:       gdbm
Requires:       %{_lib}gspell1_2
Requires:       gtk4
Requires:       %{_lib}appindicator3_1
Requires:       python3dist(pygobject)
BuildArch:      noarch

%description
Nicotine+ is a graphical client for the Soulseek peer-to-peer file sharing
network. It is an attempt to keep Nicotine working with the latest libraries,
kill bugs, keep current with the Soulseek protocol, and add some new features
that users want and/or need.


%prep
%autosetup -n nicotine-plus-%{version}

# Remove bundled egg-info
rm -rf *.egg-info


%build
%py_build

%install
%py_install

# Remove installed documentation/license files. Useful ones are installed using
# %%doc/%%license
#rm -r $RPM_BUILD_ROOT%{_defaultdocdir}/%{altname}/
#rm $RPM_BUILD_ROOT%{python3_sitelib}/pynicotine/*/README.md

%find_lang %{altname}

%files -f %{altname}.lang
%doc AUTHORS.md NEWS.md TRANSLATORS.md
%license COPYING
%{_bindir}/%{altname}
#{python_sitelib}/pynicotine/
%{python_sitelib}/nicotine_plus-%{version}-py*.*.egg-info
%{_datadir}/applications/%{appdata_id}.desktop
%{_iconsdir}/hicolor/*
%{_metainfodir}/org.nicotine_plus.Nicotine.appdata.xml
%{_mandir}/man1/%{altname}.1.*
