%define libname %mklibname xres 1
%define develname %mklibname xres -d
%define staticname %mklibname xres -s -d

Name: libxres
Summary:  X Resource Information Extension Library
Version: 1.0.5
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXres-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X Resource Information Extension Library

#-----------------------------------------------------------

%package -n %{libname}
Summary:  X Resource Information Extension Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
X Resource Information Extension Library

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libname} = %{version}-%{release}
Requires: x11-proto-devel >= 1.0.0
Provides: libxres-devel = %{version}-%{release}
Provides: libxres1-devel = %{version}-%{release}
Obsoletes: %{mklibname xres 1 -d}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXRes.so
%{_libdir}/libXRes.la
%{_libdir}/pkgconfig/xres.pc
%{_includedir}/X11/extensions/XRes.h
%{_mandir}/man3/XRes*

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}-%{release}
Provides: libxres-static-devel = %{version}-%{release}
Provides: libxres1-static-devel = %{version}-%{release}
Obsoletes: %{mklibname xres 1 -s -d}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libXRes.a

#-----------------------------------------------------------

%prep
%setup -q -n libXres-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXRes.so.1
%{_libdir}/libXRes.so.1.0.0
