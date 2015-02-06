%define upstream_name    File-Lockf
%define upstream_version 0.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	5

Summary: 	%{upstream_name} module for perl
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0: 	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
File-Lockf module for perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(444,root,root,755)
%doc COPYRIGHT README
%dir %{perl_vendorlib}/*/File
%{perl_vendorlib}/*/File/lockf.pm
%dir %{perl_vendorlib}/*/auto/File
%dir %{perl_vendorlib}/*/auto/File/lockf
%{perl_vendorlib}/*/auto/File/lockf/lockf.so
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.200.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-2mdv2011.0
+ Revision: 555829
- rebuild for perl 5.12

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2010.0
+ Revision: 403172
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.20-12mdv2009.0
+ Revision: 256939
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.20-10mdv2008.1
+ Revision: 152078
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 0.20-9mdv2008.0
+ Revision: 67613
- use %%mkrel


* Tue Nov 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.20-9mdk
- rebuild for new perl

* Thu Sep 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.20-8mdk
- rebuild

* Sun Aug 17 2003 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 0.20-7mdk
- rebuild for new perl
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.20-6mdk
- rebuild for new auto{prov,req}

* Thu May 01 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.20-5mdk
- distlint error

* Fri Dec 20 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.20-4mdk
- remove buildarch i586

* Thu Jul 25 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.20-3mdk
- rebuild for new perl

* Tue Jun 04 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.20-2mdk
- submitted by Peter Chen <petechen@netilla.com>

* Tue Jun 04 2002 Peter Chen <petechen@netilla.com> 0.20-1mdk
- 0.20

