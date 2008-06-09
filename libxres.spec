%define libxres %mklibname xres 1
Name: libxres
Summary:  X Resource Information Extension Library
Version: 1.0.3
Release: %mkrel 2
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

%package -n %{libxres}
Summary:  X Resource Information Extension Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxres}
X Resource Information Extension Library

#-----------------------------------------------------------

%package -n %{libxres}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxres} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxres-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxres}-devel
Development files for %{name}

%pre -n %{libxres}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxres}-devel
%defattr(-,root,root)
%{_libdir}/libXRes.so
%{_libdir}/libXRes.la
%{_libdir}/pkgconfig/xres.pc
%{_includedir}/X11/extensions/XRes.h
%{_mandir}/man3/XRes*

#-----------------------------------------------------------

%package -n %{libxres}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxres}-devel = %{version}
Provides: libxres-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxres}-static-devel
Static development files for %{name}

%files -n %{libxres}-static-devel
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

%files -n %{libxres}
%defattr(-,root,root)
%{_libdir}/libXRes.so.1
%{_libdir}/libXRes.so.1.0.0


