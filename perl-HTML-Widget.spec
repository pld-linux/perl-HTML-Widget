#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Widget
Summary:	HTML::Widget - HTML Widget And Validation Framework
Summary(pl.UTF-8):	HTML::Widget - szkielet widgetów i kontroli poprawności HTML-a
Name:		perl-HTML-Widget
Version:	1.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	62f582be030a322b225ced8f03012905
URL:		http://search.cpan.org/dist/HTML-Widget/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Class-Accessor-Chained
BuildRequires:	perl-Class-Data-Accessor
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-Email-Valid
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTML-Scrubber
BuildRequires:	perl-Module-Pluggable-Fast
BuildRequires:	perl-Test-NoWarnings
BuildRequires:	perl-Test-Pod-Coverage
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

%description -l pl.UTF-8
Moduł do tworzenia łatwych w utrzymianiu widgetów HTML.

Wszystko jest opcjonalne, można używać tylko kontroli poprawności lub
tylko tworzyć formularze; można osadzać je i włączać później.

API zostało zaprojektowane na podobieństwo innych popularnych modułów,
takich jak Data::FormValidator i FormValidator::Simple;
HTML::FillInForm jest także wbudowany (i dużo szybszy).

Ten moduł jest naprawdę potężny, nie należy go nadużywać jako systemu
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
