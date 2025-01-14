%define major 1
%define libname %mklibname xres %{major}
%define devname %mklibname xres -d

Summary:	X Resource Information Extension Library
Name:		libxres
Version:	1.2.2
Release:	2
Group:		Development/X11
License:	MIT
Url:		https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXres-%{version}.tar.xz

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
X Resource Information Extension Library.

%package -n %{libname}
Summary:	X Resource Information Extension Library
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
X Resource Information Extension Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	libxres-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%autosetup -n libXres-%{version} -p1

%build
%configure \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libXRes.so.%{major}*

%files -n %{devname}
%{_libdir}/libXRes.so
%{_libdir}/pkgconfig/xres.pc
%{_includedir}/X11/extensions/XRes.h
%doc %{_mandir}/man3/XRes*
