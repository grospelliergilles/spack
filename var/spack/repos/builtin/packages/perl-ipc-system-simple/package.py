# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
# Copyright 2023 EMBL-European Bioinformatics Institute
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlIpcSystemSimple(PerlPackage):
    """Run commands simply, with detailed diagnostics"""

    homepage = "https://metacpan.org/pod/IPC::System::Simple"
    url = "https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/IPC-System-Simple-1.30.tar.gz"

    maintainers("EbiArnie")

    version("1.30", sha256="22e6f5222b505ee513058fdca35ab7a1eab80539b98e5ca4a923a70a8ae9ba9e")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))

    def test_use(self):
        """Test 'use module'"""
        options = ["-we", 'use strict; use IPC::System::Simple; print("OK\n")']

        perl = self.spec["perl"].command
        out = perl(*options, output=str.split, error=str.split)
        assert "OK" in out
