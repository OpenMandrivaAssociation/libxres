%define major 1
%define libname %mklibname xres %{major}
%define devname %mklibname xres -d

Summary:	X Resource Information Extension Library
Name:		libxres
Version:	1.0.7
Release:	9
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXres-%{version}.tar.bz2

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
%setup -qn libXres-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXRes.so.%{major}*

%files -n %{devname}
%{_libdir}/libXRes.so
%{_libdir}/pkgconfig/xres.pc
%{_includedir}/X11/extensions/XRes.h
%{_mandir}/man3/XRes*

