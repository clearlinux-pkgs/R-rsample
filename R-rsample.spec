#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rsample
Version  : 1.1.1
Release  : 50
URL      : https://cran.r-project.org/src/contrib/rsample_1.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rsample_1.1.1.tar.gz
Summary  : General Resampling Infrastructure
Group    : Development/Tools
License  : MIT
Requires: R-dplyr
Requires: R-furrr
Requires: R-generics
Requires: R-glue
Requires: R-pillar
Requires: R-purrr
Requires: R-rlang
Requires: R-slider
Requires: R-tibble
Requires: R-tidyr
Requires: R-tidyselect
Requires: R-vctrs
BuildRequires : R-dplyr
BuildRequires : R-furrr
BuildRequires : R-generics
BuildRequires : R-glue
BuildRequires : R-pillar
BuildRequires : R-purrr
BuildRequires : R-rlang
BuildRequires : R-slider
BuildRequires : R-tibble
BuildRequires : R-tidyr
BuildRequires : R-tidyselect
BuildRequires : R-vctrs
BuildRequires : buildreq-R

%description
of resampling objects (e.g. bootstrap, cross-validation).

%prep
%setup -q -n rsample
cd %{_builddir}/rsample

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670504572

%install
export SOURCE_DATE_EPOCH=1670504572
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rsample/DESCRIPTION
/usr/lib64/R/library/rsample/INDEX
/usr/lib64/R/library/rsample/LICENSE
/usr/lib64/R/library/rsample/Meta/Rd.rds
/usr/lib64/R/library/rsample/Meta/features.rds
/usr/lib64/R/library/rsample/Meta/hsearch.rds
/usr/lib64/R/library/rsample/Meta/links.rds
/usr/lib64/R/library/rsample/Meta/nsInfo.rds
/usr/lib64/R/library/rsample/Meta/package.rds
/usr/lib64/R/library/rsample/Meta/vignette.rds
/usr/lib64/R/library/rsample/NAMESPACE
/usr/lib64/R/library/rsample/NEWS.md
/usr/lib64/R/library/rsample/R/rsample
/usr/lib64/R/library/rsample/R/rsample.rdb
/usr/lib64/R/library/rsample/R/rsample.rdx
/usr/lib64/R/library/rsample/doc/Common_Patterns.R
/usr/lib64/R/library/rsample/doc/Common_Patterns.Rmd
/usr/lib64/R/library/rsample/doc/Common_Patterns.html
/usr/lib64/R/library/rsample/doc/Working_with_rsets.R
/usr/lib64/R/library/rsample/doc/Working_with_rsets.Rmd
/usr/lib64/R/library/rsample/doc/Working_with_rsets.html
/usr/lib64/R/library/rsample/doc/index.html
/usr/lib64/R/library/rsample/doc/rsample.R
/usr/lib64/R/library/rsample/doc/rsample.Rmd
/usr/lib64/R/library/rsample/doc/rsample.html
/usr/lib64/R/library/rsample/generate_vctrs.R
/usr/lib64/R/library/rsample/help/AnIndex
/usr/lib64/R/library/rsample/help/aliases.rds
/usr/lib64/R/library/rsample/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/rsample/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/rsample/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/rsample/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/rsample/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/rsample/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/rsample/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/rsample/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/rsample/help/figures/logo.png
/usr/lib64/R/library/rsample/help/paths.rds
/usr/lib64/R/library/rsample/help/rsample.rdb
/usr/lib64/R/library/rsample/help/rsample.rdx
/usr/lib64/R/library/rsample/html/00Index.html
/usr/lib64/R/library/rsample/html/R.css
/usr/lib64/R/library/rsample/tests/testthat.R
/usr/lib64/R/library/rsample/tests/testthat/_snaps/boot.md
/usr/lib64/R/library/rsample/tests/testthat/_snaps/bootci.md
/usr/lib64/R/library/rsample/tests/testthat/_snaps/clustering.md
/usr/lib64/R/library/rsample/tests/testthat/_snaps/compat-vctrs.md
/usr/lib64/R/library/rsample/tests/testthat/_snaps/initial.md
/usr/lib64/R/library/rsample/tests/testthat/_snaps/labels.md
/usr/lib64/R/library/rsample/tests/testthat/_snaps/loo.md
/usr/lib64/R/library/rsample/tests/testthat/_snaps/make_groups.md
/usr/lib64/R/library/rsample/tests/testthat/_snaps/mc.md
/usr/lib64/R/library/rsample/tests/testthat/_snaps/misc.md
/usr/lib64/R/library/rsample/tests/testthat/_snaps/nesting.md
/usr/lib64/R/library/rsample/tests/testthat/_snaps/permutations.md
/usr/lib64/R/library/rsample/tests/testthat/_snaps/rsplit.md
/usr/lib64/R/library/rsample/tests/testthat/_snaps/strata.md
/usr/lib64/R/library/rsample/tests/testthat/_snaps/validation.md
/usr/lib64/R/library/rsample/tests/testthat/_snaps/vfold.md
/usr/lib64/R/library/rsample/tests/testthat/helpers-rsample.R
/usr/lib64/R/library/rsample/tests/testthat/test-boot.R
/usr/lib64/R/library/rsample/tests/testthat/test-bootci.R
/usr/lib64/R/library/rsample/tests/testthat/test-caret.R
/usr/lib64/R/library/rsample/tests/testthat/test-clustering.R
/usr/lib64/R/library/rsample/tests/testthat/test-compat-dplyr.R
/usr/lib64/R/library/rsample/tests/testthat/test-compat-vctrs.R
/usr/lib64/R/library/rsample/tests/testthat/test-fingerprint.R
/usr/lib64/R/library/rsample/tests/testthat/test-for-pred.R
/usr/lib64/R/library/rsample/tests/testthat/test-initial.R
/usr/lib64/R/library/rsample/tests/testthat/test-labels.R
/usr/lib64/R/library/rsample/tests/testthat/test-loo.R
/usr/lib64/R/library/rsample/tests/testthat/test-make-splits.R
/usr/lib64/R/library/rsample/tests/testthat/test-make_groups.R
/usr/lib64/R/library/rsample/tests/testthat/test-manual.R
/usr/lib64/R/library/rsample/tests/testthat/test-mc.R
/usr/lib64/R/library/rsample/tests/testthat/test-misc.R
/usr/lib64/R/library/rsample/tests/testthat/test-names.R
/usr/lib64/R/library/rsample/tests/testthat/test-nesting.R
/usr/lib64/R/library/rsample/tests/testthat/test-permutations.R
/usr/lib64/R/library/rsample/tests/testthat/test-rolling.R
/usr/lib64/R/library/rsample/tests/testthat/test-rset.R
/usr/lib64/R/library/rsample/tests/testthat/test-rsplit.R
/usr/lib64/R/library/rsample/tests/testthat/test-slide.R
/usr/lib64/R/library/rsample/tests/testthat/test-strata.R
/usr/lib64/R/library/rsample/tests/testthat/test-tidy.R
/usr/lib64/R/library/rsample/tests/testthat/test-validation.R
/usr/lib64/R/library/rsample/tests/testthat/test-vfold.R
/usr/lib64/R/library/rsample/vctrs_template.R
