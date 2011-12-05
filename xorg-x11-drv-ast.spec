%define tarball xf86-video-ast
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:   Xorg X11 ast video driver
Name:      xorg-x11-drv-ast
Version:   0.89.9
Release:   1.1%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Source1:   ast.xinf

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.3.0.0-6

Requires:  hwdata
Requires:  xorg-x11-server-Xorg >= 1.3.0.0-6

%description 
X.Org X11 ast video driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
%configure --disable-static --disable-dri
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases/

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/ast_drv.so
%{_datadir}/hwdata/videoaliases/ast.xinf

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.89.9-1.1
- Rebuilt for RHEL 6

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 0.89.9-1
- ast 0.89.9

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.87.0-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 0.87.0-3.1
- ABI bump

* Mon Jun 22 2009 Adam Jackson <ajax@redhat.com> 0.87.0-3
- Fix ABI for new server

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.87.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 0.87.0-1
- Latest upstream release

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 0.85.0-2
- update for latest server API

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 0.85.0-1
- Latest upstream release

* Mon Mar 10 2008 Dave Airlie <airlied@redhat.com> 0.81.0-8
- pciaccess conversion

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.81.0-7
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 0.81.0-6
- Rebuild for PPC toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 0.81.0-5
- Update Requires and BuildRequires.  Disown the module directories.  Add
  Requires: hwdata.

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 0.81.0-4
- ExclusiveArch -> ExcludeArch

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.81.0-3
- rebuild

* Sat Jun 17 2006 Mike A. Harris <mharris@redhat.com> 0.81.0-2
- Update ast.xinf with PCI ID list from driver.

* Sat Jun 17 2006 Mike A. Harris <mharris@redhat.com> 0.81.0-1
- Initial spec file for ast cloned from mga video driver spec version 1.4.1-3
