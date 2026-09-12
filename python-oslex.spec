Name:		python-oslex
Version:	2.0.0
Release:	1
Summary:	OS-independent wrapper for shlex and mslex
License:	MIT
Group:		Development/Python
URL:		https://github.com/petamas/oslex
Source0:	https://files.pythonhosted.org/packages/source/o/oslex/oslex-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(hatchling)

%description
oslex is an OS-independent wrapper around shlex (POSIX) and mslex
(Windows) for splitting and quoting command lines.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/oslex
%{py_sitedir}/oslex-*.*-info
