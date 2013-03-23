Summary:	making Embedded Linux easy
Name:		buildroot
Version:	2013.02
Release:	0.1
License:	GPL v2+
Group:		Applications/File
Source0:	http://buildroot.uclibc.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	e5bd97ef02208014fd998d5ebe498e3f
URL:		http://buildroot.uclibc.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Buildroot is a set of Makefiles and patches that makes it easy to
generate a complete embedded Linux system. Buildroot can generate any
or all of a cross-compilation toolchain, a root filesystem, a kernel
image and a bootloader image. Buildroot is useful mainly for people
working with small or embedded systems, using various CPU
architectures (x86, ARM, MIPS, PowerPC, etc.) : it automates the
building process of your embedded system and eases the
cross-compilation process.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
