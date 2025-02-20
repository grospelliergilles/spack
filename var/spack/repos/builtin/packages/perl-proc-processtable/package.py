# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
# Copyright 2023 EMBL-European Bioinformatics Institute
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlProcProcesstable(PerlPackage):
    """Perl extension to access the unix process table"""

    homepage = "https://metacpan.org/pod/Proc::ProcessTable"
    url = "https://cpan.metacpan.org/authors/id/J/JW/JWB/Proc-ProcessTable-0.636.tar.gz"

    maintainers("EbiArnie")

    version("0.636", sha256="944224ffb00fc1ef35069633770a0afda8623b5c7532d1e4ab48a9df394890fd")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))

    def test_use(self):
        """Test 'use module'"""
        options = ["-we", 'use strict; use Proc::ProcessTable; print("OK\n")']

        perl = self.spec["perl"].command
        out = perl(*options, output=str.split, error=str.split)
        assert "OK" in out
