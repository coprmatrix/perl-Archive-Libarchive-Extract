#
# spec file for package perl-Archive-Libarchive-Extract (Version 0.03)
#
# Copyright (c) 125 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define cpan_name Archive-Libarchive-Extract
Name:           perl-Archive-Libarchive-Extract
Version:        0.03
Release:        0%{?autorelease}
License:   Artistic-1.0 or GPL-1.0-or-later
Summary:        An archive extracting mechanism (using libarchive)
Url:            https://metacpan.org/release/%{cpan_name}
Source0:         https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-macros-suse
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Archive::Libarchive) >= 0.04
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(Test::Script) >= 1.09
Requires:       perl(Archive::Libarchive) >= 0.04
Requires:       perl(File::chdir)
Requires:       perl(Path::Tiny)
Requires:       perl(Ref::Util)
Provides:       perl(Archive::Libarchive::Extract)
%{?perl_requires}

%description
This class provides a simple interface for extracting archives using
'libarchive'. Although it provides similar functionality to
Archive::Extract and Archive::Extract::Libarchive it intentionally does not
provide a compatible interface. In particular it tends to throw exceptions
instead tracking errors as a property. It also supports some unique
features of the various classes that use the "Extract" style interface:

* Many Many formats

Tar, Zip, RAR, ISO 9660 images, gzip, bzip2, etc.

* Zips with encrypted entries

You can specify the passphrase or a passphrase callback with the
constructor

* Multi-file RAR archives

If filename is an array reference it will be assumed to be a list of
filenames representing a single multi-file archive.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README
%license LICENSE

%changelog
