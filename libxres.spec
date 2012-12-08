%define major 1
%define libname %mklibname xres %{major}
%define develname %mklibname xres -d

Name:		libxres
Summary:	X Resource Information Extension Library
Version:	1.0.6
Release:	2
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXres-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
X Resource Information Extension Library

%package -n %{libname}
Summary:	X Resource Information Extension Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

%description -n %{libname}
X Resource Information Extension Library

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	libxres-devel = %{version}-%{release}
Obsoletes:	%{_lib}xres1-devel < 1.0.6
Obsoletes:	%{_lib}xres-static-devel < 1.0.6
Conflicts:	libxorg-x11-devel < 7.0

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
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXRes.so.%{major}*

%files -n %{develname}
%{_libdir}/libXRes.so
%{_libdir}/pkgconfig/xres.pc
%{_includedir}/X11/extensions/XRes.h
%{_mandir}/man3/XRes*


%changelog
* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.6-1
+ Revision: 783974
- version update 1.0.6

* Thu Mar 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0.5-5
+ Revision: 783375
- Remove pre scriptlet to correct rpm upgrade moving from /usr/X11R6.

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.5-4
+ Revision: 745755
- rebuild
- disabled static build
- removed .la files
- cleaned up spec
- employed major macro

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-3
+ Revision: 662428
- mass rebuild

* Sat Feb 19 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.5-2
+ Revision: 638669
- forgot to bump release
- dropped major from devel and static pkgs
- added proper provides and obsoletes

* Fri Oct 29 2010 Thierry Vignaud <tv@mandriva.org> 1.0.5-1mdv2011.0
+ Revision: 589869
- new release

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.4-1mdv2010.1
+ Revision: 464043
- New release: 1.0.4

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.3-4mdv2010.0
+ Revision: 425936
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-3mdv2009.0
+ Revision: 223085
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-2mdv2008.1
+ Revision: 150870
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

