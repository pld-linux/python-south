#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	south
Summary:	South - schema and data migrations for Django projects
Name:		python-%{module}
Version:	0.8.4
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Python
#Source0:	http://www.aeracode.org/releases/south/%{module}-%{version}.tar.gz
Source0:	%{module}-%{version}.tar.gz
# Source0-md5:	4b7da843d1a5f04ee02e0ba4904fcd88
URL:		http://south.aeracode.org/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
Requires:	python-django
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
South brings migrations to Django applications. Its main objectives
are to provide a simple, stable and database-independent migration
layer to prevent all the hassle schema changes over time bring to your
Django applications.

%prep
%setup -q -n South-%{version}

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install


%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/south
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/South*.egg-info
%endif
