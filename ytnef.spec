#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
#
Name     : ytnef
Version  : 2.1.2
Release  : 7
URL      : https://github.com/Yeraze/ytnef/archive/v2.1.2/ytnef-2.1.2.tar.gz
Source0  : https://github.com/Yeraze/ytnef/archive/v2.1.2/ytnef-2.1.2.tar.gz
Summary  : Yerase's TNEF Stream Reader library
Group    : Development/Tools
License  : GPL-2.0
Requires: ytnef-bin = %{version}-%{release}
Requires: ytnef-lib = %{version}-%{release}
Requires: ytnef-license = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Yerase's TNEF Stream Reader
===========================
[![Build Status](https://api.travis-ci.com/Yeraze/ytnef.svg?branch=master)](https://travis-ci.com/github/Yeraze/ytnef)

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
%setup -q -n ytnef-2.1.2
cd %{_builddir}/ytnef-2.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1687306720
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1687306720
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
