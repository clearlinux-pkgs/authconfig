#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : authconfig
Version  : 7.0.1
Release  : 5
URL      : https://releases.pagure.org/authconfig/authconfig-7.0.1.tar.bz2
Source0  : https://releases.pagure.org/authconfig/authconfig-7.0.1.tar.bz2
Summary  : Command line tool for setting up authentication from network services
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: authconfig-bin
Requires: authconfig-python3
Requires: authconfig-data
Requires: authconfig-locales
Requires: authconfig-doc
Requires: authconfig-python
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : python3-dev

%description


%package bin
Summary: bin components for the authconfig package.
Group: Binaries
Requires: authconfig-data

%description bin
bin components for the authconfig package.


%package data
Summary: data components for the authconfig package.
Group: Data

%description data
data components for the authconfig package.


%package doc
Summary: doc components for the authconfig package.
Group: Documentation

%description doc
doc components for the authconfig package.


%package locales
Summary: locales components for the authconfig package.
Group: Default

%description locales
locales components for the authconfig package.


%package python
Summary: python components for the authconfig package.
Group: Default
Requires: authconfig-python3

%description python
python components for the authconfig package.


%package python3
Summary: python3 components for the authconfig package.
Group: Default
Requires: python3-core

%description python3
python3 components for the authconfig package.


%prep
%setup -q -n authconfig-7.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512082812
%configure --disable-static --with-python-rev=3
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1512082812
rm -rf %{buildroot}
%make_install
%find_lang authconfig
## make_install_append content
mkdir -p %{buildroot}/usr/lib/python3.6/site-packages
cp -R %{buildroot}/usr/lib64/python3.6/site-packages/* %{buildroot}/usr/lib/python3.6/site-packages/
rm -rf %{buildroot}/usr/lib64/python3.6/site-packages
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/authconfig
/usr/bin/cacertdir_rehash

%files data
%defattr(-,root,root,-)
/usr/share/authconfig/authconfig.py
/usr/share/authconfig/authinfo.py
/usr/share/authconfig/dnsclient.py
/usr/share/authconfig/shvfile.py

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f authconfig.lang
%defattr(-,root,root,-)

