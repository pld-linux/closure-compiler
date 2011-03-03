# TODO
# - build from source
# - NOTE: build-data.properties is included twice in .jar

%include	/usr/lib/rpm/macros.java
Summary:	Closure Compiler - JavaScript compressor
Name:		closure-compiler
Version:	20100201
Release:	0.1
License:	Apache v2.0
Group:		Applications/WWW
Source0:	http://closure-compiler.googlecode.com/files/compiler-%{version}.tar.gz
# Source0-md5:	71bb4f8975ffc81fd0b9a82e18318a49
Source1:	%{name}.sh
URL:		http://closure-compiler.appspot.com/
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Closure Compiler is a JavaScript optimizing compiler. It parses your
JavaScript, analyzes it, removes dead code and rewrites and minimizes
what's left. It also checks syntax, variable references, and types,
and warns about common JavaScript pitfalls. It is used in many of
Google's JavaScript apps, including Gmail, Google Web Search, Google
Maps, and Google Docs.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}}
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}

# jars
cp -a compiler.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_javadir}/*.jar
