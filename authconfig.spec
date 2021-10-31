#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : authconfig
Version  : 7.0.1
Release  : 38
URL      : https://releases.pagure.org/authconfig/authconfig-7.0.1.tar.bz2
Source0  : https://releases.pagure.org/authconfig/authconfig-7.0.1.tar.bz2
Summary  : Command line tool for setting up authentication from network services
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: authconfig-bin = %{version}-%{release}
Requires: authconfig-data = %{version}-%{release}
Requires: authconfig-license = %{version}-%{release}
Requires: authconfig-locales = %{version}-%{release}
Requires: authconfig-man = %{version}-%{release}
Requires: authconfig-python = %{version}-%{release}
Requires: authconfig-python3 = %{version}-%{release}
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : python3-dev

%description


%package bin
Summary: bin components for the authconfig package.
Group: Binaries
Requires: authconfig-data = %{version}-%{release}
Requires: authconfig-license = %{version}-%{release}

%description bin
bin components for the authconfig package.


%package data
Summary: data components for the authconfig package.
Group: Data

%description data
data components for the authconfig package.


%package license
Summary: license components for the authconfig package.
Group: Default

%description license
license components for the authconfig package.


%package locales
Summary: locales components for the authconfig package.
Group: Default

%description locales
locales components for the authconfig package.


%package man
Summary: man components for the authconfig package.
Group: Default

%description man
man components for the authconfig package.


%package python
Summary: python components for the authconfig package.
Group: Default
Requires: authconfig-python3 = %{version}-%{release}

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
cd %{_builddir}/authconfig-7.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635705265
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --with-python-rev=3
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1635705265
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/authconfig
cp %{_builddir}/authconfig-7.0.1/COPYING %{buildroot}/usr/share/package-licenses/authconfig/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
%make_install
%find_lang authconfig
## install_append content
# move all from /usr/lib64/ to /usr/lib as we don't do /usr/lib64 in python paths
lib_path=$(python -c "import sys; print(sys.path[-1])")
lib64_path=$(echo $lib_path | sed 's!/lib/!/lib64/!')
mkdir -pv %{buildroot}/$lib_path
cp -av %{buildroot}/$lib64_path/* %{buildroot}/$lib_path/
rm -rv %{buildroot}/$lib64_path
## install_append end

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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/authconfig/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/fingerprint-auth-ac.5
/usr/share/man/man5/password-auth-ac.5
/usr/share/man/man5/postlogin-ac.5
/usr/share/man/man5/smartcard-auth-ac.5
/usr/share/man/man5/system-auth-ac.5
/usr/share/man/man8/authconfig.8
/usr/share/man/man8/cacertdir_rehash.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f authconfig.lang
%defattr(-,root,root,-)

