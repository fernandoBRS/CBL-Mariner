Summary:	Programs for processing and formatting text
Name:		groff
Version:	1.22.3
Release:        4%{?dist}
License:	GPLv3+
URL:		http://www.gnu.org/software/groff
Group:		Applications/Text
Vendor:         Microsoft Corporation
Distribution:   Mariner
Source0:	http://ftp.gnu.org/gnu/groff/%{name}-%{version}.tar.gz
%define sha1 groff=61a6808ea1ef715df9fa8e9b424e1f6b9fa8c091
Provides:	perl(oop_fh.pl)
Provides:	perl(main_subs.pl)
Provides:   perl(man.pl)
Provides:   perl(subs.pl)
Requires: perl
Requires: perl-DBI
Requires: perl-DBIx-Simple
Requires: perl-DBD-SQLite
Requires: perl-File-HomeDir
%description
The Groff package contains programs for processing
and formatting text.
%prep
%setup -q
%build
PAGE=letter ./configure \
	--prefix=%{_prefix} \
	--with-grofferdir=%{_datadir}/%{name}/%{version}/groffer
make
%install
install -vdm 755 %{_defaultdocdir}/%{name}-1.22/pdf
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_infodir}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%files
%defattr(-,root,root)
%license LICENSES
%{_bindir}/*
%{_libdir}/groff/*
%{_defaultdocdir}/%{name}-%{version}/*
%{_datarootdir}/%{name}/*
%{_mandir}/*/*
%changelog
* Sat May 09 00:21:28 PST 2020 Nick Samson <nisamson@microsoft.com> - 1.22.3-4
- Added %%license line automatically

*   Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 1.22.3-3
-   Initial CBL-Mariner import from Photon (license: Apache2).
*	Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.22.3-2
-	GA - Bump release of all rpms
*   Tue Feb 23 2016 Xiaolin Li <xiaolinl@vmware.com> 1.22.3-1
-   Updated to version 1.22.3
*	Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 1.22.2-1
-	Initial build. First version
