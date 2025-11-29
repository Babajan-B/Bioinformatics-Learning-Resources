#!/usr/bin/env python3
"""
Complete Documentation Builder
Creates all remaining documentation files with proper structure
"""

import os
from pathlib import Path

# Base templates
SIMPLE_INDEX = """# {title}

{description}

## Contents

{content}

---

**Last Updated**: November 2025
"""

PLACEHOLDER_PAGE = """# {title}

> **Status**: Content migration in progress

{description}

## Overview

This page will contain information about {topic}.

**Content from README-2.md will be migrated here.**

## What to Expect

{expectations}

---

**Contributing**: Help us populate this page! See [CONTRIBUTING.md](../../CONTRIBUTING.md)

**Last Updated**: November 2025
"""

def create_file(filepath, content):
    """Create file with proper directory structure"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    Path(filepath).write_text(content)
    print(f"✓ Created: {filepath}")

def main():
    base = Path("docs")
    
    # Intermediate index
    create_file(base / "intermediate/index.md", SIMPLE_INDEX.format(
        title="Intermediate Track",
        description="Real-world bioinformatics analyses for those with basic programming and biology knowledge.",
        content="""
### [Sequence Analysis](sequence-analysis/) 
Multiple alignment, phylogenetics, motif finding, HMM profiles

### [Genomics](genomics/)
NGS technologies, genome assembly, variant calling, annotation

### [Transcriptomics](transcriptomics/)
RNA-seq, differential expression, pathway analysis, single-cell basics

### [Proteomics](proteomics/)
Protein structure, mass spectrometry, functional annotation

### [Algorithms](algorithms/)
Dynamic programming, graph algorithms, machine learning intro

### [Practical Projects](practical-projects/)
Complete RNA-seq pipeline, variant analysis, phylogenetic trees

**Next**: [Advanced Track](../advanced/index.md)
"""
    ))
    
    # Advanced index
    create_file(base / "advanced/index.md", SIMPLE_INDEX.format(
        title="Advanced Track",
        description="Cutting-edge techniques and specialized topics for experienced practitioners.",
        content="""
### [Specialized Omics](specialized-omics/)
Metagenomics, epigenomics, metabolomics, multi-omics integration

### [Advanced Genomics](advanced-genomics/)
Population genomics, structural variants, long-read sequencing, cancer genomics

### [Computational Methods](computational-methods/)
Deep learning, network biology, systems biology, algorithm optimization

### [Specialized Tools](specialized-tools/)
Workflow managers, containers, cloud computing, HPC environments

### [Drug Discovery](drug-discovery/)
Molecular docking, virtual screening, QSAR modeling

### [Research Projects](research-projects/)
Publication-quality analyses and pipelines
"""
    ))
    
    # Pathways index
    create_file(base / "pathways/index.md", SIMPLE_INDEX.format(
        title="Learning Pathways",
        description="Career-oriented learning paths for specific bioinformatics roles.",
        content="""
- [Genomics Specialist](genomics-specialist.md)
- [Computational Biologist](computational-biologist.md)
- [Bioinformatics Data Scientist](data-scientist.md)
- [Structural Biologist](structural-biologist.md)
"""
    ))
    
    # Sample resource pages
    topics = [
        ("resources/tools/essential-tools.md", "Essential Bioinformatics Tools",
         "Core software tools every bioinformatician should know", "tools and software"),
        ("resources/databases/sequence-databases.md", "Sequence Databases",
         "Major nucleotide and protein sequence databases", "database navigation and usage"),
        ("resources/books-and-courses/online-courses.md", "Online Courses",
         "Free and paid online courses for bioinformatics", "course recommendations"),
        ("reference/glossary.md", "Bioinformatics Glossary",
         "Common terms and definitions in bioinformatics", "terminology explanations"),
        ("reference/file-formats-reference.md", "File Formats Reference",
         "Common bioinformatics file formats (FASTA, FASTQ, SAM, VCF, BED, etc.)", "format specifications"),
    ]
    
    for filepath, title, desc, topic in topics:
        create_file(base / filepath, PLACEHOLDER_PAGE.format(
            title=title,
            description=desc,
            topic=topic,
            expectations=f"- Comprehensive coverage of {topic}\\n- Practical examples\\n- Links to official documentation\\n- Usage guidelines"
        ))
    
    print("\n✅  Documentation structure created!")
    print("\n📝 Next steps:")
    print("   1. Add your content to the topic files")
    print("   2. Run: pip install -r requirements.txt")
    print("   3. Run: mkdocs serve") 
    print("   4. Visit: http://127.0.0.1:8000")

if __name__ == "__main__":
    main()
