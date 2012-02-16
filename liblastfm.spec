
Name:		liblastfm
Version:	0.3.3
Release:	3%{?dist}.R
Summary:	Libraries to integrate Last.fm services

Group:		System Environment/Libraries
License:	GPLv2+
URL:		http://github.com/mxcl/liblastfm/tree/master 
# redirect from http://github.com/mxcl/liblastfm/tarball/%{version}
Source0:	mxcl-liblastfm-%{version}-0-gf0b3239.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Patch1: liblastfm-0.3.2-qmake.patch

BuildRequires: fftw3-devel
BuildRequires: libsamplerate-devel
BuildRequires: qt4-devel
BuildRequires: ruby

%description
Liblastfm is a collection of libraries to help you integrate Last.fm services
into your rich desktop software.

%package devel
Summary: Development files for %{name}
Group:	 Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
# wtf ?  -- Rex
%setup -q -n mxcl-liblastfm-1c739eb

%patch1 -p1 -b .qmake


%build
# hack around hard-coded libdir, see qmake patch
LIB=%{_lib} ; export LIB
# no autofoo
./configure \
  --prefix %{_prefix} \
  --no-strip \
  --release

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc README COPYING
%{_libdir}/liblastfm.so.0*
%{_libdir}/liblastfm_fingerprint.so.0*

%files devel
%defattr(-,root,root,-)
%{_libdir}/liblastfm.so
%{_libdir}/liblastfm_fingerprint.so
%{_includedir}/lastfm.h
%{_includedir}/lastfm/


%changelog
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.3.3-2
- Rebuilt for gcc bug 634757

* Sat Sep 25 2010 Rex Dieter <rdieter@fedoraproject.org> 0.3.3-1
- liblastfm-0.3.3
- missing symbols in liblastfm-0.3.2 (#636729)

* Fri Sep 17 2010 Rex Dieter <rdieter@fedoraproject.org> 0.3.2-1
- liblastfm-0.3.2

* Tue Jun 30 2009 Rex Dieter <rdieter@fedoraproject.org> 0.3.0-2
- rpmlint clean(er)
- BR: libsamplerate-devel
- -devel: fix Requires (typo, +%%?_isa)

* Tue Jun 09 2009 Rex Dieter <rdieter@fedoraproject.org> 0.3.0-1
- liblastfm-0.3.0

* Tue May 05 2009 Rex Dieter <rdieter@fedoraproject.org> 0.2.1-1
- liblastfm-0.2.1, first try
