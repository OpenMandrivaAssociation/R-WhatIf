%global packname  WhatIf
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.5_5
Release:          1
Summary:          Software for Evaluating Counterfactuals
Group:            Sciences/Mathematics
License:          GPLv3
URL:              https://cran.r-project.org/web/packages/WhatIf/index.html
Source0:          http://cran.r-project.org/src/contrib/WhatIf_1.5-5.tar.gz
BuildRequires:    R-devel R-lpSolve
Requires:         R-core R-lpSolve
BuildArch:        noarch

%description
Inferences about counterfactuals are essential for prediction,
answering what if questions, and estimating causal effects.
However, when the counterfactuals posed are too far from the data at hand,
conclusions drawn from well-specified statistical analyses become based largely
on speculation hidden in convenient modeling assumptions that few would be 
willing to defend. Unfortunately, standard statistical approaches assume the 
veracity of the model rather than revealing the degree of model-dependence, 
which makes this problem hard to detect. WhatIf offers easy-to-apply methods 
to evaluate counterfactuals that do not require sensitivity testing over 
specified classes of models. If an analysis fails the tests offered here, 
then we know that substantive inferences will be sensitive to at least some 
modeling choices that are not based on empirical evidence, no matter what 
method of inference one chooses to use. WhatIf implements the methods for 
evaluating counterfactuals discussed in Gary King and Langche Zeng, 2006, 
"The Dangers of Extreme Counterfactuals," Political Analysis 14 (2); 
and Gary King and Langche Zeng, 2007, "When Can History Be Our Guide? 
The Pitfalls of Counterfactual Inference," 
International Studies Quarterly 51 (March).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
rm %{buildroot}%{rlibdir}/%{packname}/doc/whatif.idx
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%doc %{rlibdir}/%{packname}/doc/.latex2html-init
%doc %{rlibdir}/%{packname}/doc/Makefile
%doc %{rlibdir}/%{packname}/doc/index.html
%doc %{rlibdir}/%{packname}/doc/index.shtml
%doc %{rlibdir}/%{packname}/doc/whatif.out
%doc %{rlibdir}/%{packname}/doc/whatif.pdf
%doc %{rlibdir}/%{packname}/doc/whatif.tex
%doc %{rlibdir}/%{packname}/doc/whatif.toc