Summary:	Makes bootable ISO images for sparc systems
Summary(pl):	Tworzy obrazy ISO przygotowane do wystartowania na systemach sparc
Name:		mksunbootcd
Version:	1.0
Release:	1
License:	BSD
Group:		Applications/System
Group(cs):	Aplikace/Syst�m
Group(da):	Programmer/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(fr):	Applications/Syst�me
Group(is):	Forrit/Kerfisforrit
Group(it):	Applicazioni/Sistema
Group(ja):	���ץꥱ�������/�����ƥ�
Group(no):	Applikasjoner/System
Group(pl):	Aplikacje/System
Group(pt):	Aplica��es/Sistema
Group(pt_BR):	Aplica��es/Sistema
Group(ru):	����������/�������
Group(sl):	Programi/Sistem
Group(sv):	Till�mpningar/System
Group(uk):	�������Φ ��������/�������
Source0:	ftp://ftp.netbsd.org/pub/NetBSD/misc/mksunbootcd/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
`mksunbootcd' combines filesystem partitions for Sun Microsystems,
Inc. computers into an image suitable for writing to a compact disc,
that will allow the disc to be booted on the sun3, sun3x, sun4, sun4c,
sun4m and sun4u platforms.

%description -l pl
Tworzy obrazy ISO, kt�re mog� by� u�yte do wystartowania system�w
sparc (sun3, sun3x, sun4, sun4c, sun4m, sun4u).

%prep
%setup -q -n %{name}-%{version}

%build
autoconf
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install mksunbootcd $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README NEWS THANKS INSTALL COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc {README,NEWS,THANKS,INSTALL,COPYING}.gz
