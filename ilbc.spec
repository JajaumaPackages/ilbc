Name:		ilbc
Summary:	Internet Low Bitrate Codec
Version:	1.1.1
Release:	9%{?dist}
License:	BSD
Group:		Development/Libraries
# wget --content-disposition https://github.com/dekkers/libilbc/tarball/88cd161
Source0:	dekkers-libilbc-upstream-1.1.1-9-g88cd161.tar.gz
# Fedora/EPEL-specific
Patch1:		%{name}-0001-Don-t-build-silently.patch
# Fedora/EPEL-specific
Patch2:		%{name}-0002-No-dist-xz-for-EL5.patch
# Fedora/EPEL-specific
Patch3:		ilbc-0003-Suppress-warning-about-unused-parameter-s.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%description
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for
robust voice communication over IP. The codec is designed for narrow
band speech and results in a payload bit rate of 13.33 kbit/s with an
encoding frame length of 30 ms and 15.20 kbps with an encoding length
of 20 ms. The iLBC codec enables graceful speech quality degradation in
the case of lost frames, which occurs in connection with lost or
delayed IP packets.


%package	devel
Summary:	development files for %{name}
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig


%description devel
Additional header files for development with %{name}.


%prep
%setup -q -n dekkers-libilbc-88cd161
%patch1 -p1 -b .fedora_specific
%patch2 -p1 -b .epel5_specific
%patch3 -p1 -b .epel5_specific


%build
autoreconf -ivf
%{configure} --disable-static --with-pic
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libilbc.la
# Required for compatibility with a very old apps
cd %{buildroot}%{_libdir}/pkgconfig && ln -s libilbc.pc ilbc.pc

# Make compat symlinks
cd %{buildroot}%{_includedir}
ln -s ilbc.h iLBC_decode.h
ln -s ilbc.h iLBC_define.h
ln -s ilbc.h iLBC_encode.h


%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc COPYING README
%{_libdir}/lib%{name}.so.*


%files devel
%{_includedir}/ilbc.h
# Compat symlinks
%{_includedir}/iLBC_decode.h
%{_includedir}/iLBC_define.h
%{_includedir}/iLBC_encode.h
%{_libdir}/pkgconfig/ilbc.pc
%{_libdir}/pkgconfig/libilbc.pc
%{_libdir}/lib%{name}.so


%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 12 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.1-3
- Added licensing info

* Wed Aug 15 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.1-2
- Add compat symlinks for old apps

* Wed May  9 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.1-1
- Ver. 1.1.1

* Thu Oct 20 2011 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1
- Initial package
