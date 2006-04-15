#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Widget
Summary:	HTML::Widget - HTML Widget And Validation Framework
Summary(pl):	HTML::Widget - szkielet widgetów i kontroli poprawno¶ci HTML-a
Name:		perl-HTML-Widget
Version:	1.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/C/CF/CFRANKS/HTML-Widget-1.06.tar.gz
# Source0-md5:	ee62b38523b15b7c180c37cb8256dd59
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Class-Accessor-Chained
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-Email-Valid
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTML-Scrubber
BuildRequires:	perl-Module-Pluggable-Fast
BuildRequires:	perl-Test-NoWarnings
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Create easy to maintain HTML widgets!

Everything is optional, use validation only or just generate forms,
you can embed and merge them later.

The API was designed similar to other popular modules like
Data::FormValidator and FormValidator::Simple,
HTML::FillInForm is also built in (and much faster).

This module is very powerful, don't misuse it as a template system!

%description -l pl
Modu³ do tworzenia ³atwych w utrzymianiu widgetów HTML.

Wszystko jest opcjonalne, mo¿na u¿ywaæ tylko kontroli poprawno¶ci lub
tylko tworzyæ formularze; mo¿na osadzaæ je i w³±czaæ pó¼niej.

API zosta³o zaprojektowane na podobieñstwo innych popularnych modu³ów,
takich jak Data::FormValidator i FormValidator::Simple;
HTML::FillInForm jest tak¿e wbudowany (i du¿o szybszy).

Ten modu³ jest naprawdê potê¿ny, nie nale¿y go nadu¿ywaæ jako systemu
szablonów!

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/*.pm
%{perl_vendorlib}/HTML/Widget
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
