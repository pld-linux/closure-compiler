# TODO
# - build from source (get-source.sh fetches it)

%include	/usr/lib/rpm/macros.java
Summary:	Closure Compiler - JavaScript compressor
Name:		closure-compiler
Version:	20111003
Release:	1
License:	Apache v2.0
Group:		Applications/WWW
Source0:	http://closure-compiler.googlecode.com/files/compiler-%{version}.tar.gz
# Source0-md5:	6108a6f2c3b3e357f8758a24ea8b01c6
Source1:	%{name}.sh
Source2:	get-source.sh
URL:		http://closure-compiler.appspot.com/
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Closure Compiler is a tool for making JavaScript download and run
faster. It is a true compiler for JavaScript. Instead of compiling
from a source language to machine code, it compiles from JavaScript to
better JavaScript. It parses your JavaScript, analyzes it, removes
dead code and rewrites and minimizes what's left. It also checks
syntax, variable references, and types, and warns about common
JavaScript pitfalls.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}}
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}

# jars
cp -p compiler.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_javadir}/*.jar
