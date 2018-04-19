#! /bin/bash -i

plink --bfile /fslhome/inwosu/fsl_groups/fslg_KauweLab/compute/ADGC1KG2014/ADGC_Combined_Data/unrelated_dataset/backup/ADGC_unrelated_newgsk --recode vcf --out /fslhome/inwosu/fsl_groups/fslg_KauweLab/compute/ADGC1KG2014/ADGC_Combined_Data/unrelated_dataset/backup/ADGC_unrelated_newgsk --threads 4

plink --bfile ADGC_unrelated_newgsk --filter-cases --make-bed --out case_only

plink --bfile ADGC_unrelated_newgsk --filter-controls --make-bed --out controls_only

plink --bfile controls_only --bmerge case_only.bed case_only.bim case_only.fam --make-bed --out merge

vcftools --vcf ADGC_unrelated_newgsk_edited.vcf --out filtered --remove famList.txt --recode
