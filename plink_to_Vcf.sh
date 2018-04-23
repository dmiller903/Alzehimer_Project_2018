#This script generates a file in vcf format from plink format
#The script also filters the vcf file by excluding individuals in a text file passed to it

#! /bin/bash

plink --bfile input_fileset --recode vcf --out output_file 

vcftools --vcf input_file.vcf --out filtered --remove exclude_list.txt --recode --recode-INFO-all
