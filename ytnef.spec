#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ytnef
Version  : 1.9.3
Release  : 5
URL      : https://github.com/Yeraze/ytnef/archive/v1.9.3.tar.gz
Source0  : https://github.com/Yeraze/ytnef/archive/v1.9.3.tar.gz
Summary  : Yerase's TNEF Stream Reader library
Group    : Development/Tools
License  : GPL-2.0
Requires: ytnef-bin = %{version}-%{release}
Requires: ytnef-lib = %{version}-%{release}
Requires: ytnef-license = %{version}-%{release}
Patch1: CVE-2021-3403.patch
Patch2: CVE-2021-3404.patch

%description
Yerase's TNEF Stream Reader
===========================
[![Build Status](https://travis-ci.org/Yeraze/ytnef.svg?branch=master)](https://travis-ci.org/Yeraze/ytnef)

%package bin
Summary: bin components for the ytnef package.
Group: Binaries
Requires: ytnef-license = %{version}-%{release}

%description bin
bin components for the ytnef package.


%package dev
Summary: dev components for the ytnef package.
Group: Development
Requires: ytnef-lib = %{version}-%{release}
Requires: ytnef-bin = %{version}-%{release}
Provides: ytnef-devel = %{version}-%{release}
Requires: ytnef = %{version}-%{release}

%description dev
dev components for the ytnef package.


%package lib
Summary: lib components for the ytnef package.
Group: Libraries
Requires: ytnef-license = %{version}-%{release}

%description lib
lib components for the ytnef package.


%package license
Summary: license components for the ytnef package.
Group: Default

%description license
license components for the ytnef package.


%prep
%setup -q -n ytnef-1.9.3
cd %{_builddir}/ytnef-1.9.3
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664894011
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1664894011
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ytnef
cp %{_builddir}/ytnef-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ytnef/12549569098cbb0efa8a4aa91f5f38068791fe42 || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ytnef
/usr/bin/ytnefprint
/usr/bin/ytnefprocess

%files dev
%defattr(-,root,root,-)
/usr/include/mapi.h
/usr/include/mapidefs.h
/usr/include/mapitags.h
/usr/include/tnef-errors.h
/usr/include/tnef-types.h
/usr/include/ytnef.h
/usr/lib64/libytnef.so
/usr/lib64/pkgconfig/libytnef.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libytnef.so.0
/usr/lib64/libytnef.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ytnef/12549569098cbb0efa8a4aa91f5f38068791fe42
