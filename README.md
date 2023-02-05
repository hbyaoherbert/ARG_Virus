# ARG_Virus
scripts for viral metagenomics in the ARG project  
Folder virfinder contains scripts for parsing Virfinder viral contig identification results.  
Folder virsorter contains scripts for parsing VirSorter viral contig identification results.  
Folder fpremoval contains scripts for removing potential false positives in virfinder and virsorter reported viral contigs, aligning agaist three database:
   1. Busco conserved bacteria gene database
   2. CAT bacteria genome database
   3. VPF viral gene family database
Folder annotation contains scripts for annotating valid viral contigs to viral species, referenced to Refseq Viral Genomes, based on blastp alignment between genes predicted from discovered viral contigs and viral genes in Refseq Genbank files. Critical steps are :
   1. Number of ORFs of each viral contig is counted
   2. If over 50% of ORFs for a contig align to one reference species, then the contig is assigned to that species (ambiguous case is resolved by total alignment bitscores of different reference species)
   3. For a viral contig annotated to a viral species, this contig must have at least one ORF with alignment length over 20aa to make this annotation valid.

Folder abundance contains scripts for calculation of  relative abundance of viral species
