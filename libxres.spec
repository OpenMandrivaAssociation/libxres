%define major 1
%define libname %mklibname xres %{major}
%define develname %mklibname xres -d

Name: libxres
Summary:  X Resource Information Extension Library
Version: 1.0.5
Release: 5
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXres-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X Resource Information Extension Library

%package -n %{libname}
Summary:  X Resource Information Extension Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
X Resource Information Extension Library

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Provides: libxres-devel = %{version}-%{release}
Obsoletes: %{_lib}xres1-devel
Obsoletes: %{_lib}xres-static-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXres-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXRes.so.%{major}*

%files -n %{develname}
%{_libdir}/libXRes.so
%{_libdir}/pkgconfig/xres.pc
%{_includedir}/X11/extensions/XRes.h
%{_mandir}/man3/XRes*

