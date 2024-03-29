# NOTE:
# - Check releases here: https://github.com/google/closure-compiler/wiki/Releases
# TODO
# - build from source (get-source.sh fetches it)

%define		java_min_classdataversion 51.0
Summary:	Closure Compiler - JavaScript compressor
Summary(pl.UTF-8):	Closure Compiler - kompresor JavaScriptu
Name:		closure-compiler
Version:	20161201
Release:	2
License:	Apache v2.0
Group:		Applications/WWW
Source0:	http://dl.google.com/closure-compiler/compiler-%{version}.tar.gz
# Source0-md5:	fc1f0c8ad1658c5ee99aec1abdfa9958
Source1:	%{name}.sh
Source2:	get-source.sh
Source4:	Changes
URL:		http://closure-compiler.appspot.com/
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.745
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

%description -l pl.UTF-8
Closure Compiler to narzędzie przyspieszające pobieranie i
uruchamianie JavaScriptu. Jest to prawdziwy kompilator tego języka,
ale zamiast kompilowania do kodu maszynowego, kompiluje JavaScript do
lepszego JavaScriptu. Analizuje źródła, usuwa martwy kod i przepisuje
pozostały, minimalizując go. Sprawdza także składnię, odwołania oraz
typy zmiennych i ostrzega o najczęstszych pułapkach JavaScriptu.

%prep
%setup -qc
cp -p %{SOURCE4} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}}
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}

# jars
cp -p closure-compiler-v%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md Changes
%attr(755,root,root) %{_bindir}/closure-compiler
%{_javadir}/closure-compiler-%{version}.jar
%{_javadir}/closure-compiler.jar
