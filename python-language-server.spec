#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-language-server
Version  : 0.36.2
Release  : 30
URL      : https://files.pythonhosted.org/packages/66/30/0c31b052ede62bbeddf4110db57c78d3c704506178caa18b2f0be2271293/python-language-server-0.36.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/66/30/0c31b052ede62bbeddf4110db57c78d3c704506178caa18b2f0be2271293/python-language-server-0.36.2.tar.gz
Summary  : Python Language Server for the Language Server Protocol
Group    : Development/Tools
License  : MIT
Requires: python-language-server-bin = %{version}-%{release}
Requires: python-language-server-license = %{version}-%{release}
Requires: python-language-server-python = %{version}-%{release}
Requires: python-language-server-python3 = %{version}-%{release}
Requires: flake8
Requires: jedi
Requires: mccabe
Requires: pluggy
Requires: pycodestyle
Requires: pydocstyle
Requires: pyflakes
Requires: pylint
Requires: python-jsonrpc-server
Requires: rope
Requires: ujson
Provides: pypi(python_language_server)

BuildRequires : buildreq-distutils3
BuildRequires : flake8
BuildRequires : jedi
BuildRequires : mccabe
BuildRequires : pluggy
BuildRequires : pycodestyle
BuildRequires : pydocstyle
BuildRequires : pyflakes
BuildRequires : pylint
BuildRequires : python-jsonrpc-server
BuildRequires : rope
BuildRequires : ujson
Patch1: deps.patch

%description
======================

%package bin
Summary: bin components for the python-language-server package.
Group: Binaries
Requires: python-language-server-license = %{version}-%{release}

%description bin
bin components for the python-language-server package.


%package license
Summary: license components for the python-language-server package.
Group: Default

%description license
license components for the python-language-server package.


%package python
Summary: python components for the python-language-server package.
Group: Default
Requires: python-language-server-python3 = %{version}-%{release}

%description python
python components for the python-language-server package.


%package python3
Summary: python3 components for the python-language-server package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-language-server package.


%prep
%setup -q -n python-language-server-0.36.2
cd %{_builddir}/python-language-server-0.36.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1616687503
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-language-server
cp %{_builddir}/python-language-server-0.36.2/LICENSE %{buildroot}/usr/share/package-licenses/python-language-server/4df3c87108ebab83aa7bb222e245d841c6574d4f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyls

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-language-server/4df3c87108ebab83aa7bb222e245d841c6574d4f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
